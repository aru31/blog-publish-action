#!/bin/bash

# to exit if there is any status code of non zero
set -e

echo "Hello from the bash world"
echo "test variable -> ${INPUT_TEST_VARIABLE}"
echo "Github Token  -> ${INPUT_TOKEN_GITHUB}"
echo "Random Token  -> ${INPUT_TOKEN_RANDOM}"

python3 /app/src/main.py ${INPUT_TOKEN_DEVTO}