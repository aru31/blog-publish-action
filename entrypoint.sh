#!/bin/bash

# to exit if there is any status code of non zero
set -e

echo "Hello from the bash world"
echo "test variable -> ${INPUT_TEST_VARIABLE}"
python3 /app/src/main.py ${INPUT_TOKEN_DEVTO}