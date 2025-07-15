MDScreen:
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "🎧 KyaNaDeApp"
            elevation: 4
            md_bg_color: app.theme_cls.primary_color

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: 20
                spacing: 20

                MDLabel:
                    id: mode_label
                    text: "Mode: Offline"
                    halign: "center"
                    theme_text_color: "Primary"
                    font_style: "H6"

                MDRaisedButton:
                    text: "🔁 Ganti Mode"
                    on_release: app.switch_mode()
                    pos_hint: {"center_x": 0.5}

                MDBoxLayout:
                    id: offline_controls
                    orientation: "vertical"
                    spacing: 10
                    adaptive_height: True

                    MDRaisedButton:
                        text: "▶️ Putar Lagu Offline"
                        on_release: app.play_sample_song()
                        pos_hint: {"center_x": 0.5}

                MDBoxLayout:
                    id: online_controls
                    orientation: "vertical"
                    spacing: 10
                    adaptive_height: True
                    opacity: 0
                    disabled: True

                    MDTextField:
                        id: search_input
                        hint_text: "Masukkan URL atau Judul YouTube"

                    MDRaisedButton:
                        text: "🔍 Cari & Putar"
                        on_release: app.search_and_play_online(search_input.text)
                        pos_hint: {"center_x": 0.5}

                    MDRaisedButton:
                        id: pause_resume_button
                        text: "Pause"
                        on_release: app.toggle_pause_resume()
                        pos_hint: {"center_x": 0.5}

                    MDRaisedButton:
                        text: "⏹️ Stop"
                        on_release: app.stop_online()
                        pos_hint: {"center_x": 0.5}

                MDLabel:
                    id: current_song_label
                    text: "Lagu yang sedang diputar akan tampil di sini"
                    halign: "center"
                    theme_text_color: "Secondary"
                    font_style: "Body1"

                MDLabel:
                    id: status_label
                    text: "Status pemutaran"
                    halign: "center"
                    theme_text_color: "Secondary"
                    font_style: "Body2"
