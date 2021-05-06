SHELL := /bin/bash

setup: install dev

install:
	virtualenv .venv
	source .venv/bin/activate
	pip3 install -r requirements.txt

dev:
	uvicorn src.jobs_api:app

health-check:
	curl localhost:8000/health

deploy:
	uvicorn src.jobs_api:app --host 0.0.0.0 --port 443 --ssl-keyfile=./certs/privkey.pem --ssl-certfile=./certs/fullchain.pem


