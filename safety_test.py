
import librosa
import numpy as np

def analyze_pitch(audio_file_path):
    y, sr = librosa.load(audio_file_path)
    
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    
    pitch_mean = np.mean(pitches)
    pitch_std = np.std(pitches)
    
    return pitch_mean, pitch_std

audio_file_path = "path/to/audio/file.wav"
pitch_mean, pitch_std = analyze_pitch(audio_file_path)

print(f"Mean pitch: {pitch_mean}")
print(f"Pitch standard deviation: {pitch_std}")
