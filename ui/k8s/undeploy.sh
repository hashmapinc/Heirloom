#!/bin/bash

# undeploy service
kubectl delete service heirloom-ui-dev-service

# undeploy deployment (haha)
kubectl delete deployment heirloom-ui.dev.deployment
