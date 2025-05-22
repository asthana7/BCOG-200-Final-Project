import sounddevice as sd
import numpy as np
import librosa
import threading
import queue
import time
from src.hand_model import my_own_calc

from src.hand_model.app import get_gesture_label

class AudioManager:
    def __init__(self):
        self.audio_data = None
        self.sr = None
        self.frame_index = 0
        self.block_size = 8192

        self.pitch_factor = 0.0
        self.speed_factor = 1.0
        self.volume_factor = 1.0

        self.last_gesture_time = 0
        self.track_list = [
            "audios/between_the_lines.mp3",
            "audios/calm_the_f_down.mp3",
            "audios/chaos_agent.mp3",
            "audios/garage_fuzz.mp3",
            "audios/shake_that_rump.mp3",
        ]
        self.current_track_index = 0
        #gesture_type = get_gesture_label()

        self.stream = None
        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()
        self.lock = threading.Lock()

    def load_audio_file(self, path):
        self.audio_data, self.sr = librosa.load(path, sr=None, mono=True)
        self.frame_index = 0
        print(f"Audio file loaded: {path}")
        return self.audio_data, self.sr

    def start_stream(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
        self.stream = sd.OutputStream(
            samplerate=self.sr,
            channels=1,
            dtype='float32',
            callback=self.audio_callback,
            blocksize=self.block_size
        )
        self.stream.start()
        print("Audio stream started")

    def skip_to_next(self):
        self.current_track_index = (self.current_track_index + 1) % len(self.track_list)
        path = self.track_list[self.current_track_index]
        self.stop_audio()
        self.load_audio_file(path)
        self.start_stream()
        print(f"[Audio Manager] playing {path}")

    def skip_to_previous(self):
        self.current_track_index = (self.current_track_index - 1) % len(self.track_list)
        path = self.track_list[self.current_track_index]
        self.stop_audio()
        self.load_audio_file(path)
        self.start_stream()

        print(f"[Audio Manager] playing {path}")

    def handle_gesture(self):
        gesture_type = get_gesture_label()
        now = time.time()
        if now - self.last_gesture_time < 3:
            return
        if gesture_type == "Clockwise" or gesture_type == "next":
            print("skipping to next song in list")
            self.skip_to_next()
            self.last_gesture_time = now
        elif gesture_type == "Counter Clockwise" or gesture_type == "previous":
            print("skipping to previous song in list")
            self.skip_to_previous()
            self.last_gesture_time = now
        



    def audio_callback(self, outdata, frames, time, status):
        gesture = get_gesture_label()
        print(gesture)
        self.handle_gesture()
        if status:
            print("Stream status:", status)

        start = self.frame_index
        end = start + frames
        if end >= len(self.audio_data):
            self.frame_index = 0
            start = 0
            end = frames

        chunk = self.audio_data[start:end]
        self.frame_index += frames

        #jand check
        hands_up = my_own_calc.hands_detected()

        #feed buffer only if gesture is active
        if hands_up and self.input_queue.qsize() < 10:
            self.input_queue.put(chunk.copy())

        #try using processed output if available
        try:
            processed = self.output_queue.get(timeout = 0.02)
            chunk = processed
            
        except queue.Empty:
            print("[AUDIO_CALLBACK] Using raw chunk fallback")

        #volume always applied
        chunk *= self.volume_factor
        if not np.isfinite(chunk).all():
            chunk = np.zeros(frames, dtype=np.float32)

        try:
            outdata[:] = chunk.reshape(-1, 1)
            
        except Exception as e:
            
            outdata[:] = np.zeros((frames, 1), dtype=np.float32)


    def stop_audio(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.stream = None
            print("Audio stream stopped")

    def set_pitch(self, n_steps):
        print(f"[AUDIO_MANAGER] Setting pitch to {n_steps}")
        self.pitch_factor = n_steps

    def set_speed(self, speed_ratio):
        print(f"[AUDIO_MANAGER] Setting speed to {speed_ratio}")
        self.speed_factor = speed_ratio

    def set_volume(self, gesture_distance):
        self.volume_factor = np.clip(np.interp(gesture_distance, [30, 300], [0.0, 1.0]), 0.0, 1.0)

    def reset_audio(self):
        self.set_pitch(0.0)
        self.set_speed(1.0)
        self.volume_factor = 1.0
        print("Audio reset to neutral")


#what was actually supposed to be this project: also control frequency+speed but i couldnt get it up to real-time standards
# import sounddevice as sd
# import numpy as np
# import librosa
# import soundfile as sf
# from src.hand_model import my_own_calc

# class AudioManager:
#     def __init__(self):
#         self.audio_data = None
#         self.sr = None
#         self.pitch_factor = 0.0  #in semitones (smallest interval used in classicial Western music)
#         self.speed_factor = 1.0  
#         self.volume_factor = 1.0 #(0, 1)
#         self.stream = None
#         self.frame_index = 0
#         self.block_size = 8192
#         self.last_chunk = np.zeros(4410, dtype = np.float32)
#         self.effect_buffer = np.zeros(0, dtype = np.float32)
#         self.buffer_threshold = 11025 #1 second approx
#         self.processed_buffer = np.zeros(0, dtype = np.float32)
#         self.effect_process_cooldown = 0

#     def load_audio_file(self, path):
#         self.audio_data, self.sr = librosa.load(path, sr=None, mono=True)
#         self.frame_index = 0
#         print(f"Audio file loaded: {path}")
#         return self.audio_data, self.sr

#     def start_stream(self):
#         if self.stream:
#             self.stream.stop()
#             self.stream.close()

#         self.stream = sd.OutputStream(
#             samplerate=self.sr,
#             channels=1,
#             dtype='float32',
#             callback=self.audio_callback,
#             blocksize=self.block_size
#         )
#         self.stream.start()
#         print("Audio stream started")

#     def stop_audio(self):
#         if self.stream:
#             self.stream.stop()
#             self.stream.close()
#             self.stream = None
#             print("Audio stream stopped")



# #AUDIO DOESNT STOP
#     def audio_callback(self, outdata, frames, time, status):
#         if status:
#             print("Stream status:", status)

#         #get raw chunk
#         start = self.frame_index
#         end = start + frames
#         if end >= len(self.audio_data):
#             self.frame_index = 0
#             start = 0
#             end = frames

#         raw_chunk = self.audio_data[start:end]
#         self.frame_index += frames

#         if raw_chunk.size == 0:
#             raw_chunk = np.zeros(frames, dtype=np.float32)

#         #detect ahnds
#         self.hand_present = my_own_calc.hands_detected()

#         #build buffer
#         if self.hand_present:
#             self.effect_buffer = np.concatenate((self.effect_buffer, raw_chunk))
#             print(f"[DEBUG] effect_buffer size: {len(self.effect_buffer)}")

#         #process effects when ready
#         if self.hand_present and len(self.effect_buffer) >= self.buffer_threshold:
#             try:
#                 temp = self.effect_buffer[:self.buffer_threshold]
#                 self.effect_buffer = self.effect_buffer[self.buffer_threshold:]

#                 effects_applied = False

#                 if abs(self.pitch_factor) > 0.1:
#                     temp = librosa.effects.pitch_shift(temp, sr=self.sr, n_steps=self.pitch_factor)
#                     effects_applied = True
#                     print("[SUCCESS] Pitch shift applied")

#                 if abs(self.speed_factor - 1.0) > 0.05:
#                     if len(temp) < 2048:
#                         temp = np.pad(temp, (0, 2048 - len(temp)), mode='reflect')
#                     temp = librosa.effects.time_stretch(temp, rate=self.speed_factor)
#                     effects_applied = True
#                     print("[SUCCESS] Time stretch applied")

#                 if effects_applied:
#                     self.processed_buffer = np.concatenate((self.processed_buffer, temp))
#                     print("[DEBUG] Added to processed buffer")

#             except Exception as e:
#                 print("[ERROR] Effect processing failed:", e)

#         # === OUTPUT LOGIC — 3-WAY (sacred structure) ===
#         if len(self.processed_buffer) >= frames:
#             chunk = self.processed_buffer[:frames]
#             self.processed_buffer = self.processed_buffer[frames:]
#             print("[AUDIO_CALLBACK] Using processed buffer")

#         elif self.hand_present and len(self.effect_buffer) >= frames:
#             chunk = self.effect_buffer[:frames]
#             self.effect_buffer = self.effect_buffer[frames:]
#             print("[AUDIO_CALLBACK] Using effect buffer")

#         else:
#             chunk = raw_chunk
#             print("[AUDIO_CALLBACK] Using raw chunk fallback")

#         # === FINAL SAFETY + VOLUME ===
#         if len(chunk) < frames:
#             chunk = np.pad(chunk, (0, frames - len(chunk)), mode='edge')

#         chunk *= self.volume_factor

#         if not np.isfinite(chunk).all():
#             print("[WARNING] Non-finite chunk — zeroing")
#             chunk = np.zeros(frames, dtype=np.float32)

#         try:
#             outdata[:] = chunk.reshape(-1, 1)
#         except Exception as e:
#             print("[ERROR] Reshape failed:", e)
#             outdata[:] = np.zeros((frames, 1), dtype=np.float32)

    
            
        
#     def set_pitch(self, n_steps):
#         print(f"[AUDIO_MANAGER] Setting pitch to {n_steps}")
#         self.pitch_factor = n_steps

#     def set_speed(self, speed_ratio):
#         self.speed_factor = speed_ratio

#     def set_volume(self, gesture_distance):
        
#         self.volume_factor = np.clip(np.interp(gesture_distance, [30, 300], [0.0, 1.0]), 0.0, 1.0)

#     def reset_audio(self):
#         self.set_pitch(0.0)
#         self.set_speed(1.0)
#         self.volume_factor = 1.0
#         print("audio reset to neutral")