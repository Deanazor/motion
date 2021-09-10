#!/bin/bash
while getopts r:c:t: flag
do
    case "${flag}" in
            r) row=${VARIABLE:=1280};;
            c) col=${OPTARG:=720};;
            t) threshold=${OPTAR:=0.75G};;
    esac
done

xhost +local:docker
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
touch /tmp/.docker.xauth
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -
docker run -it --rm --device=/dev/video0 -e DISPLAY=$DISPLAY \-v $XSOCK:$XSOCK -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH -v ${PWD}:/src  -it deanazor/motion \
-r $row -c $col -t $threshold
xhost -local:docker