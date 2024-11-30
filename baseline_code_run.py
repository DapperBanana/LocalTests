
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio file
audio_file = "path/to/audio/file.wav"
y, sr = librosa.load(audio_file)

# Get the pitch of the audio
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# Find the dominant pitch at each frame
pitch = []
for i in range(pitches.shape[1]):
    pitch_idx = magnitudes[:, i].argmax()
    pitch_hz = pitches[pitch_idx, i]
    pitch.append(pitch_hz)

# Display the pitch chart
plt.figure(figsize=(14, 5))
librosa.display.specshow(librosa.amplitude_to_db(magnitudes, ref=np.max), y_axis='log', x_axis='time', sr=sr)
plt.colorbar(format='%+2.0f dB')
plt.title('Pitch estimation')
plt.tight_layout()
plt.show()
