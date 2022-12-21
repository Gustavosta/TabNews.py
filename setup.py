#!/usr/bin/python
# -*- coding: utf-8 -*-

import setuptools


with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tabnews",
    version="1.0.0",
    author="Gustavo Santana",
    author_email="sowlfie@gmail.com",
    description='Python library for communication via API to the website: "TabNews.com.br"',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gustavosta/Tabnews.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)