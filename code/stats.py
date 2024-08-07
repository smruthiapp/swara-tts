import os
from pydub import AudioSegment
from datetime import timedelta
from tqdm import tqdm

def compute_audio_duration(directory, file_type=".mp3"):  # Set the default file type as ".mp3"
    # Initialize total duration, maximum duration, minimum duration, and number of audio files
    total_duration = 0
    max_duration = float('-inf')
    min_duration = float('inf')
    num_files = 0

    # Iterate over all files in the directory
    for filename in tqdm(os.listdir(directory), desc="Processing audio files"):
        if filename.lower().endswith(file_type):
            # Load the audio file
            audio = AudioSegment.from_file(os.path.join(directory, filename))
            
            # Get the duration of the audio file
            duration = len(audio)
            
            # Update total duration
            total_duration += duration
            
            # Update maximum duration
            if duration > max_duration:
                max_duration = duration
            
            # Update minimum duration
            if duration < min_duration:
                min_duration = duration
            
            # Increment the number of audio files
            num_files += 1

    # Convert the total duration to timedelta object
    total_duration = timedelta(milliseconds=total_duration)

    # Calculate the average duration
    avg_duration = total_duration / num_files

    # Return the results as a dictionary
    results = {
        "total_duration": str(total_duration),
        "max_duration": str(timedelta(milliseconds=max_duration)),
        "min_duration": str(timedelta(milliseconds=min_duration)),
        "avg_duration": str(avg_duration)
    }
    
    return results

# Example usage
directory = "./HolyGitaAudio"
results = compute_audio_duration(directory)

# Print the results
print("Total duration:", results["total_duration"])
print("Maximum duration:", results["max_duration"])
print("Minimum duration:", results["min_duration"])
print("Average duration:", results["avg_duration"])
