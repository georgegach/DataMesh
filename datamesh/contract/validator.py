import os
import json
import yaml
from typing import List, Dict, Any, Union
from jsonschema import Draft201909Validator
import argparse
import pkg_resources


class Validator:
    """
    A class to validate YAML data contracts against Open Data Contract Standard json schemas.

    Attributes:
        contract (Union[str, Dict[str, Any]]): A YAML contract or the path to a YAML file.
        standard (Union[str, Dict[str, Any]]): A JSON standard or the path to a JSON schema file.
        errors (List[Dict[str, Any]]): A list to store validation errors.
    """

    def __init__(
        self, 
        contract: Union[str, Dict[str, Any]], 
        standard: Union[str, Dict[str, Any]] = None
    ):
        """
        Initialize the Validator with a contract and a standard, and perform validation.

        :param contract: A YAML contract or the path to a YAML file.
        :param standard: A JSON standard or the path to a JSON schema file.
        """
        if standard is None:
            standard = pkg_resources.resource_filename('datamesh', 'resources/odcs-json-schema.json')

        self.contract = self.load_contract(contract) if isinstance(contract, str) else contract
        self.standard = self.load_standard(standard) if isinstance(standard, str) else standard
        self.errors = self.validate()

    @staticmethod
    def load_standard(standard_path: str) -> Dict[str, Any]:
        """
        Load a JSON standard from a file.

        :param standard_path: Path to the JSON schema file.
        :return: The JSON standard as a dictionary.
        """
        with open(standard_path, "r", encoding='utf-8-sig') as file:
            return json.load(file)

    @staticmethod
    def load_contract(contract_path: str) -> Any:
        """
        Load a YAML contract from a file.

        :param contract_path: Path to the YAML file.
        :return: The YAML contract data.
        """
        with open(contract_path, "r") as file:
            return yaml.safe_load(file)

    def validate(self) -> List[Dict[str, Any]]:
        """
        Validate the contract against the standard.

        :return: A list of validation errors.
        """
        if not isinstance(self.standard, dict) or not isinstance(self.contract, dict):
            raise ValueError("Invalid input. Standard and contract must be dictionaries.")

        validation = Draft201909Validator(self.standard)
        errors = []
        for error in sorted(validation.iter_errors(self.contract), key=str):
            errors.append({
                "path": list(error.path),
                "message": error.message
            })
        return errors

    def is_valid(self) -> bool:
        """
        Check if the contract is valid against the standard.

        :return: True if valid, False otherwise.
        """
        return len(self.errors) == 0

    def print_report(self) -> 'Validator':
        """
        Print a report of the validation, showing errors if there are any.

        :return: Self to allow further method chaining.
        """
        def message_printer(message: str) -> str:
            if len(message) > 100:
                return message[:12] + "....." + message[-42:]
            return message

        if self.is_valid():
            print("✅ Data contract adheres to Open Data Contract Standard.")
        else:
            print("⚠️ Validation errors:\n.")
            for error in sorted(self.errors, key=lambda x: x['path']):
                print(f"│\n├──{error['path']}\n│  └── {message_printer(error['message'])}")

        return self


def main():
    parser = argparse.ArgumentParser(description="Validate a YAML data contract against a Open Data Contract Standard JSON schema.")
    parser.add_argument('contract', type=str, help="Path to the YAML data contract file.")
    parser.add_argument('--standard', type=str, help="Path to the JSON schema standard file (optional. Defaults to local copy of ODCS packaged within the library).", default=None)

    args = parser.parse_args()

    try:
        validator = Validator(contract=args.contract, standard=args.standard)
        validator.print_report()
        return 0 if validator.is_valid() else 1
    except Exception as e:
        print(f"Error occurred: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
