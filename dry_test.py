
import librosa

# Load audio file
audio_path = 'audio.wav'
y, sr = librosa.load(audio_path)

# Extract pitch from audio data
pitch, _ = librosa.core.piptrack(y=y, sr=sr)

# Get the most dominant pitch
dominant_pitch_index = pitch.max(axis=1).argmax()
dominant_pitch = pitch[dominant_pitch_index]

print(f"The dominant pitch is: {dominant_pitch}")
