#Runtime
FROM python:3.6

#Setting working directory
WORKDIR /damnificados

#Copy our require enviroment to the build
COPY damnificados/requirements.txt /damnificados/requirements.txt

#We run our requirements.txt file to avoid re-installing every time we make a new build or our image
RUN pip install -r /damnificados/requirements.txt

#Copy current directory contents into the container
COPY damnificados /damnificados

#Install the environment (bin/libs) required for the app to run
RUN pip install -r requirements.txt

CMD sh config.sh