#==============================================================================
# Dockerfile for the ui of the heirloom project
#
# Flask api for user interaction with heirloom
#==============================================================================
FROM python:3

# add application files
COPY heirloom/ /heirloom

# set workdir to the UI root dir
WORKDIR /heirloom/ui

# point flask to the application, add heirloom ui to the python path
ENV FLASK_APP=heirloom/ui/main.py \
    PYTHONPATH=/:$PYTHONPATH

# install the application and database
RUN pip install -r requirements.txt && \
    mkdir data && \
    flask db init && \
    flask db migrate && \
    flask db upgrade


# open flask app port
EXPOSE 80

# start flask app
CMD ["python", "-m", "flask", "run", "--port", "80", "--host" ,"0.0.0.0"]
#==============================================================================