from setuptools import setup, find_packages

setup(
    name='DataMesh',
    version='0.1.2',
    author='Giorgi Gachechiladze',
    author_email='georgegach@outlook.com',
    description='A collection of tools for Data Mesh architectural approach.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/georgegach/DataMesh',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'jsonschema',
        'pyyaml'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'data-contract-validation=datamesh.contract.validator:main',
        ],
    },
    python_requires='>=3.6',
)
