import yt_dlp

def download_audio_from_youtube(video_url, output_path='.', ffmpeg_location=None):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        if ffmpeg_location:
            ydl_opts['ffmpeg_location'] = ffmpeg_location

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print(f"Downloaded audio from: {video_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

# List of YouTube video URLs
video_urls = [
    'https://www.youtube.com/watch?v=E53GuZ8NFQw&ab_channel=BrajaBeats',
    'https://www.youtube.com/watch?v=uip3DK9JVLU&ab_channel=ChinmayaChannel',
    'https://www.youtube.com/watch?v=tZxnilHN8EE&ab_channel=GaanasampadaDevotional',
    'https://www.youtube.com/watch?v=uYxt86Yk58w&ab_channel=Release-Topic',
    'https://www.youtube.com/watch?v=WITUOwi3EYk'
]

# Path to ffmpeg (if needed)
ffmpeg_path = 'C:/ffmpeg/bin'  # Replace with the actual path if necessary

# Download audio for each video URL
for url in video_urls:
    download_audio_from_youtube(url, ffmpeg_location=ffmpeg_path)
