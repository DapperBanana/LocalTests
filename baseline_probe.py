
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load audio file
audio_path = 'example_audio.wav'
y, sr = librosa.load(audio_path)

# Extract pitch (fundamental frequency) from audio data
pitch, _ = librosa.piptrack(y=y, sr=sr)

# Average pitch values across all frequencies
mean_pitch = np.mean(pitch, axis=0)

# Plot pitch curve
plt.figure(figsize=(10, 4))
librosa.display.waveshow(y=y, sr=sr, x_axis='time')
plt.plot(librosa.times_like(mean_pitch, sr=sr), mean_pitch, color='r')
plt.title('Pitch Analysis')
plt.xlabel('Time (s)')
plt.ylabel('Pitch')
plt.show()
