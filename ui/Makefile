all: dev 

# create venv
venv:
	-python3 -m virtualenv env

# install requirements
install: venv
	source env/bin/activate; \
	pip install -r heirloom/ui/requirements.txt

# get venv-activated shell
shell: install
	source env/bin/activate; \
	python;

# run local dev server
dev: install
	source env/bin/activate; \
	export FLASK_APP=heirloom/ui/main.py; \
	export FLASK_DEBUG=1; \
	python -m flask run --host '0.0.0.0'

# build the image
build: 
	docker build -t hashmapinc/heirloom-ui .

# run the container
run: 
	docker run --rm -it -p 80:80 hashmapinc/heirloom-ui