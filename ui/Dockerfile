#==============================================================================
# Dockerfile for the ui of the heirloom project
#
# Flask api for user interaction with heirloom
#==============================================================================
FROM python:3

# add flask app
COPY heirloom/ /heirloom

# install python libs
WORKDIR /heirloom/ui
RUN pip install -r requirements.txt

# add the app to the python path
ENV PYTHONPATH=/:$PYTHONPATH

# open flask app port
EXPOSE 80

# start flask app
CMD ["python", "-m", "heirloom.ui.app"]
#==============================================================================