# How to Dockerize

## Create a file named Dockerfile

### Add the base Image

```Dockerfile
# In Dockerfile
FROM ubuntu
```

## Build and Tag the Image

```bash
docker build -t <YOUR DOCKER HUB USERNAME>/<YOUR IMAGE NAME>
```

## Create the Container

```bash
docker run -it <YOUR DOCKER HUB USERNAME>/<YOUR IMAGE NAME>
```


### Verify that the Container is a different OS

```bash
cat /etc/lsb-release
```

You should see output similar to:

```bash
root@854c4e712040:/project# cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.3 LTS"
```

## Update Dockerfile

```Dockerfile
FROM ubuntu

# Update default OS packages
RUN apt-get update && apt-get install -y software-properties-common gcc vim && \
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
```

## Recreate the Container

```bash
docker run -it <YOUR DOCKER HUB USERNAME>/<YOUR IMAGE NAME>
```

## Run the script

With the project in our new container we can now run

```bash
python3 cleaner.py
```

and we should see output like

```bash
root@8e4f4b252200:/project# python3 cleaner.py 
    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130    409.10
1         60 2020-12-02    117       145    479.00
2         60 2020-12-03    103       135    340.00
3         45 2020-12-04    109       175    282.40
4         45 2020-12-05    117       148    406.00
...
```

and if you run `ls` the `plot.png` should be generated.

```bash
root@8e4f4b252200:/project# ls
Dockerfile  README.md  cleaner.py  data.csv  plot.png  requirements.txt
```

## Push to Docker Hub

```bash
docker push <YOUR DOCKER HUB USERNAME>/<YOUR IMAGE NAME>
```
