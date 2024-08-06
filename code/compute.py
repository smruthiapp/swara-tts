import os
from pydub import AudioSegment
from datetime import timedelta
from tqdm import tqdm

# Path to the directory containing the audio files
directory = "./HolyGitaAudio"

# Initialize total duration
total_duration = 0

# Get the total number of audio files
num_files = len([filename for filename in os.listdir(directory) if filename.endswith((".mp3", ".wav"))])

# Iterate over all files in the directory
for filename in tqdm(os.listdir(directory), total=num_files, desc="Processing audio files"):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        # Load the audio file
        audio = AudioSegment.from_file(os.path.join(directory, filename))
        
        # Add the duration of the audio file to the total duration
        total_duration += len(audio)

# Convert the total duration to timedelta object
duration = timedelta(milliseconds=total_duration)

# Print the total duration in hr:min:sec format
print("Total duration:", str(duration)) # 5:07:57
