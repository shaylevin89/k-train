#!/bin/bash


echo $SEMVER_LEVEL
TOKEN=$(curl -s -H "Content-Type: application/json" -X POST -d '{"username": "'${DOCKERHUB_USER}'", "password": "'${DOCKERHUB_PASSWD}'"}' https://hub.docker.com/v2/users/login/ | jq -r .token)
echo $TOKEN



curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://hub.docker.com/v2/repositories/$DOCKER_REPO_NAME/$DOCKER_IMAGE_NAME/tags | jq
