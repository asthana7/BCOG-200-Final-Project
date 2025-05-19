# # src/GUI/camera_feed_handler.py
# import cv2
# from PIL import Image, ImageTk
# import threading
# import time

# class CameraFeed:
#     def __init__(self, video_label):
#         self.video_label = video_label
#         self.running = False
#         self.cap = cv2.VideoCapture(0)

#     def start(self):
#         if not self.running:
#             self.running = True
#             threading.Thread(target=self.update_frame, daemon=True).start()

#     def stop(self):
#         self.running = False
#         if self.cap.isOpened():
#             self.cap.release()

#     def update_frame(self):
#         while self.running:
#             ret, frame = self.cap.read()
#             if ret:
#                 # Flip + convert to RGB
#                 frame = cv2.flip(frame, 1)
#                 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 img = Image.fromarray(frame)
#                 imgtk = ImageTk.PhotoImage(image=img)

#                 self.video_label.imgtk = imgtk
#                 self.video_label.configure(image=imgtk)

#             time.sleep(0.03)  # ~30 FPS

import cv2
from PIL import Image, ImageTk

class CameraFeed:
    def __init__(self, video_label, app_logic=None):
        self.video_label = video_label
        self.app_logic = app_logic
        self.cap = cv2.VideoCapture(0)
        self.running = False

    def start(self):
        self.running = True
        self.update_frame()

    def stop(self):
        self.running = False
        if self.cap and self.cap.isOpened():
            self.cap.release()

    def update_frame(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)

            if self.app_logic:
                frame = self.app_logic.process_frame(frame)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        # Schedule the next frame update (approx 30 FPS)
        self.video_label.after(33, self.update_frame)
