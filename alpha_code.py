
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load audio file using librosa
audio_file = "example.wav"
y, sr = librosa.load(audio_file)

# Calculate pitches using librosa
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# Get the pitch with the maximum magnitude for each frame
max_pitches = [pitches[np.argmax(magnitudes[:, i]), i] for i in range(pitches.shape[1])]

# Plot the pitch contour
plt.figure(figsize=(12, 6))
librosa.display.specshow(librosa.amplitude_to_db(magnitudes, ref=np.max),
                         y_axis='log', x_axis='time', sr=sr)
plt.colorbar(format='%+2.0f dB')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Pitch estimation')
plt.plot(librosa.times_like(max_pitches, sr=sr), max_pitches, color='c', linewidth=1, label='Estimated pitch')
plt.tight_layout()
plt.show()
