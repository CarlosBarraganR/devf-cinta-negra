#Runtime
FROM python:3.6

#Copy our require enviroment to the build
COPY damnificados/requirements.txt /damnificados/requirements.txt

#We run our requirements.txt file to avoid re-installing every time we make a new build or our image
RUN pip install -r /damnificados/requirements.txt

#Setting working directory
WORKDIR /damnificados

#Copy current directory contents into the container
COPY damnificados /damnificados

#Install the environment (bin/libs) required for the app to run
RUN pip install -r requirements.txt

#Create a conection between the container and a listener @Localhost in port 8000 (In this case a mySQL database)
CMD gunicorn --bind 0.0.0.0:8000 damnificados.wsgi:application