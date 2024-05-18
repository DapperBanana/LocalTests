
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio file
audio_path = 'path/to/audio/file.wav'
y, sr = librosa.load(audio_path)

# Extract pitch
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# Find dominant pitch
pitch_mean = librosa.estimate_tuning(y=y, sr=sr)

# Plot pitch
plt.figure(figsize=(10, 6))
librosa.display.specshow(librosa.amplitude_to_db(magnitudes, ref=np.max), y_axis='log', x_axis='time')
plt.title('Pitch')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()

print(f'Dominant pitch: {pitch_mean} Hz')
