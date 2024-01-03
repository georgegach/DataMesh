from setuptools import setup, find_packages

setup(
    name='DataMesh',
    version='0.1.0',
    author='Giorgi Gachechiladze',
    author_email='georgegach@outlook.com',
    description='A collection of tools for Data Mesh architectural approach.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/georgegach/DataMesh',
    packages=find_packages(),
    install_requires=[
        'jsonschema',
        'pyyaml'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
