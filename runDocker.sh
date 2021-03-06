xhost +local:docker
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
touch /tmp/.docker.xauth
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -
docker run -it --rm --device=/dev/video0 -e DISPLAY=$DISPLAY \-v $XSOCK:$XSOCK -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH -v ${PWD}:/src  -it deanazor/motion
xhost -local:docker