SHELL := /bin/bash

setup: install dev

install:
	virtualenv .venv
	source .venv/bin/activate
	pip3 install -r requirements.txt

dev:
	uvicorn src.jobs_api:app --reload

health-check:
	curl localhost:8000/health
