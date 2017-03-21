FROM ubuntu:latest
MAINTAINER David Gwizdala
RUN apt-get update && apt-get install -y \
	git \
	python3.4 \
	python3-pip
#update pip
RUN pip3 install --upgrade pip
RUN apt-get install -y python-pip python-dev build-essential

#download flask-server
RUN pip3 install Flask-API
RUN pip install Flask-API
RUN pip3 install flask
RUN pip3 install markdown
RUN pip install requests==1.1.0

#download pymongo
RUN apt-get install -y mongodb
RUN pip install pymongo

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

#Expose port 8080 for testing
EXPOSE 5000
#start the server
CMD python3 -m swagger_server
