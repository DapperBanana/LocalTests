
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio file
audio_file = 'path/to/audio/file.wav'
y, sr = librosa.load(audio_file)

# Extract pitch using librosa
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

# Get the pitch with the highest magnitude for each frame
pitch = []
for i in range(pitches.shape[1]):
    index = magnitudes[:, i].argmax()
    pitch.append(pitches[index, i])

# Plot the pitch
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.amplitude_to_db(magnitudes, ref=np.max), y_axis='log', x_axis='time', sr=sr)
plt.colorbar()
plt.title('Pitch')
plt.tight_layout()
plt.show()

print('Pitch values:', pitch)
