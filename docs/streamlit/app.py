import streamlit as st
from datamesh.contract import Validator
import yaml
import tempfile

def validate_yaml(yaml_content):
    validation = Validator(yaml_content)
    return validation.is_valid(), validation.errors

# Streamlit interface
st.title("✅ ODCS Data Contract Validator")
st.markdown("> The following streamlit app uses [DataMesh](https://github.com/georgegach/DataMesh) python library underneath to validate *.yaml contracts* against [Open Data Contract Standard](https://github.com/bitol-io/open-data-contract-standard) JSON Schema, part of Linux Foundation.")

st.markdown("___")

uploaded_file = st.file_uploader("Choose a YAML file containing data contract", type="yaml")

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".yaml") as fp:
        fp.write(uploaded_file.getvalue().decode("utf-8"))
        fp.seek(0)

        with open(fp.name, 'r') as file:

            yaml_content = yaml.safe_load(file)
            is_valid, errors = validate_yaml(yaml_content)

            if is_valid:
                st.success("💚 The YAML file is valid.")
            else:
                st.error("🚩 Validation failed. Errors:")
                st.write(errors)
