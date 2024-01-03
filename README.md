# DataMesh
> A collection of tools for Data Mesh architectural approach.


## Data Contract Validation
The library can be used to validate your .yaml data contract against Open Data Contract Standard JSON schema from [Bitol-io / open-data-contract-standard](https://github.com/bitol-io/open-data-contract-standard/) 


### Installation
```
pip install -U datamesh
```

### Usage
```bash
data-contract-validation <path_to_contract_yaml_file> <optional_path_to_standards_json_schema>
```

or in Python
```python
from datamesh.contract import Validator

validation_errors = (
    Validator(
        contract="examples/all/postgresql-adventureworks-contract.yaml",
        standard="schema/odcs-json-schema.json" # This is optional
    ) 
    .print_report() # Prints validation results and returns `self`
    .errors # List of errors 
)
```
```
🚩 Validation errors:
.
│
├──[]
│  └── 'datasetName' is a required property
│
├──[]
│  └── 'quantumName' is a required property
│
├──['kind']
│  └── 'managedDataset' is not one of ['DataContract']
```

### [Streamlit App](https://datamesh.streamlit.app/)
[![streamlit app screenshot](https://raw.githubusercontent.com/georgegach/DataMesh/main/docs/streamlit/streamlit-screenshot.png)](https://datamesh.streamlit.app/)


## Contribution

Feel free to contribute to the project under free and open-source GPLv3 license. 


## Resources

- [Open Data Contract Standard (ODCS)](https://github.com/bitol-io/open-data-contract-standard)
- [PayPal open sources its data contract template](https://jgp.ai/2023/05/01/paypal-open-sources-its-data-contract-template/)

