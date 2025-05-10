# BCOG-200-Final-Project
I plan to create a hand-tracking Song Adjuster. The idea is that it'll use computer vision and motion tracking to allow users to control certain aspects of a song. These aspects will include the frequency, speed, volume of the song as well as be able to skip, pause, or restart a song. I plan to assign the left hand for frequency, the right hand for the speed, the distance between the two as volume, and specific hand gestures for recognising to pause or play a song. I plan to use OpenCV and Mediapipe to assist me with this project.

Disclaimer: I was inspired by an Instagram Reel I saw, but I am not following any tutorials or have access to any source codes. Here's a link to the inspiration: https://www.instagram.com/reel/DFclaRKTW63/?
igsh=MXhrd3UzNnpodTU4eQ==


Introduction to the logic of the program: 
This program uses openCV and mediapipe to simultaneously track hand location and identify specific hand gestures in order to modify songs. Users will log into their Spotify, pick a song, and then be able to control certain aspects of their listening experience using just their hands. 

The logic relies on the program identifying hand gestures (such as index finger pointing up to pause the song, thumbs down to skip the song, and identifying hand landmark locations to figure out the distance between two landmarks (such as the points between right index finger and right thumb to adjust the frequency of the song). For song selection, I am utilizing the Spotify API. 

Names of functions/methods and their parameters: 
1. a track_hand_motion(): will be in charge of identifying hands as the control panel for altering the song. It will also recognize certain patterns to alter the songs in specific ways, such as greater distance between the hands equals higher volume, or gesturing 'I love you' in ASL  equals liking a song and adding it to your Spotify library. I believe it will use similar concepts to an ASL hand-movement detector, and I will primarily use mediapipe's gesture recognition code.
  
2. distance(point1, point2): This project makes use of a lot of distance calculations, so it will benefit from having a re-usable function if I can generalise it enough. It would be used to calculate distances between two points, such as the pointer finger and thumb on each hand, since the distance between these objects will decide certain aspects of the song. I will use mediapipe's hand landmark output as point1 and point2.

3. spotify(): I intend for this project to be applicable to a wide range of songs, and the best available database of music is Spotify's library. I am using Spotify's API and spotipy in order to get users to be able to have their pick of songs.

4. setup_gui(): upon further examination, I believe I will have to use tkinter to create a window and be able to pack all the necessary elements. This will include a frame for where the main program runs (where you can see yourself changing aspects of the song), a frame for controlling your Spotify, and a menu to help guide the users throughout the process. 

5. modify_frequency(left_hand): I am assigning the left hand to tweak the frequency, with the distance between the index finger and thumb acting as the dial.

6. modify_speed(right_hand): I am assigning the right hand to tweak the speed of the song, with the distance between the index finger and thumb acting as the dial.

7. volume(point1, point2): The volume of the song will be directly proportional to the distance between the index fingers of the two hands (point1 and point2), calculated using the function defined above.

8. pause_song(right_hand): for all gesture-recognition based tasks, I intend to assign the right hand. For pausing, the gesture will be index finger pointing up.

9. like_song(right_hand): To heart the song and add it to the user's Spotify library, the gesture will be the ASL 'I love you' (palm facing forward with the thumb, index finger and pinky finger pointing up and middle and ring finger folded in)

Why would anyone use this?
- This program can be useful for music production and DJing on the spot.
- It can also be helpful for improving accessibility as it can be modified to not need a keyboard

