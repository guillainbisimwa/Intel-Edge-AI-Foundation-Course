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

# Choosing Models
I chose the following models for the three tasks:

Human Pose Estimation: human-pose-estimation-0001
Text Detection: text-detection-0004
Determining Car Type & Color: vehicle-attributes-recognition-barrier-0039
Downloading Models
To navigate to the directory containing the Model Downloader:

``` bash
cd /opt/intel/openvino/deployment_tools/open_model_zoo/tools/downloader
```

Within there, you'll notice a downloader.py file, and can use the -h argument with it to see available arguments. For this exercise, --name for model name, and --precisions, used when only certain precisions are desired, are the important arguments. Note that running downloader.py without these will download all available pre-trained models, which will be multiple gigabytes. You can do this on your local machine, if desired, but the workspace will not allow you to store that much information.

Note: In the classroom workspace, you will not be able to write to the /opt/intel directory, so you should also use the -o argument to specify your output directory as /home/workspace (which will download into a created intel folder therein).

Downloading Human Pose Model

``` bash
sudo ./downloader.py --name human-pose-estimation-0001 -o /home/workspace
```

``` bash
sudo ./downloader.py --name text-detection-0004 --precisions FP16 -o /home/workspace
```

``` bash
sudo ./downloader.py --name vehicle-attributes-recognition-barrier-0039 --precisions INT8 -o /home/workspace
```


# Commit a container with new configurations


``` bash
sudo docker commit --change "ENV DEBUG true" CONTAINER_ID  my_name/my_image:version3

```
sudo docker commit --change "ENV DEBUG true" fb63594bf93b  guillainbisimwa/openvino:version4

