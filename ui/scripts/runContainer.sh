#!/bin/bash

docker run \
    --rm \
    -it \
    -p 80:80 \
    -v /Users/randypitcherii/projects/Heirloom/ui/heirloom:/mnt/heirloom \
    hashmapinc/heirloom-ui  /bin/bash