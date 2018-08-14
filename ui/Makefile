all: dev 

# create venv
venv:
	-python3 -m virtualenv env

# install requirements
install: venv
	source env/bin/activate; \
	pip install -r heirloom/ui/requirements.txt

# migrate database
db:
	source env/bin/activate; \
	export FLASK_APP=heirloom/ui/main.py; \
	export FLASK_DEBUG=1; \
	flask db migrate; \
	flask db upgrade

# get venv-activated shell
shell: db
	source env/bin/activate; \
	python;

# run local dev server
dev: install db
	source env/bin/activate; \
	export FLASK_APP=heirloom/ui/main.py; \
	export FLASK_DEBUG=1; \
	python -m flask run --host '0.0.0.0'

# build the image
build: 
	docker build -t hashmapinc/heirloom-ui .

# push the image
push: build 
	docker push hashmapinc/heirloom-ui

# run the container
run: 
	docker run --rm -it -p 80:80 hashmapinc/heirloom-ui