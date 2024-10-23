from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='maxpackage',
    version='0.4',
    packages=find_packages(),
    description='A simple Python package',
    author='Max Rerisi',
    install_requires=required
)