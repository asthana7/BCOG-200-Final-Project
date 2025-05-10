# src/gesture_manager.py
import numpy as np
from src.hand_model import my_own_calc
from src.audio_manipulation import volume, frequency, speed  # Your existing functions

def map_distance_to_effect(distance, min_d, max_d, min_val, max_val):
    """
    Normalize distance between [min_d, max_d] to [min_val, max_val].
    """
    distance = max(min_d, min(distance, max_d))  # clamp
    return min_val + (max_val - min_val) * ((distance - min_d) / (max_d - min_d))

class GestureManager:
    def __init__(self, volume_threshold=0.01, pitch_threshold=0.01, speed_threshold=0.01):
        self.prev_d_volume = 0.0
        self.prev_d_pitch = 0.0
        self.prev_d_speed = 0.0

        self.volume_threshold = volume_threshold
        self.pitch_threshold = pitch_threshold
        self.speed_threshold = speed_threshold

    def process_gestures(self):
        
        d_volume = my_own_calc.ii_distance()
        d_pitch  = my_own_calc.rdistance()
        d_speed  = my_own_calc.ldistance()

        delta_volume = abs(d_volume - self.prev_d_volume)
        delta_pitch  = abs(d_pitch - self.prev_d_pitch)
        delta_speed  = abs(d_speed - self.prev_d_speed)

        if delta_volume > self.volume_threshold or delta_pitch > self.pitch_threshold or delta_speed > self.speed_threshold:
            if delta_volume > delta_pitch and delta_volume > delta_speed:
                self._handle_volume_change(d_volume)
            elif delta_pitch > delta_speed:
                self._handle_pitch_change(d_pitch)
            else:
                self._handle_speed_change(d_speed)

        self.prev_d_volume = d_volume
        self.prev_d_pitch = d_pitch
        self.prev_d_speed = d_speed

    def _handle_volume_change(self, d_volume):
        print(f"Volume distance: {d_volume:.3f}")
        new_volume = map_distance_to_effect(d_volume, 0.02, 0.3, 0.0, 1.0)
        volume(new_volume)

    def _handle_pitch_change(self, d_pitch):
        print(f"Pitch distance: {d_pitch:.3f}")
        new_pitch = map_distance_to_effect(d_pitch, 0.01, 0.25, 0.8, 1.25)
        frequency(new_pitch)

    def _handle_speed_change(self, d_speed):
        print(f"Speed distance: {d_speed:.3f}")
        new_speed = map_distance_to_effect(d_speed, 0.01, 0.25, 0.5, 1.5)
        speed(new_speed)

