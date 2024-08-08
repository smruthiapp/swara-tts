from tqdm import tqdm
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the website


# Headers (modify as needed)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Create a directory to save the audio files
os.makedirs('resources/HolyGitaAudio', exist_ok=True)

# Function to download audio files
def download_audio(audio_url, filename):
    response = requests.get(audio_url, headers=headers)
    with open(filename, 'wb') as f:
        f.write(response.content)



# Find all audio tags and download the audio files


def getholygitaaudio (url,verse,chapter) :
    # Request the website content with headers
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')


    audio_urls = []
    for audio_tag in soup.find_all('audio'):
        audio_url = audio_tag.get('src')
        if audio_url:
            # Ensure the URL is complete
            audio_url = urljoin(url, audio_url)
            audio_urls.append(audio_url)
    for i, audio_url in enumerate(audio_urls, start=1):
        audio_filename = os.path.join('HolyGitaAudio', f'{chapter}-{verse}.mp3')
        download_audio(audio_url, audio_filename)





sutras = [47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78] 
for i in tqdm(range(0,len(sutras)),desc="chapters - ") :
    for j in range(0,sutras[i]) :
      
        getholygitaaudio(f'https://www.holy-bhagavad-gita.org/chapter/{i+1}/verse/{j+1}',j+1,i+1)

