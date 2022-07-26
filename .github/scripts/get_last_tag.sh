#!/bin/bash

TOKEN=$(curl -s -H "Content-Type: application/json" -X POST -d '{"username": "'${DOCKERHUB_USER}'", "password": "'${DOCKERHUB_PASSWD}'"}' https://hub.docker.com/v2/users/login/ | jq -r .token)
echo $TOKEN
export TOKEN=$TOKEN