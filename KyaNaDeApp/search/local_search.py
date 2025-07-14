import os

def list_local_songs(directory="songs"):
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if f.endswith(".mp3")]
