import argparse
import cv2
import numpy as np

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input file"

    # -- Create the arguments
    parser.add_argument("-i", help=i_desc)
    args = parser.parse_args()

    return args


def capture_stream(args):
    ### TODO: Handle image, video or webcam

    ### TODO: Get and open video capture

    ### TODO: Re-size the frame to 100x100

    ### TODO: Add Canny Edge Detection to the frame, 
    ###       with min & max values of 100 and 200
    ###       Make sure to use np.dstack after to make a 3-channel image

    ### TODO: Write out the frame, depending on image or video

    ### TODO: Close the stream and any windows at the end of the application


def main():
    args = get_args()
    capture_stream(args)


if __name__ == "__main__":
    main()
