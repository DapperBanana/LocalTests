
import librosa
import numpy as np

# Load audio file
audio_file = 'example_audio.wav'
y, sr = librosa.load(audio_file)

# Calculate pitch using librosa
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# Get the frequency with the maximum magnitude for each frame
pitch = []
for i in range(pitches.shape[1]):
    index = np.argmax(magnitudes[:, i])
    freq = pitches[index, i]
    pitch.append(librosa.core.hz_to_midi(freq))

# Print the pitch for each frame
for i, p in enumerate(pitch):
    print(f"Frame {i+1}: {p} MIDI")
