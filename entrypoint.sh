#!/bin/bash

# to exit if there is any status code of non zero
set -e

echo "Environment variables received"
echo "website -> ${INPUT_WEBSITE}"
echo "Repository & owner -> ${GITHUB_REPOSITORY}"
echo "-------------------------------------------------------------------------"
echo "Output of Python Code"

python3 /app/src/main.py ${INPUT_TOKEN} ${INPUT_WEBSITE} ${GITHUB_REPOSITORY}