PYTHON = env PYTHONPATH=. bin/python

default:
run: start-dev-server
start-dev-server:
	$(PYTHON) etpaste/main.py
bootstrap:
	./utils/bootstrap
.PHONY: default bootstrap run start-dev-server
