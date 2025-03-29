
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio file
audio_file = 'audio.wav'
y, sr = librosa.load(audio_file)

# Extract pitch information
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

# Calculate pitch from pitch detection
pitch = []
for i in range(pitches.shape[1]):
    index = magnitudes[:, i].argmax()
    pitch.append(librosa.hz_to_midi(pitches[index, i]))

# Plot pitch contour
plt.figure(figsize=(10, 6))
librosa.display.specshow(pitches, y_axis='hz', x_axis='time', sr=sr)
plt.colorbar()
plt.title('Pitch Contour')
plt.tight_layout()
plt.show()

# Display pitch values
print('Pitch (in MIDI) at each time frame:')
print(pitch)
