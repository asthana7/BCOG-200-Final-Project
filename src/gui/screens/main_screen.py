import tkinter as tk
import threading
import subprocess
import os
import pygetwindow as gw
import time

from src.audio_manipulation import AudioManager
from src.gesture_manager import GestureManager
from src.hand_model import my_own_calc


class MainScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.pack(expand=True, fill="both")

        tk.Label(self, text="Live Feed + Controls", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        song_label = tk.Label(self, text=f"Now Playing: {os.path.basename(controller.selected_song_path)}", font=("Helvetica", 14), bg="#f0f0f0")
        song_label.pack(pady=10)

        tk.Button(self, text="Back", command=self.controller.show_login_screen).pack(pady=20)

        self.audio_manager = AudioManager()
        self.audio_manager.load_audio_file(self.controller.selected_song_path)
        self.audio_manager.start_stream()

        self.gesture_manager = GestureManager(self.audio_manager)

        self.launch_app_py()
        self.start_hand_tracking()
        self.start_gesture_processing_thread()

    def launch_app_py(self):
        subprocess.Popen(["python", "src/hand_model/app.py"])
        #self.after(2000, self.reliably_position_mediapipe)
        threading.Thread(target = self.reliably_position_mediapipe, daemon = True).start()

    def reliably_position_mediapipe(self):
        def monitor_and_reposition():
            while True:
                try:
                    win = gw.getWindowsWithTitle("Hand Gesture Recognition")[0]
                    win.moveTo(0, 0)
                    win.activate()
                    time.sleep(1.5)  # Keep reapplying every second to override shift
                except IndexError:
                    pass
                time.sleep(1)
        threading.Thread(target=monitor_and_reposition, daemon=True).start()


    def start_hand_tracking(self):
        my_own_calc.start_tracking()

    def start_gesture_processing_thread(self):
        def gesture_loop():
            while True:
                self.gesture_manager.process_gestures()
        threading.Thread(target=gesture_loop, daemon=True).start()



