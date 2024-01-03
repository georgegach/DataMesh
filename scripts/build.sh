#!/bin/bash

rm -rf dist build DataMesh.egg-info 
pip uninstall DataMesh -y
python setup.py sdist bdist_wheel
pip install --find-links=dist DataMesh --no-index
rm -rf build DataMesh.egg-info 