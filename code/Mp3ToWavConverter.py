import os
from pydub import AudioSegment

def convert_mp3_to_wav(root_directory):
    # Traverse all subdirectories
    for subdir, _, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith(".MP3"):
                # Construct full file path
                mp3_path = os.path.join(subdir, filename)
                # Define the output .wav path
                wav_path = os.path.join(subdir, os.path.splitext(filename)[0] + ".wav")
                
                # Load the .mp3 file
                audio = AudioSegment.from_mp3(mp3_path)
                
                # Export as .wav
                audio.export(wav_path, format="wav")
                print(f"Converted {mp3_path} to {wav_path}")

# Specify the root directory containing the subdirectories
root_directory = "D:\\MTP\\Audio Files\\slokas"

# Call the conversion function
convert_mp3_to_wav(root_directory)
