#!/usr/bin/env bash

password=$1

echo "push docker image to the repo"
docker login -u="chaimozdsd" -p=${password}
docker push chaimozdsd/dsd