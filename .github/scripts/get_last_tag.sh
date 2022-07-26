#!/bin/bash

if ${{ github.event.inputs.semver_level }}; then
  echo "SEMVER_LEVEL=${{ github.event.inputs.semver_level }}" >> $GITHUB_ENV
else
  echo "SEMVER_LEVEL=$SEMVER_LEVEL" >> $GITHUB_ENV
fi
echo $SEMVER_LEVEL

TOKEN=$(curl -s -H "Content-Type: application/json" -X POST -d '{"username": "'${DOCKERHUB_USER}'", "password": "'${DOCKERHUB_PASSWD}'"}' https://hub.docker.com/v2/users/login/ | jq -r .token)
echo $TOKEN
export TOKEN=$TOKEN