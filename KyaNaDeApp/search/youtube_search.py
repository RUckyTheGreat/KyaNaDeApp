from yt_dlp import YoutubeDL

def search_youtube(query):
    options = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'default_search': 'ytsearch1',
    }

    with YoutubeDL(options) as ydl:
        try:
            result = ydl.extract_info(query, download=False)
            if 'entries' in result:
                return result['entries'][0]['url']
            return result['url']
        except Exception as e:
            print("Gagal mencari:", e)
            return None
