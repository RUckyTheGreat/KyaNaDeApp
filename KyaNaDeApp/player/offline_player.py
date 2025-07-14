import os
from ffpyplayer.player import MediaPlayer

class OfflinePlayer:
    def __init__(self):
        self.player = None
        self.current_song = None

    def play(self, filepath):
        if not os.path.exists(filepath):
            print(f"❌ File not found: {filepath}")
            return
        if self.player:
            self.stop()
        self.player = MediaPlayer(filepath)
        self.current_song = filepath
        print(f"🎵 Playing: {os.path.basename(filepath)}")

    def stop(self):
        if self.player:
            self.player.close_player()
            self.player = None
            print("⏹️ Stopped playback.")
