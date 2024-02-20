code-format:
	black --skip-string-normalization .
	isort .

migrate:
	python manage.py makemigrations
	python manage.py migrate

run-django:
	python manage.py runserver 0.0.0.0:8000

install-dev-dep:
	pip install -r requirements.dev.txt

install-prod-dep:
	pip install -r requirements.txt