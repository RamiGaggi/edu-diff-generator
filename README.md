# Diff Generator

Difference generator - CLI utility that determines the difference between two data structures(json, yaml).
Generating a report in plain text, stylish and json format.

[![asciicast](https://asciinema.org/a/8SE7wW9mDLf8phUtk5riw9JxH.svg)](https://asciinema.org/a/8SE7wW9mDLf8phUtk5riw9JxH)

## Tests and linter status(CI)

[![diff-check](https://github.com/RamiGaggi/python-project-lvl2/actions/workflows/gendiff-check.yml/badge.svg)](https://github.com/RamiGaggi/python-project-lvl2/actions/workflows/gendiff-check.yml)

## Codeclimate

[![Maintainability](https://api.codeclimate.com/v1/badges/5877a0c524a9eb3a8ef8/maintainability)](https://codeclimate.com/github/RamiGaggi/edu-diff-generator/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5877a0c524a9eb3a8ef8/test_coverage)](https://codeclimate.com/github/RamiGaggi/edu-diff-generator/test_coverage)

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
