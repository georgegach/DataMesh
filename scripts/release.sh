#!/bin/bash

python setup.py sdist bdist_wheel
twine upload dist/*
rm -rf dist build DataMesh.egg-info