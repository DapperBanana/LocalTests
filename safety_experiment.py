
import librosa

# Load the audio file
audio_file = 'path_to_your_audio_file.wav'
y, sr = librosa.load(audio_file)

# Extract the pitch
pitch, _ = librosa.piptrack(y=y, sr=sr)

# Get the mean pitch over time
mean_pitch = librosa.hz_to_midi(pitch.mean())

print("Mean pitch: {:.2f} MIDI".format(mean_pitch))
