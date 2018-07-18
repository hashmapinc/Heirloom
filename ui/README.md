# Heirloom UI
This directory contains the code for the Heirloom frontend. All web UI code will live here.

## Development Instructions
`cd` into this directory and run the `testImage.sh` script. This will build the application and run a container shell with the proper ports exposed.

To start the application within the container, run `python -m heirloom_ui.app` and open `localhost:80` on your local browser to see live changes.

**Note:** ensure that you update the `runContainer.sh` script to point to the volume locations suitable for your environment.