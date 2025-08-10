
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio file
audio_file = 'audio.wav'
y, sr = librosa.load(audio_file)

# Get the pitches using the librosa library
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# Get the mean pitch over time
mean_pitch = []
for i in range(pitches.shape[1]):
    mean_pitch.append(librosa.hz_to_midi(np.mean(pitches[:,i])))

# Plot the pitch over time
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.amplitude_to_db(magnitudes, ref=np.max), y_axis='log', x_axis='time', sr=sr)
plt.colorbar()
plt.title('Pitch Analysis')
plt.tight_layout()

plt.figure()
plt.plot(mean_pitch)
plt.xlabel('Time')
plt.ylabel('Pitch (MIDI)')
plt.title('Mean Pitch over Time')

plt.show()
