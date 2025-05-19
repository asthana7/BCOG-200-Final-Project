import sounddevice as sd
import numpy as np
import librosa
import soundfile as sf

class AudioManager:
    def __init__(self):
        self.audio_data = None
        self.sr = None
        self.pitch_factor = 0.0  #in semitones (smallest interval used in classicial Western music)
        self.speed_factor = 1.0  
        self.volume_factor = 1.0 #(0, 1)
        self.stream = None
        self.frame_index = 0
        self.block_size = 8192
        self.last_chunk = np.zeros(4410, dtype = np.float32)
        self.effect_buffer = np.zeros(0, dtype = np.float32)
        self.buffer_threshold = 44100 #1 second approx
        self.processed_buffer = np.zeros(0, dtype = np.float32)

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

    def stop_audio(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.stream = None
            print("Audio stream stopped")

    def audio_callback(self, outdata, frames, time, status):
        if status:
            print("Stream status:", status)

        #get next raw chunk
        start = self.frame_index
        end = start + frames
        if end >= len(self.audio_data):
            self.frame_index = 0
            start = 0
            end = frames

        raw_chunk = self.audio_data[start:end]
        self.frame_index += frames

        #build up effect buffer
        self.effect_buffer = np.concatenate((self.effect_buffer, raw_chunk))

        #if enough buffer collected, apply pitch/speed
        if len(self.effect_buffer) >= self.buffer_threshold:
            try:
                temp = self.effect_buffer.copy()
                #success = True

                if self.pitch_factor != 0.0 and len(temp) >= 2048:
                    temp = librosa.effects.pitch_shift(temp, sr=self.sr, n_steps=self.pitch_factor)

                if self.speed_factor != 1.0 and len(temp) >= 2048:
                    temp = librosa.effects.time_stretch(temp, rate = self.speed_factor)
                if temp.size == 0:
                    raise ValueError("Processed buffer empty after effects")
                
                self.processed_buffer = np.concatenate((self.processed_buffer, temp))
                self.effect_buffer = np.zeros(0, dtype=np.float32)
            except Exception as e:
                print("Effect processing error:", e)
                # success = False
                # fallback = self.audio_data[start:end]
                # self.processed_buffer = np.concatenate((self.processed_buffer, fallback))

        #extract final output from processed buffer
        if len(self.processed_buffer) >= frames:
            chunk = self.processed_buffer[:frames]
            self.processed_buffer = self.processed_buffer[frames:]
        else:
            #not enough data — pad with zeros
            chunk = np.zeros(frames, dtype=np.float32)

        #applying volume
        chunk *= self.volume_factor
        if not np.isfinite(chunk).all():
            print("Non-finite values in chunk - zeroing out")
            chunk = np.zeros(frames, dtype = np.float32)
        # if chunk.size == 0:
        #     chunk = np.zeros(frames, dtype = np.float32)
        try:
            outdata[:] = chunk.reshape(-1, 1)
        except Exception as e:
            print("Reshape error", e)
            outdata[:] = np.zeros((frames, 1), dtype=np.float32)


    def set_pitch(self, n_steps):
        self.pitch_factor = n_steps

    def set_speed(self, speed_ratio):
        self.speed_factor = speed_ratio

    def set_volume(self, gesture_distance):
        self.volume_factor = np.clip(np.interp(gesture_distance, [30, 300], [0.0, 1.0]), 0.0, 1.0)
