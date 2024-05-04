
import librosa

# Load an audio file
audio_path = 'sample_audio.wav'
y, sr = librosa.load(audio_path)

# Extract pitch using librosa
pitch, _ = librosa.piptrack(y=y, sr=sr)

# Calculate the mean pitch
mean_pitch = pitch.mean()

print(f"The mean pitch of the audio is {mean_pitch} Hz.")
