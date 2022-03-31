#!/bin/bash

# to exit if there is any status code of non zero
set -e

echo "Environment variables received"
echo "website -> ${INPUT_WEBSITE}"
echo "Repository & owner -> ${GITHUB_REPOSITORY}"
echo "Log Level -> ${INPUT_LOG_LEVEL}"
echo "Finding out variables GITHUB_HEAD_REF -> ${GITHUB_HEAD_REF}, GITHUB_BASE_REF -> ${GITHUB_BASE_REF}, GITHUB_REF -> ${GITHUB_REF}, GITHUB_REF_NAME -> ${GITHUB_REF_NAME}, GITHUB_REF_TYPE -> ${GITHUB_REF_TYPE}"
echo "-------------------------------------------------------------------------"
echo "Output of Python Code"

python3 /app/src/main.py ${INPUT_TOKEN} ${INPUT_WEBSITE} ${GITHUB_REPOSITORY} ${INPUT_LOG_LEVEL}