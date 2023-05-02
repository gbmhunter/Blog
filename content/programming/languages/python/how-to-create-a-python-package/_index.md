---
authors: [ Geoffrey Hunter ]
categories: [ Programming ]
date: 2023-05-02
draft: false
lastmod: 2023-05-02
tags: [ Python, packages, setuptools, pyproject, TOML, build, build tools ]
title: How To Create A Python Package
type: page
---

## Overview

PEP 621 introduced the `pyproject.toml` method of specifying package metadata, including how to build the package. The idea is that this method supports many different build systems, with the exact build system being mentioned under the `[build-system]` table inside the TOML file[^bib-python-pep-621].

The three main build systems that are supported as of 2023 are Setuptools, Flit and Poetry[^bib-python-pep-621].

## Use With setuptools

A basic example of a `pyproject.toml` that tells pip to use `setuptools` to build the package:

```toml
[build-system]
requires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
authors = [
    {name = "My name", email = "my_email@abc.com"},
]
description = "My package description."
readme = "README.md"
requires-python = ">=3.7"
dependencies = [
  "PyYAML ~= 5.0",
  "requests >= 2.20.0, < 3",
]
```

If you specify the build metadata this way, you DO NOT need to add the `setup.py` Python file that setuptools traditionally required.

Note that dependencies are not pulled from a `requirements.txt` file, instead you have to list them in the `pyproject.toml` file under `project.dependencies`. PEP 631 specifies how to write these dependencies (this PEP has been merged into the overarching PEP 621)[^bib-python-pep-631].

Once this file is in place, you should be able to run a test installation by pointing `pip` at this package on the local file system, e.g.:

```bash
$ pip install /path/to/package/
```

where `/path/to/package/` is the path to the directory in where the `pyproject.toml` resides.

## References

[^bib-python-pep-631]: Python (2022, Jun 14). _PEP 631 – Dependency specification in pyproject.toml based on PEP 508_. Retrieved 2023-05-02, from https://peps.python.org/pep-0631/.
[^bib-python-pep-621]: Python (2022, Oct 7). _PEP 621 – Storing project metadata in pyproject.toml_. Retrieved 2023-05-02, from https://peps.python.org/pep-0621/.