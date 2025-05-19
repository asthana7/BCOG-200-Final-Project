import tkinter as tk
import os

class LoginScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.pack(expand=True)

        tk.Label(self, text="Please Select A Song", font=("Helvetica", 20), bg="#f0f0f0").pack(pady=20)

        audio_folder = os.path.join("audios")
        for filename in os.listdir(audio_folder):
            if filename.endswith(".mp3"):
                full_path = os.path.join(audio_folder, filename)
                tk.Button(self, text=filename, command=lambda path=full_path: self.select_song(path)).pack(pady=5)

    def select_song(self, path):
        print(f"[LoginScreen] Selected song: {path}")
        self.controller.selected_song_path = path
        self.controller.show_main_screen()

