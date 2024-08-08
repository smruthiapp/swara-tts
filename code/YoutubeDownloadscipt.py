import os
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
            'extract_flat': True,  # Flatten the playlist and download all videos
        }

        if ffmpeg_location:
            ydl_opts['ffmpeg_location'] = ffmpeg_location

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print(f"Downloaded audio from: {video_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Dictionary of YouTube video URLs and corresponding directory names
video_urls = {
    'https://www.youtube.com/watch?v=tZxnilHN8EE&ab_channel=GaanasampadaDevotional': 'Dr. Vidyabhushana',
    'https://www.youtube.com/watch?v=E53GuZ8NFQw&ab_channel=BrajaBeats': 'ISCKON',
    'https://www.youtube.com/watch?v=WITUOwi3EYk': 'Udaya Shreyas',
    'https://www.youtube.com/watch?v=C5UHgA9C3kw': 'Kum. Aditi',
    'https://www.youtube.com/playlist?list=OLAK5uy_lOp1HGU8md9RbTmZfbR7Dc8LaBv-mAtug': 'Swami Paramarthananda',
    'https://www.youtube.com/watch?v=hHq14qUebOc': 'Radha Gopinath Prabhu',
}

# Path to ffmpeg (if needed)
ffmpeg_path = 'C:/ffmpeg/bin'  # Replace with the actual path if necessary

# Download audio for each video URL and save in the corresponding directory
for url, directory in video_urls.items():
    output_path = os.path.join('.', directory)
    os.makedirs(output_path, exist_ok=True)
    download_audio_from_youtube(url, output_path=output_path, ffmpeg_location=ffmpeg_path)
