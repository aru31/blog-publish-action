FROM python:alpine3.15

# copy the requirements.txt file and run it.


# Copies your code file  repository to the filesystem
COPY entrypoint.sh /app/entrypoint.sh

# change permission to execute the script and
RUN chmod +x /app/entrypoint.sh

# copying code for running
COPY src /app

# file to execute when the docker container starts up
ENTRYPOINT ["/app/entrypoint.sh"]