install:
	poetry install

build:
	poetry build

test-build:
	poetry run pytest tests

test-coverage:
	poetry run coverage run --source=gendiff -m pytest tests

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl
	
lint:
	poetry run flake8 gendiff