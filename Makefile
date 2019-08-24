docker:
	docker-compose -f docker-compose.yml build --no-cache
	docker-compose -f docker-compose.yml up

run:
	python manage.py
	
clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

test:
	pytest tests/ -v

coverage:
	pytest --cov=src tests/

lint:
	pylint src/*

