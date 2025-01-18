
import librosa

# Load audio file
audio_file = 'example_audio.wav'
y, sr = librosa.load(audio_file)

# Compute the pitch using a time-frequency transform
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

# Get the estimated pitch by selecting the maximum magnitude for each frame
estimated_pitches = []
for i in range(pitches.shape[1]):
    index = magnitudes[:, i].argmax()
    estimated_pitches.append(pitches[index, i])

# Print the estimated pitches
print("Estimated pitches:")
for pitch in estimated_pitches:
    print(pitch)
