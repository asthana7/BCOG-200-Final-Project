# Wave 'Em Around
**BCOG-200 Final Project by Ananya Asthana**
I created a hand-tracking Song Adjuster. The idea is that it'll use computer vision and motion tracking to allow users to control certain aspects of a song. These aspects will include the frequency, speed, and volume. I plan to assign the left hand for frequency, the right hand for the speed,and the distance between the two as volume. I plan to use OpenCV and Mediapipe to assist me with this project.

Disclaimer: I was inspired by an Instagram Reel I saw. Here's a link to the inspiration: https://www.instagram.com/reel/DFclaRKTW63/?
igsh=MXhrd3UzNnpodTU4eQ==

# Installation
#Install the required dependencies
pip install -r requirements.txt

# Testing
You can run the tests by running pytest in the root directory as a module.
python -m pytest

Introduction to the logic of the program: 
This program uses openCV and mediapipe to simultaneously track hand location and identify specific hand gestures in order to modify songs. Users can currently choose between a few different royalty-free audios and then control certain aspects of their listening experience using just their hands. 

The logic relies on the program identifying hand landmark locations to figure out the distance between two landmarks (such as the points between right index finger and right thumb to adjust the frequency of the song). For song selection, I am relying on a few royalty-free and CC-licensed songs. 

Why would anyone use this?
- This program can be useful for music production and DJing on the spot.
- It can also be helpful for improving accessibility as it can be modified to not need a keyboard
