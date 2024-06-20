
import librosa

# Load audio file
audio_path = "audio.wav"
y, sr = librosa.load(audio_path)

# Compute the pitch
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

# Get the pitch with highest magnitude for each frame
pitch_values = []
for i in range(pitches.shape[1]):
    pitch_value = pitches[:,i][np.argmax(magnitudes[:,i])]
    pitch_values.append(pitch_value)

# Print the pitch values
print("Pitch values for each frame:", pitch_values)
