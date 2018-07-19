#==============================================================================
# Dockerfile for the ui of the heirloom project
#
# Flask api for user interaction with heirloom
#==============================================================================
FROM python:3

# add flask app
COPY heirloom_ui/ /heirloom_ui

# install python libs
WORKDIR /heirloom_ui
RUN pip install -r requirements.txt

# add the app to the python path
ENV PYTHONPATH=/:$PYTHONPATH

# open flask app port
EXPOSE 80

# dev port
EXPOSE 8123

# start flask app
CMD ["python", "-m", "heirloom_ui.app"]
#==============================================================================