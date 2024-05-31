
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio file
audio_file = "example_audio.wav"
y, sr = librosa.load(audio_file)

# Calculate the pitch using the spectral centroid
spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

# Display the spectrogram and spectral centroid
plt.figure(figsize=(12, 6))
librosa.display.specshow(librosa.amplitude_to_db(librosa.stft(y), ref=np.max), y_axis='log', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.plot(librosa.times_like(spectral_centroids), spectral_centroids, label='Spectral centroid', color='w')
plt.legend(loc='upper right')
plt.title('Spectrogram with Spectral Centroid')
plt.show()
