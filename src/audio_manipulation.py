# import os
# from pydub import AudioSegment
# from pydub.playback import play
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# import numpy as np
# import time
# import librosa
# import sounddevice as sd

# path = None #needs to be imported or something


# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None
# )
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# vol_range = volume.GetVolumeRange()

# min_vol = vol_range[0]
# max_vol = vol_range[1]



# def load_audio_file(path):
#     if path is None or not os.path.exists(path):
#           raise ValueError("No Valid file path provided.")

#     audio_data, sr = librosa.load(path, sr=None)
#     return audio_data, sr

# def volume(i_i_distance):
#     #volume toggle
#         #hand range: 10 to 900
#         #volume range -65 to 0
#         vol = np.interp(i_i_distance,[10, 550], [min_vol, max_vol])
#         #print(vol)
#         volume.SetMasterVolumeLevel(vol, None)

# def frequency(r_distance, audio_data, sr):
#     pitch_factor = r_distance #need to normalize it or whatever
#     librosa.effects.pitch_shift(audio_data, sr, n_steps=pitch_factor)


# # # Real-time audio callback function
# # def callback(indata, frames, time, status):
# #     # Shift pitch (without changing speed)
# #     pitch_factor = 2.0  # Increase pitch by 2 semitones
# #     shifted_audio = shift_pitch_librosa(indata[:, 0], 44100, pitch_factor)  # Only apply to the first channel (mono)
# #     sd.play(shifted_audio, 44100)

# # # Setup stream for real-time audio input/output
# # with sd.InputStream(callback=callback, channels=1, samplerate=44100):
# #     print("Press Ctrl+C to stop")
# #     while True:
# #         time.sleep(1)
# def speed(l_distance, audio_data, sr):
#     rate = l_distance #needs to be normalized
#     librosa.effects.time_stretch(audio_data, sr, rate = rate)
    
    
# # def apply_effect(audio: AudioSegment, effect_id: int) -> AudioSegment:
# #     if effect_id == 1:
# #         return audio.speedup(playback_speed=1.5)
# #     elif effect_id == 2:
# #         return audio._spawn(audio.raw_data, overrides={
# #             "frame_rate": int(audio.frame_rate * 0.75)
# #         }).set_frame_rate(audio.frame_rate)
# #     elif effect_id == 3:
# #         return audio._spawn(audio.raw_data, overrides={
# #             "frame_rate": int(audio.frame_rate * 1.25)
# #         }).set_frame_rate(audio.frame_rate)
# #     elif effect_id == 4:
# #         return audio._spawn(audio.raw_data, overrides={
# #             "frame_rate": int(audio.frame_rate * 0.8)
# #         }).set_frame_rate(audio.frame_rate)
# #     elif effect_id == 5:
# #         return audio.reverse()
# #     else:
# #         raise ValueError("Invalid effect ID")

# # def process_audio(audio_path, effect_id, output_name="modified_output.mp3"):
# #     audio = AudioSegment.from_mp3(audio_path)
# #     modified = apply_effect(audio, effect_id)
# #     print("Playing modified audio...")
# #     play(modified)
# #     output_path = os.path.join(os.path.dirname(audio_path), output_name)
# #     modified.export(output_path, format="mp3")
# #     print(f"Modified audio saved as: {output_path}")


# # from pydub import AudioSegment
# # from pydub.playback import play

# # # Load from disk
# # audio = AudioSegment.from_mp3("audio/song1.mp3")

# # # Apply transformation in memory
# # faster_audio = audio.speedup(playback_speed=1.5)

# # # Play directly (real-time)
# # play(faster_audio)
# def play_audio(audio: AudioSegment):
#      play(audio)


from pydub import AudioSegment
from pydub.playback import play
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import librosa
import numpy as np
import simpleaudio as sa


class AudioManager:
    def __init__(self):
        self.audio = None
        self.sr = None
        

    def load_audio_file(self, path):
        self.audio = AudioSegment.from_mp3(path)
        self.sr = 44100
        print(f"Audio file loaded: {path}")
        return self.audio, self.sr

    def play_audio(self, audio:AudioSegment):
        play_obj = sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate = audio.frame_rate)
        play_obj.wait_done()

    def volume(self, i_i_distance):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        vol_range = volume.GetVolumeRange()

        min_vol = vol_range[0]
        max_vol = vol_range[1]
        #volume toggle
        #hand range: 10 to 900
        #volume range -65 to 0
        vol = np.interp(i_i_distance,[10, 550], [min_vol, max_vol])
        #print(vol)
        volume.SetMasterVolumeLevel(vol, None)

    def frequency(r_distance, audio_data, sr):
        pitch_factor = r_distance #need to normalize it or whatever
        librosa.effects.pitch_shift(audio_data, sr, n_steps=pitch_factor)
            
    def speed(l_distance, audio_data, sr):
        rate = l_distance #needs to be normalized
        librosa.effects.time_stretch(audio_data, sr, rate = rate)