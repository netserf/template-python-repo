# template-python-repo v0.2.0

<!-- markdown-link-check-disable -->
[![Actions Status](https://github.com/netserf/template-python-repo/workflows/Lint/badge.svg)](https://github.com/netserf/template-python-repo/actions)
[![Actions Status](https://github.com/netserf/template-python-repo/workflows/Tests/badge.svg)](https://github.com/netserf/template-python-repo/actions)
<!-- markdown-link-check-enable -->

## What?

TODO - Describe the functionality of this package

## Why?

TODO - Describe the motivation for this package

## Usage

TODO - Show how to use this package

## Manual Installation

TODO - Replace this section with instructions for installing this package

To install this package manually, clone the repository and run the following
commands:

```bash
git clone git@github.com:netserf/template-python-repo.git
pip install -r requirements.txt
pip install -e .
python setup.py bdist_wheel
pip install $(ls dist/*.whl | tail -1)
```

## Testing & Linting

For tests and linting, run the following command:

```bash
pytest -v
pylint template_python_repo_package_name/ tests/
black --check template_python_repo_package_name/ tests/
```

## Versioning

This package uses [Semantic Versioning](https://semver.org/). To make version
updates use the following commands:

```bash
bumpversion [major|minor|patch]
```

## Future Improvements

TODO - Describe future improvements to this package

## Licence

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Attribution

TODO - Provide attribution for any third-party code used in this package

## Template Checkist Steps

- [ ] Update all references to `template_python_repo_package_name` with new
  package name
- [ ] Update template-python-repo to new repo / project name
- [ ] Update blank fields in `setup.py`
- [ ] Update all URL references in `README.md`
- [ ] Run `pre-commit install` to install pre-commit hooks
- [ ] Run `pre-commit run --all-files` to test pre-commit hooks
- [ ] Remove this section from `README.md`
