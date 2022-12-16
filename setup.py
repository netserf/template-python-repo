#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", mode="r", encoding="utf-8") as reqs_file:
    install_requirements = reqs_file.readlines()

with open("requirements_dev.txt", mode="r", encoding="utf-8") as devreqs_file:
    test_requirements = devreqs_file.readlines()
    test_requirements.extend(install_requirements)

setup(
    author="",
    author_email="netserf.projects@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="",
    install_requires=install_requirements,
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=readme,
    name="template_python_repo_package_name",
    packages=find_packages(exclude=["tests"]),
    test_suite="tests",
    tests_require=test_requirements,
    version="0.2.1",
    url="",
)
