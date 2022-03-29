FROM python:alpine3.15

# copy the requirements.txt file and run it.
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

# Copies your code file  repository to the filesystem
COPY entrypoint.sh /app/entrypoint.sh

# change permission to execute the script and
RUN chmod +x /app/entrypoint.sh

# copying code for running
COPY src /app

# file to execute when the docker container starts up
ENTRYPOINT ["/app/entrypoint.sh"]