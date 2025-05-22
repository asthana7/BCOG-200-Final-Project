import pytest
from src.audio_manipulation import AudioManager

@pytest.fixture
def audio_manager():
    manager = AudioManager()
    manager.song_paths = [
        "audios/chaos_agent.mp3",
        "audios/song2.mp3",
        "audios/song3.mp3",
        "audios/song4.mp3",
        "audios/song5.mp3",
    ]
    manager.current_song_index = 0
    return manager

def test_audio_loads(audio_manager):
    data, sr = audio_manager.load_audio_file(audio_manager.song_paths[0])
    assert data is not None
    assert sr > 0

def test_clockwise_skips_to_next_song(audio_manager):
    initial_index = audio_manager.current_track_index
    audio_manager.skip_to_next()
    expected_index = (initial_index + 1) % len(audio_manager.track_list)
    assert audio_manager.current_track_index == expected_index

def test_volume_range(audio_manager):
    audio_manager.set_volume(100)
    assert 0.0 <= audio_manager.volume_factor <= 1.0

