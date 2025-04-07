#right now these are all in this file, but i will have to figure out what class/function needs to be in which file

import tkinter as tk
class Display():
    screen_size = (800, 600)
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Wave 'Em Around")
        self.init_window()

    def init_window(self):
        #set up main window with the following elements:
        #- a frame of size (800, 300) for where user can see themself and where the hand-tracking takes place
        #- a frame of size (400, 300) packed below and to the left of the hand_tracking_frame for selecting the song through spotify
        #- a menu to guide the users through the whole process
        pass
class Hand():
    #base class for using mediapipe's hand-tracking as well as landmark identification (such location of the left index finger)
    def _init__(self):
        self.hand = track_hand_motion()
        #track_hand_motion() will be defined in a separate file along with distance(point1, point2)
        #this file will also contain the code for mediapipe's hand-recognition and tracking 
        
class Left_Hand(Hand):
    #child class in charge of keeping track of the left hand and its landmarks
    def __init__(self):
        self.left_hand = self.left_hand()

    def left_hand(self):
        #function to figure out which hand is the left hand
        pass
        

    def modify_frequency(self):
        #function that uses the location of the index finger and thumb of the left hand as parameters for distance(point1, point2) and creates an if-else statement
        #if new_dist > current_dist: frequency increases
        #if new_dist < current_dist: frequency decreases
        #else (no change): no change in frequency
        pass

class Right_Hand(Hand):
    #child class in charge of keeping track of the right hand, its landmarks and gestures
    def __init__(self):
        self.right_hand = self.right_hand()
    
    def right_hand(self):
        #function to figure out which hand is the right hand
        pass

    def modify_speed(self):
        #function that uses the location of the index finger and thumb of the right hand as parameters for distance(point1, point2) and creates an if-else statement
        #if new_dist > current_dist: speed increases
        #if new_dist < current_dist: speed decreases
        #else (no change): no change in speed
        pass

    def pause_song(self):
        #function that recognizes the shape of the right-hand as ☝️ (pre-defined gesture which is palm facing forward, only index finger point up) and pauses song
        pass
    
    def like_song(self):
        #function that recognizes the shape of the right-hand as 🤘 (pre-defined gesure which is palm facing forward, pointer and pinky finger raised, I love you in ASL)
        #then hearts the song and adds it to Spotify library
        pass


class Song():
    #base class for using Spotify API and accessing Spotify database to allow users to log into their spotify account and search for a song of their liking
    def __init__(self):
        self.song = selected_song()
        #selected_song() will be defined in a separate file along with any functions that allow access to attributes of the song (such as the frequency, speed)
        #this file will also contain the code for spotipy (the library i am using to access Spotify's API) 
        pass

def main():
    my_display = Display()
    my_display.root.mainloop()


if __name__== "__main__":
    main()
    
    
        