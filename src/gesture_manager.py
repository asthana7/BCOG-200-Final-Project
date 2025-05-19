import numpy as np
from src.hand_model import my_own_calc

def map_distance_to_effect(distance, min_d, max_d, min_val, max_val):
    
    #normalize distance between [min_d, max_d] to [min_val, max_val].
    
    distance = max(min_d, min(distance, max_d))  
    return min_val + (max_val - min_val) * ((distance - min_d) / (max_d - min_d))

class GestureManager:
    def __init__(self, audio_manager, volume_threshold=0.01, pitch_threshold=0.01, speed_threshold=0.01):
        self.audio_manager = audio_manager

        self.prev_d_volume = 0.0
        self.prev_d_pitch = 0.0
        self.prev_d_speed = 0.0

        self.smoothed_pitch = 0.0
        self.smoothed_speed = 1.0
        self.smoothing_alpha = 0.3
        
        self.baseline_pitch = None
        self.baseline_speed = None

        self.volume_threshold = volume_threshold
        self.pitch_threshold = pitch_threshold
        self.speed_threshold = speed_threshold

    def process_gestures(self):
        if not my_own_calc.hands_detected():
            if self.hand_present:
                print("No hands detected, resetting audio to neural")
                self.audio_manager.set_pitch(0.0)
                self.audio_manager.set_speed(1.0)
                self.hand_present = False
            return
        
        self.hand_present = True
        
        d_volume = my_own_calc.ii_distance()
        d_pitch  = my_own_calc.rdistance()
        d_speed  = my_own_calc.ldistance()

        if self.baseline_pitch is None:
            self.baseline_pitch = d_pitch
            print(f"[INIT] Baseline pitch set to {self.baseline_pitch:.2f}")
        
        if self.baseline_speed is None:
            self.baseline_speed = d_speed
            print(f"[INIT] Baseline speed set to {self.baseline_speed:.2f}")
        
        delta_volume = abs(d_volume - self.prev_d_volume)
        delta_pitch  = abs(d_pitch - self.prev_d_pitch)
        delta_speed  = abs(d_speed - self.prev_d_speed)

        #volume
        if delta_volume > self.volume_threshold:
            self.audio_manager.set_volume(d_volume)
            print(f"[VOLUME] Distance: {d_volume:.2f} → Volume Factor: {self.audio_manager.volume_factor:.2f}")
            self.prev_d_volume = d_volume

        #pitch
        if delta_pitch > self.pitch_threshold:
            target_pitch = np.interp(d_pitch - self.baseline_pitch, [10,550],[-6,6])
            self.smoothed_pitch = (self.smoothing_alpha * target_pitch + (1 - self.smoothing_alpha)*self.smoothed_pitch)
            self.audio_manager.set_pitch(self.smoothed_pitch)
            
            print(f"[PITCH] Raw: {target_pitch:.2f} → Smoothed: {self.smoothed_pitch:.2f}")
            self.prev_d_pitch = d_pitch

        #speed 
        if delta_speed > self.speed_threshold:
            target_speed = np.interp(d_speed - self.baseline_speed, [10, 550], [0.5, 2.0])
            self.smoothed_speed = (self.smoothing_alpha * target_speed + (1 - self.smoothing_alpha)*self.smoothed_speed)
            self.audio_manager.set_speed(self.smoothed_speed)
            print(f"[SPEED] Raw: {target_speed:.2f} → Speed Ratio: {self.smoothed_speed:.2f}")
            self.prev_d_speed = d_speed


