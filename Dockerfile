FROM ubuntu

# Update default OS packages
RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

# Install python
RUN apt-get update && apt-get install -y python3.8 python3-distutils python3-pip python3-apt

# Copy requirements.txt from the project into the Docker Image
COPY requirements.txt requirements.txt

# Install project dependencies
RUN pip3 install -r requirements.txt

# Make folder called /project and cd into it
WORKDIR /project

COPY . .
