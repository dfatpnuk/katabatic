% pip install wheel
% pip install setuptools
% pip install twine

from setuptools import find_packages, setup

setup(
    name='katabatic',
    packages=find_packages(include=['katabatic']),
    version='0.1.0',
    description='An open source framework for tabular data generation',
    author='Nayyar Zaidi, Jaime Blackwell',
    install_requires=[],
    setup_requires=['pytest-runner'],
)
