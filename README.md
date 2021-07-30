### Tests and linter status:
[![Actions Status](https://github.com/RamiGaggi/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/RamiGaggi/python-project-lvl2/actions)
[![diff-check](https://github.com/RamiGaggi/python-project-lvl2/actions/workflows/gendiff-check.yml/badge.svg)](https://github.com/RamiGaggi/python-project-lvl2/actions/workflows/gendiff-check.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/6140e64cfc802ddecbd3/maintainability)](https://codeclimate.com/github/RamiGaggi/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6140e64cfc802ddecbd3/test_coverage)](https://codeclimate.com/github/RamiGaggi/python-project-lvl2/test_coverage)

## Install
1) Clone repository ```git clone https://github.com/RamiGaggi/edu-diff-generator.git```
2) Go to working directory ```cd edu-diff-generator```
3) Install dependencies ```make install```
4) Install as package```make package-install``` or use ```poetry run```


## Usage
```
gendiff -f json tests/fixtures/recursive/file1.json  tests/fixtures/recursive/file2.yaml
```
```
poetry run gendiff -f json tests/fixtures/recursive/file1.json  tests/fixtures/recursive/file2.yaml
```
[![asciicast](https://asciinema.org/a/8SE7wW9mDLf8phUtk5riw9JxH.svg)](https://asciinema.org/a/8SE7wW9mDLf8phUtk5riw9JxH)