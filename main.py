import os
import yt_dlp as youtube_dl

def download_audio(url):
    youtube_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join('musics', '%(title)s.%(ext)s')
    }
    with youtube_dl.YoutubeDL(youtube_options) as ydl:
        ydl.download([url])
            
def main():
    with open(file='links.txt', mode='r', encoding='utf8') as data:
        line = data.readline()
        while line:
            line_url = line.strip()
            download_audio(line_url)
            line = data.readline()
    
main()