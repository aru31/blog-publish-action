#!/bin/bash

# to exit if there is any status code of non zero
set -e

echo "Hello from the bash world"
echo "website -> ${INPUT_WEBSITE}"

python3 /app/src/main.py ${INPUT_TOKEN} ${INPUT_WEBSITE}