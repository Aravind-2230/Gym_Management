# use base python image
FROM python:3.9-slim

# set workspace
WORKDIR /app

# copy the requirements file
COPY requirements.txt /app

# install all the dependencies
RUN pip install -r requirements.txt

# copy the entire project files
COPY . /app

# expose container port for flask application
EXPOSE 5000

# cmd to run the application
CMD ["flask", "run", "--host", "0.0.0.0"]