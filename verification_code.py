
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load audio file
audio_file = "path_to_audio_file.wav"
y, sr = librosa.load(audio_file)

# Extract pitch contours
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

# Compute pitch from pitch contours
pitch = np.argmax(magnitudes, axis=0)

# Plot pitch contour
plt.figure(figsize=(12, 6))
plt.plot(librosa.times_like(pitch), pitch)
plt.xlabel('Time (s)')
plt.ylabel('Pitch')
plt.title('Pitch Contour')
plt.show()
