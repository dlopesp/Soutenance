import cv2
import os
import numpy as np
from PIL import Image

# Directory containing your PNG frames
image_folder = '.'

# Video output file
video_name = 'output.mp4'

# Collect the image file names
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()  # Ensure frames are in order

# Get the dimensions of the first image
frame = Image.open(os.path.join(image_folder, images[0]))
width, height = frame.size

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
fps = 5  # Frames per second
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

for image in images:
    # Open the image using PIL
    frame = Image.open(os.path.join(image_folder, image))
    
    # Convert the PIL image to a NumPy array (compatible with OpenCV)
    frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    
    # Write the frame to the video
    video.write(frame)

# Release the video writer object
video.release()

print("Video has been created successfully.")

