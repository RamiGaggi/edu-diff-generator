install:
	poetry install

build:
	poetry build

test:
	poetry run pytest -vv tests

test-coverage:
	poetry run coverage run --source=gendiff -m pytest tests && poetry run coverage xml

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl
	
lint:
	poetry run flake8 gendiff

.PHONY: build