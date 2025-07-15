import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit,
    QFrame
)
from PySide6.QtGui import QMovie, QPixmap, QFont
from PySide6.QtCore import Qt, QSize

from player.online_player import OnlinePlayer
from search.youtube_search import search_youtube


class KyaNaDeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎧 KyaNaDeApp")
        self.setMinimumSize(600, 700)

        # 🔹 Container utama
        container = QWidget(self)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(container)

        # 🔹 Layout utama
        self.bg_label = QLabel(container)
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, 600, 700)
        movie = QMovie("assets/bg_anim.gif")
        self.bg_label.setMovie(movie)
        movie.start()

        # 🔹 Frame UI
        self.ui_frame = QFrame(container)
        self.ui_frame.setStyleSheet("background: rgba(255, 255, 255, 0.85); border-radius: 10px;")
        self.ui_frame.setGeometry(20, 20, 560, 660)

        foreground_layout = QVBoxLayout(self.ui_frame)
        foreground_layout.setAlignment(Qt.AlignTop)
        foreground_layout.setSpacing(10)

        # 🔸 Logo
        logo = QLabel()
        pixmap = QPixmap("assets/logo_overlay.jpg")
        logo.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo.setAlignment(Qt.AlignCenter)
        foreground_layout.addWidget(logo)

        # 🔸 Title
        title = QLabel("🎧 KyaNaDeApp")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 18, QFont.Bold))
        foreground_layout.addWidget(title)

        # 🔁 Mode
        self.mode = "Offline"
        self.mode_label = QLabel("Mode: Offline")
        self.mode_label.setAlignment(Qt.AlignCenter)
        foreground_layout.addWidget(self.mode_label)

        self.switch_button = QPushButton("🔁 Ganti Mode")
        self.switch_button.clicked.connect(self.switch_mode)
        foreground_layout.addWidget(self.switch_button)

        # ▶️ Offline only
        self.offline_play_button = QPushButton("▶️ Putar Lagu Offline")
        self.offline_play_button.clicked.connect(self.play_sample_song)
        foreground_layout.addWidget(self.offline_play_button)

        # 🔎 Online only
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Masukkan URL atau Judul YouTube")
        self.search_button = QPushButton("🔍 Cari & Putar")
        self.search_button.clicked.connect(self.search_and_play_online)
        self.pause_resume_button = QPushButton("Pause")
        self.pause_resume_button.clicked.connect(self.toggle_pause_resume)
        self.stop_button = QPushButton("⏹️ Stop")
        self.stop_button.clicked.connect(self.stop_online)

        # Online control list
        self.online_controls = [
            self.search_input, self.search_button,
            self.pause_resume_button, self.stop_button
        ]
        for widget in self.online_controls:
            widget.setVisible(False)
            foreground_layout.addWidget(widget)

        # Status
        self.current_song_label = QLabel("Lagu yang sedang diputar akan tampil di sini")
        self.current_song_label.setAlignment(Qt.AlignCenter)
        foreground_layout.addWidget(self.current_song_label)

        self.status_label = QLabel("Status pemutaran")
        self.status_label.setAlignment(Qt.AlignCenter)
        foreground_layout.addWidget(self.status_label)

        self.online_player = OnlinePlayer()

        # 🔁 Resize background & frame
        self.resizeEvent = self.on_resize

    def on_resize(self, event):
        size = event.size()
        self.bg_label.resize(size)
        self.ui_frame.setGeometry(20, 20, size.width() - 40, size.height() - 40)

    def switch_mode(self):
        if self.mode == "Offline":
            self.mode = "Online"
            self.mode_label.setText("Mode: Online")
            self.offline_play_button.setVisible(False)
            for widget in self.online_controls:
                widget.setVisible(True)
        else:
            self.mode = "Offline"
            self.mode_label.setText("Mode: Offline")
            self.offline_play_button.setVisible(True)
            for widget in self.online_controls:
                widget.setVisible(False)

    def play_sample_song(self):
        from kivy.core.audio import SoundLoader
        path = os.path.join("songs", "lagu1.mp3")
        if os.path.exists(path):
            sound = SoundLoader.load(path)
            if sound:
                sound.play()
                self.status_label.setText("Memutar lagu offline: lagu1.mp3")
                self.current_song_label.setText("🎵 lagu1.mp3 (Offline)")
        else:
            self.status_label.setText("Lagu tidak ditemukan.")

    def search_and_play_online(self):
        query = self.search_input.text()
        if not query.strip():
            self.status_label.setText("Masukkan URL atau Judul YouTube terlebih dahulu!")
            return

        def update_status(status):
            print(status)
            self.status_label.setText(status)
            self.current_song_label.setText(status)
            self.pause_resume_button.setText("Pause")

        print(f"🔎 Mencoba memutar: {query}")
        self.online_player.play(query, callback=update_status)

    def stop_online(self):
        self.online_player.stop()
        self.status_label.setText("Pemutaran dihentikan.")
        self.current_song_label.setText("")

    def toggle_pause_resume(self):
        if self.online_player.player:
            self.online_player.pause_resume()
            is_playing = self.online_player.is_playing()
            self.pause_resume_button.setText("Pause" if is_playing else "Resume")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KyaNaDeApp()
    window.show()
    sys.exit(app.exec())
