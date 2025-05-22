# No-Hand Volume Control
**BCOG-200 Final Project by Ananya Asthana**

I created a hand-tracking Volume Adjuster. The idea is that it'll use computer vision and motion tracking to allow users to control the volume of a song. I assigned the  distance between the index fingers as volume. I plan to use OpenCV and Mediapipe to assist me with this project.

Disclaimer: I was inspired by an Instagram Reel I saw. Here's a link to the inspiration: https://www.instagram.com/reel/DFclaRKTW63/?
igsh=MXhrd3UzNnpodTU4eQ==

# Setup Instructions

### Python Version

This project was developed and tested on **Python 3.12**

If you're using **Python 3.13** or any other version other than 3.12, some packages (such as mediapipe) may not behave consistently. I would recommend using **Python 3.12** in a virtual environment.


# Installation

#Install the required dependencies

pip install -r requirements.txt

# Testing

You can run the tests by running pytest in the root directory as a module.

python -m pytest

Introduction to the logic of the program: 
This program uses openCV and mediapipe to simultaneously track hand location to control the volume level. Users can currently choose between a few different royalty-free audios and then control certain aspects of their listening experience using just their hands. 

The logic relies on the program identifying hand landmark locations to figure out the distance between two landmarks For song selection, I am relying on a few royalty-free and CC-licensed songs. 
