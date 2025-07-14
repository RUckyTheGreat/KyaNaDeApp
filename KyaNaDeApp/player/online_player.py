import yt_dlp
from ffpyplayer.player import MediaPlayer
import threading

class OnlinePlayer:
    def __init__(self):
        self.player = None
        self.current_title = ""
        self.current_channel = ""
        self._paused = False

    def play(self, query, callback=None):
        if self.player:
            self.stop()

        def _play_audio():
            info = self._extract_info(query)
            if not info:
                if callback:
                    callback("❌ Gagal mendapatkan info video.")
                return

            if "formats" not in info:
                if callback:
                    callback("❌ Data format audio tidak ditemukan.")
                print("DEBUG INFO (No formats):", info)
                return

            stream_url = self._get_best_audio_url(info["formats"])
            if not stream_url:
                if callback:
                    callback("❌ Tidak ditemukan URL audio yang bisa diputar.")
                return

            title = info.get("title", "Tanpa Judul")
            channel = info.get("channel", "Tanpa Channel")
            self.current_title = title
            self.current_channel = channel

            if callback:
                callback(f"▶️ {title} - {channel}")

            print(f"▶️ Streaming dari: {stream_url}")
            self.player = MediaPlayer(stream_url)
            self._paused = False

            while True:
                frame, val = self.player.get_frame()
                if val == "eof" or self.player.get_pause():
                    break

        threading.Thread(target=_play_audio, daemon=True).start()

    def stop(self):
        if self.player:
            self.player.close_player()
            self.player = None
            self._paused = False

    def pause_resume(self):
        if self.player:
            self._paused = not self._paused
            self.player.set_pause(self._paused)

    def is_playing(self):
        return self.player is not None and not self._paused

    def get_current_info(self):
        return f"{self.current_title} - {self.current_channel}" if self.current_title else "❌ Tidak ada lagu aktif"

    def __init__(self):
        self.player = None

    def play(self, query, callback=None):
        if self.player:
            self.stop()

        def _play_audio():
            info = self._extract_info(query)
            if not info:
                if callback:
                    callback("❌ Gagal mendapatkan info video.")
                return

            if "formats" not in info:
                if callback:
                    callback("❌ Data format audio tidak ditemukan.")
                print("DEBUG INFO (No formats):", info)
                return

            stream_url = self._get_best_audio_url(info["formats"])
            if not stream_url:
                if callback:
                    callback("❌ Tidak ditemukan URL audio yang bisa diputar.")
                return

            title = info.get("title", "Tanpa Judul")
            channel = info.get("channel", "Tanpa Channel")
            if callback:
                callback(f"▶️ {title} - {channel}")

            print(f"▶️ Streaming dari: {stream_url}")
            self.player = MediaPlayer(stream_url)

            while True:
                frame, val = self.player.get_frame()
                if val == "eof" or self.player.get_pause():
                    break

        # Jalankan pemutaran di thread terpisah SAJA
        threading.Thread(target=_play_audio, daemon=True).start()

    def stop(self):
        if self.player:
            self.player.close_player()
            self.player = None

    def _extract_info(self, query):
        ytdl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True,
            'default_search': 'ytsearch1',
            'skip_download': True,
        }
        try:
            with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                if info.get('_type') == 'playlist' and 'entries' in info:
                    info = info['entries'][0]
                print(f"🎵 Dapat info: {info.get('title')} - {info.get('channel')}")
                return info
        except Exception as e:
            print("❌ Gagal mengambil info video:", e)
            return None

    def _get_best_audio_url(self, formats):
        for fmt in formats:
            if "m3u8" in fmt.get("url", ""):
                continue
            if fmt.get("acodec") != "none" and fmt.get("vcodec") == "none":
                return fmt["url"]
        return None
