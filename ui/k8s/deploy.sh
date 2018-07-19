#!/bin/bash

# deploy service
kubectl create -f ./heirloom-ui-dev-service.yaml

# deploy deployment (haha)
kubectl create -f ./heirloom-ui.dev.deployment.yaml
