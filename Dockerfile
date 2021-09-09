# Use an official Python runtime as a parent image
FROM python:3.8-slim

RUN apt-get update && apt-get install -y python3-opencv
RUN apt-get install libsm6 libxext6 libxrender-dev -y

# Set the working directory to /app
WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

ENV QT_DEBUG_PLUGINS=1

# Run app.py when the container launches
CMD ["python", "cam.py"]