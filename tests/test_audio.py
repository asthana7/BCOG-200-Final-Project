import pytest
from src.audio_manipulation import AudioManager

def test_audio_loads():
    manager = AudioManager()
    data, sr = manager.load_audio_file("audios/chaos_agent.mp3")
    assert data is not None
    assert sr > 0

def test_pitch_change():
    manager = AudioManager()
    manager.set_pitch(2.5)
    assert manager.pitch_factor == 2.5

def test_volume_range():
    manager = AudioManager()
    manager.set_volume(100)
    assert 0.0 <= manager.volume_factor <= 1.0
