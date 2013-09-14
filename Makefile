PYTHON = env PYTHONPATH=. bin/python

default:
run: start-dev-server
start-dev-server:
	$(PYTHON) etpaste/main.py
bootstrap:
	./utils/bootstrap
TAGS:
	etags -R --exclude='etpaste/static/jquery/*' --exclude='etpaste/static/bootstrap/*' etpaste utils
.PHONY: default bootstrap run start-dev-server TAGS
