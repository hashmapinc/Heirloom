all: venv install build run 

# create venv
venv:
	-python3 -m virtualenv env

# install requirements
install:
	pip3 install -r heirloom/ui/requirements.txt

# run local dev server
dev:
	sh scripts/runDevServer.sh

# build the ui image
build: 
	sh scripts/buildImage.sh

# run the ui container
run: 
	sh scripts/runContainer.sh