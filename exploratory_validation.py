
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio file
file_path = 'audio.wav'
y, sr = librosa.load(file_path)

# Extract pitch using librosa
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# Get the average pitch
mean_pitches = []
for i in range(pitches.shape[1]):
    pitch = pitches[:, i][pitches[:, i] > 0]
    if len(pitch) > 0:
        mean_pitch = sum(pitch) / len(pitch)
        mean_pitches.append(mean_pitch)

# Plot pitch
plt.figure(figsize=(10, 6))
librosa.display.specshow(librosa.amplitude_to_db(magnitudes, ref=np.max),
                         y_axis='log', x_axis='time', sr=sr)
plt.colorbar(format='%+2.0f dB')
plt.title('Pitch estimation')
plt.plot(librosa.times_like(mean_pitches), librosa.hz_to_midi(mean_pitches), color='red', marker='o', label='Estimated pitch')
plt.ylabel('Hz')
plt.xlabel('Time')
plt.show()
