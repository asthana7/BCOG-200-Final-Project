# BCOG-200-Final-Project
I plan to create a hand-tracking Song Adjuster. The idea is that it'll use computer vision and motion tracking to allow users to control certain aspects of a song. These aspects will include the frequency, speed, volume of the song as well as be able to skip, pause, or restart a song. I plan to assign the left hand for frequency, the right hand for the speed, the distance between the two as volume, and specific hand gestures for recognising to pause or play a song. I plan to use OpenCV and Mediapipe to assist me with this project.

Disclaimer: I was inspired by an Instagram Reel I saw, but I am not following any tutorials or have access to any source codes. Here's a link to the inspiration: https://www.instagram.com/reel/DFclaRKTW63/?
igsh=MXhrd3UzNnpodTU4eQ==


Introduction to the logic of the program: 
This program uses openCV and mediapipe to simultaneously track hand location and identify specific hand gestures in order to modify songs. Users can currently choose between a few different royalty-free audios and then control certain aspects of their listening experience using just their hands. 

The logic relies on the program identifying hand gestures (such as index finger pointing up to pause the song, thumbs down to skip the song, and identifying hand landmark locations to figure out the distance between two landmarks (such as the points between right index finger and right thumb to adjust the frequency of the song). For song selection, I am relying on a few royalty-free and CC-licensed songs. 

Why would anyone use this?
- This program can be useful for music production and DJing on the spot.
- It can also be helpful for improving accessibility as it can be modified to not need a keyboard

THINGS I NEED TO IMPROVE ON (BEFORE FINAL PROJECT SUBMISSION):
1. GUI needs to be better
2. Integrate more features (such as specialized gesture recognition)
