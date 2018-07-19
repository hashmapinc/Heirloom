#!/bin/bash

docker run \
    --rm \
    -it \
    -p 80:80 \
    -p 8123:8123 \
    -v /Users/randypitcherii/projects/Heirloom/ui/heirloom_ui:/mnt/heirloom_ui \
    hashmapinc/heirloom-ui  /bin/bash