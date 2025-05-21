#things I wanna implement in the GUI: (described in tkinter terms tho im using kivy)
#atleast 3 screens
#screen 1: is a window with the <h1> title <h1> (working title: Wave 'em Around), and it says <h2> "Welcome"<h2> <h4> "To the Future of Audio Design" <h4>
#screen 2: "Please log into Spotify" + "Please Select A Song"
#screen 3: The actual thing: So a frame with what ur camera sees (where the actual song modification happens) + a label with the song title and artist 
# and progress bar + 2 buttons (1 for changing song, 1 for exit program(?))
# + include a menu for what hand gestures do what in the program

#notes: users should be able to choose which part of the song theyre adjusting
#since it can recognise clockwise/ counter-clockwise, use that to forward/ rewind a song
# src/gui.py

from tkinter import filedialog, ttk, messagebox
import tkinter as tk
from src.gesture_manager import GestureManager
from src.audio_manipulation import AudioManager
import time
import threading
from src.hand_model import my_own_calc
import queue

class AudioGestureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wave 'Em Around")

        self.audio_manager = AudioManager()
        self.song_path = None
        self.gesture_manager = GestureManager(self.audio_manager)
        # self.gesture_queue = queue.Queue()
        # self.gesture_manager = GestureManager(self.gesture_queue)

        self.audio_data = None
        self.sr = None

        self.song_label = tk.Label(root, text = "No song selected")
        self.song_label.pack()

        self.select_song_button = tk.Button(root, text = "Select Song", command =lambda: self.select_song())
        self.select_song_button.pack()

        self.volume_label = tk.Label(root, text = "Volume: 1.0")
        self.volume_label.pack()

        self.pitch_label = tk.Label(root, text = "Pitch: 1.0")
        self.pitch_label.pack()

        self.speed_label = tk.Label(root, text = "Speed: 1.0")
        self.speed_label.pack()

        
        self.process_gestures_thread()
        threading.Thread(target=self.start_camera_feed, daemon = True).start()


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def select_song(self):
        #stop any song that might be alr playing
        self.audio_manager.stop_audio()

        # Trigger file selection and load audio file
        self.song_path = tk.filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.song_path:
            self.audio_data, self.sr = self.audio_manager.load_audio_file(self.song_path)
            self.song_label.config(text=f"Playing: {self.song_path.split('/')[-1]}")
            self.audio_manager.start_stream()
            self.process_gestures_thread()
        

    def start_audio_playback(self):
        if self.audio_data:
            self.audio_manager.play_audio(self.audio_data)

        else:
            print("No audio loaded to play")
    
    def start_camera_feed(self):
        my_own_calc.start_tracking()

    def process_gestures_thread(self):
        """Run gesture processing in a separate thread to avoid blocking the GUI."""
        
        threading.Thread(target=self.process_gestures, daemon=True).start()


    def process_gestures(self):
        #Check for gesture changes in the loop
        while True:
            self.gesture_manager.process_gestures()
            time.sleep(0.1)
            

    def update_volume_label(self, effect_value):
        """Update the volume label."""
        self.volume_label.config(text=f"Volume: {effect_value:.2f}")

    def update_pitch_label(self, effect_value):
        """Update the pitch label."""
        self.pitch_label.config(text=f"Pitch: {effect_value:.2f}")

    def update_speed_label(self, effect_value):
        """Update the speed label."""
        self.speed_label.config(text=f"Speed: {effect_value:.2f}")

    def on_closing(self):
        if self.audio_manager:
            self.audio_manager.stop_audio()
        self.root.destroy()