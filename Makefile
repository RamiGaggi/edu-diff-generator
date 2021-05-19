install:
	poetry install

build:
	poetry build

test-build:
	poetry run pytest

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl
	
lint:
	poetry run flake8 gendiff