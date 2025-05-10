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

import os
from tkinter import filedialog, ttk, messagebox
import tkinter as tk
import librosa

class AudioGestureApp:
    def __init__(self, root):
        self.root = root
        self.audio_data == None
        self.sr = None
        self.original_audio_data = None
        self.song_path = None  # This will store the file path of the selected song
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Gesture-controlled Audio Manipulation")
        
        # Song selection frame
        self.song_frame = tk.Frame(self.root)
        self.song_frame.pack(pady=10)
        
        self.song_label = tk.Label(self.song_frame, text="No song selected", font=("Arial", 14))
        self.song_label.pack(pady=10)

        # "Select Song" Button
        self.select_button = tk.Button(self.song_frame, text="Select Song", command=self.select_audio_file)
        self.select_button.pack(pady=5)

        # Song list menu (this will show songs in your 'audio' folder)
        self.song_list_frame = tk.Frame(self.root)
        self.song_list_frame.pack(pady=10)

        self.song_menu_label = tk.Label(self.song_list_frame, text="Choose a song from list:", font=("Arial", 12))
        self.song_menu_label.pack(pady=10)

        # List songs in 'audio/' directory and show them
        self.show_song_menu()

        # Display some effect buttons (optional, depending on your app)
        self.effect_buttons_frame = tk.Frame(self.root)
        self.effect_buttons_frame.pack(pady=10)

        # Button to apply effect (just a placeholder for now)
        self.effect_button = tk.Button(self.effect_buttons_frame, text="Apply Effect", command=self.apply_effect)
        self.effect_button.pack(pady=10)

    def show_song_menu(self):
        # List all MP3 files in the 'audio' directory
        audio_dir = os.path.join(os.path.dirname(__file__), 'audio')
        mp3_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]

        if mp3_files:
            # Create a dropdown menu to select a song from the list
            self.song_menu = ttk.Combobox(self.song_list_frame, values=mp3_files)
            self.song_menu.pack(pady=10)

            # Set default value to the first song in the list
            self.song_menu.set(mp3_files[0])

            # "Load selected song" Button
            self.load_button = tk.Button(self.song_list_frame, text="Load Selected Song", command=self.load_selected_song)
            self.load_button.pack(pady=5)
        else:
            # Show a message if no MP3 files are found in the directory
            self.no_songs_label = tk.Label(self.song_list_frame, text="No songs available in the 'audio/' folder.", font=("Arial", 12))
            self.no_songs_label.pack(pady=10)

    def load_selected_song(self):
        song_name = self.song_menu.get()
        audio_dir = os.path.join(os.path.dirname(__file__), 'audio')
        self.song_path = os.path.join(audio_dir, song_name)
        self.audio_data, self.sr = self.load_audio_file(self.song_path)
        self.song_label.config(text=f"Selected song: {song_name}")
        # print(f"Song path: {self.song_path}")

        # # After loading the song, you can trigger any additional logic (like gesture manipulation)
        # self.apply_effect()  # Just for testing, we'll apply an effect right away

    # def select_audio_file(self):
    #     file_path = filedialog.askopenfilename(
    #         title="Select an MP3 file",
    #         filetypes=[("MP3 files", "*.mp3")]
    #     )
    #     if file_path:
    #         self.song_path = file_path
    #         song_name = os.path.basename(file_path)
    #         self.song_label.config(text=f"Selected song: {song_name}")
    #         print(f"Song path: {self.song_path}")

    #         # After selecting a file, you can trigger any additional logic (like gesture manipulation)
    #         self.apply_effect()  # Just for testing, we'll apply an effect right away
    #     else:
    #         print("No file selected.")

    def load_audio_file(self, path):
        audio_data, sr = librosa.load(path, sr = None)
        return audio_data, sr

    def apply_effect(self):
        # Placeholder for effect logic (e.g. changing volume, pitch, etc.)
        if self.song_path:
            print(f"Applying effect to: {self.song_path}")
        else:
            print("No song selected.")
