
import librosa
import numpy as np

# Load audio file
file_path = "audio_sample.wav"
data, sr = librosa.load(file_path)

# Extract pitch using librosa library
f0, voiced_flag, voiced_probs = librosa.pyin(data, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

# Print the pitch values
print("Pitch values:")
for i, pitch in enumerate(f0):
    if voiced_flag[i]:
        print(f"Frame {i}: {pitch} Hz")

# Visualize the pitch contour
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(librosa.times_like(f0), f0, label='Pitch (Hz)', color='b')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.title('Pitch Contour')
plt.legend()
plt.show()
