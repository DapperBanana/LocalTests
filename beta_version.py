
import librosa
import numpy as np

# Load audio file
audio_file = 'path_to_audio_file.wav'
y, sr = librosa.load(audio_file)

# Extract pitch information using librosa
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# Get dominant pitch for each frame
pitch_mean = []
for i in range(pitches.shape[1]):
    pitch_mean.append(np.argmax(magnitudes[:, i]))

# Convert pitch values to Hz
pitch_values = []
for p in pitch_mean:
    pitch_values.append(librosa.midi_to_hz(p))

# Print the extracted pitch values
print("Pitch values (in Hz):", pitch_values)
