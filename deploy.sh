#!/bin/bash

# Fetch the current branch name
BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

# Check if the branch name is one of prod, uat, or test
if [[ "$BRANCH_NAME" != "prod" && "$BRANCH_NAME" != "uat" && "$BRANCH_NAME" != "test" ]]; then
  echo "Error: Branch name must be one of prod, uat, or test."
  exit 1
fi

# Get the last commit hash
LAST_COMMIT_HASH=$(git rev-parse --short HEAD)

# Create the tag name
TAG_NAME="$BRANCH_NAME-$LAST_COMMIT_HASH"

# Build the Docker image
docker build --build-arg BRANCH_NAME=$BRANCH_NAME -t registry.cn-hangzhou.aliyuncs.com/legalgenius/legalgenius-backend-model:$TAG_NAME . --platform linux/amd64

# Push the Docker image to the registry
docker push registry.cn-hangzhou.aliyuncs.com/legalgenius/legalgenius-backend-model:$TAG_NAME

echo "Docker image built and tagged as registry.cn-hangzhou.aliyuncs.com/legalgenius/legalgenius-backend-model:$TAG_NAME"