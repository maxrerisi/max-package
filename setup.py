from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='myPackage',
    version='0.2.1',
    packages=find_packages(),
    description='A simple Python package',
    author='Max Rerisi',
    install_requires=required
)