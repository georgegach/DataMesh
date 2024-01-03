import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0, project_root)

from datamesh.contract import Validator


def main():
    validation_errors = (
        Validator(
            contract="examples/example-contract.yaml"
        )
        .print_report()
        .errors
    )

    print(f"\n{len(validation_errors)} errors")
    

if __name__ == "__main__":
    main()
