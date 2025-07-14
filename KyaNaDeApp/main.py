from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.audio import SoundLoader
import os

from player.online_player import OnlinePlayer
from search.youtube_search import search_youtube

class MainApp(MDApp):
    def build(self):
        root = Builder.load_file("ui/main.kv")

        # Inisialisasi pemutar YouTube
        self.online_player = OnlinePlayer()

        # Sembunyikan kontrol online di awal
        root.ids.online_controls.opacity = 0
        root.ids.online_controls.disabled = True
        return root

    def switch_mode(self):
        current_mode = self.root.ids.mode_label.text
        offline_controls = self.root.ids.offline_controls
        online_controls = self.root.ids.online_controls

        if "Offline" in current_mode:
            self.root.ids.mode_label.text = "Mode: Online"
            offline_controls.opacity = 0
            offline_controls.disabled = True
            online_controls.opacity = 1
            online_controls.disabled = False
        else:
            self.root.ids.mode_label.text = "Mode: Offline"
            offline_controls.opacity = 1
            offline_controls.disabled = False
            online_controls.opacity = 0
            online_controls.disabled = True

    def play_sample_song(self):
        path = os.path.join("songs", "lagu1.mp3")
        if os.path.exists(path):
            sound = SoundLoader.load(path)
            if sound:
                sound.play()
        else:
            print("File tidak ditemukan:", path)

    def search_and_play_online(self, query):
        if not query.strip():
            print("Masukkan URL atau Judul YouTube terlebih dahulu!")
            return

        def update_status(status):
            print(status)
            self.root.ids.status_label.text = status
            self.root.ids.current_song_label.text = status
            self.root.ids.pause_resume_button.text = "Pause"  # reset button setiap ganti lagu

        print(f"🔎 Mencoba memutar: {query}")
        self.online_player.play(query, callback=update_status)

    def stop_online(self):
        self.online_player.stop()

    def toggle_pause_resume(self):
        if self.online_player.player:
            self.online_player.pause_resume()
            is_playing = self.online_player.is_playing()
            self.root.ids.pause_resume_button.text = "Pause" if is_playing else "Resume"


if __name__ == "__main__":
    MainApp().run()
