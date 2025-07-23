import os
import yt_dlp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import mainthread

SONGS_DIR = "songs"

if not os.path.exists(SONGS_DIR):
    os.makedirs(SONGS_DIR)

class Downloader(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.input = TextInput(hint_text='Enter YouTube title or URL', multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.input)
        self.button = Button(text='Download as MP3', size_hint_y=None, height=40)
        self.button.bind(on_press=self.download)
        self.add_widget(self.button)
        self.status = Label(text='', size_hint_y=None, height=40)
        self.add_widget(self.status)

    def set_status(self, msg):
        self.status.text = msg

    def download(self, instance):
        query = self.input.text.strip()
        if not query:
            self.set_status('Please enter a title or URL.')
            return
        self.set_status('Downloading...')
        from threading import Thread
        Thread(target=self._download_thread, args=(query,)).start()

    def _download_thread(self, query):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(SONGS_DIR, '%(title)s_%(id)s.%(ext)s'),
            'quiet': True,
            'noplaylist': True,
            'default_search': 'ytsearch',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=True)
                filename = ydl.prepare_filename(info)
                mp3_path = os.path.splitext(filename)[0] + ".mp3"
                self._set_status_mainthread(f"Downloaded: {os.path.basename(mp3_path)}")
        except Exception as e:
            self._set_status_mainthread(f"Download error: {e}")

    @mainthread
    def _set_status_mainthread(self, msg):
        self.set_status(msg)

class YT2MP3App(App):
    def build(self):
        Window.size = (400, 180)
        Window.title = "YouTube to MP3 Downloader"
        return Downloader()

if __name__ == '__main__':
    YT2MP3App().run()
