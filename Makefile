.PHONY: install test api docker sandbox

install:
	python -m pip install -r requirements.txt
	python -m pip install -e .

test:
	pytest

api:
	uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8080

docker:
	docker compose up --build

sandbox:
	curl -X POST http://localhost:8080/sandbox/reset
