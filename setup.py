#!/usr/bin/python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

requirements = [
    "cleverdict",
    "requests"
]

setuptools.setup(
    name="tabnews",
    version="1.1.0",
    author="Gustavo Santana",
    license='MIT',
    author_email="sowlfie@gmail.com",
    description='Python library for communication via API to the website: "TabNews.com.br"',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    keywords=["api", "tabnews", "tabcoins"],
    url="https://github.com/Gustavosta/Tabnews.py",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
