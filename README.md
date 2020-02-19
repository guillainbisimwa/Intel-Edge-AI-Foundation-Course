# Intel-Edge-AI-Foundation-Course

Use the image in another container
You can use this Docker image as a base image and use it in multiple Dockerfiles. An example of how to do this has been provided:

Move to sample-app directory and build the image

``` bash
docker build -t intel-edge .
```

Run the the container with X enabled (Linux)
Additionally, for running a intel-edge application that displays an image, you need to share the host display to be accessed from guest Docker container.

The X server on the host should be enabled for remote connections:
``` bash
xhost +
```

The following flags needs to be added to the docker run command:
``` bash
--net=host
--env="DISPLAY"
--volume="$HOME/.Xauthority:/root/.Xauthority:rw"
```
To run the intel-edge image with the display enabled:

``` bash
docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -ti d9c72c1ee970 /bin/bash
```
Finally disable the remote connections to the X server
``` bash
xhost -
```

### Use the image in another container

You can use this Docker image as a base image and use it in multiple Dockerfiles. An example of how to do this has been provided:

Move to root directory and build the image

``` bash
cd root directory
docker build -t my-intel-edge .
```

### Run a container

You can directly run a container based on this image or use this image across other images.

To run a container based on this image:

``` bash
docker run -ti d9c72c1ee970 /bin/bash
```
