FROM python:3
# Python output straight to terminal
ENV PYTHONUNBUFFERED 1
ENV WEB_APP_DIR=/code
RUN apt-get update && pip install --upgrade pip && mkdir $WEB_APP_DIR
WORKDIR $WEB_APP_DIR
ADD requirements.txt $WEB_APP_DIR/
RUN pip install -r requirements.txt
COPY . $WEB_APP_DIR/
