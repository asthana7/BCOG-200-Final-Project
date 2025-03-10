# BCOG-200-Final-Project
1. I plan to create a hand-tracking Song Adjuster. The idea is that it'll use computer vision and motion tracking to allow users to control certain aspects of a song. These aspects will include the frequency, speed, volume of the song as well as be able to skip, pause, or restart a song. I plan to assign the left hand for frequency, the right hand for the speed, the distance between the two as volume, and specific hand gestures for recognising to pause or play a song. I plan to use OpenCV and Mediapipe to assist me with this project.

Disclaimer: I was inspired by an Instagram Reel I saw, but I am not following any tutorials or have access to any source codes. Here's a link to the inspiration: https://www.instagram.com/reel/DFclaRKTW63/?
igsh=MXhrd3UzNnpodTU4eQ==

2a) a track_hand_motion() function- will be in charge of identifying hands as the control panel for altering the song, will also recognize certain patterns to alter the songs in specific ways, such as greater distance between the hands equals higher volume, or making a fist equals pausing a song. I believe it will use similar concepts to a ASL hand-movement detector.

2b) distance(): This project makes use of a lot of distance calculations, so it will benefit from having a re-usable function if I can generalise it enough. It would be used to calculate distances betweeen hands, and the pointer finger and thumb on each hand, the distance between these objects will decide certain aspects of the song. 

2c) access_freq(): I think this might be an (oversimplified) if, elif, else statement to decide how to affect the frequency. I picture having the distance between the pointer finger and thumb on the right hand as the controls for frequency. So this function will decide if the distance has been shortened, the frequency decreases, elif the distance is increased, the frequency increases, else the frequency stays the same. I can write similar functions for speed and volume.
