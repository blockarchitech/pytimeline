# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="pypebbletimeline",
    version="0.1.1",
    description="Interface with the Rebble Timeline Services in python.",
    license="MIT",
    author="BlockArchitech",
    packages=find_packages(),
    install_requires=["requests"],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ]
)
