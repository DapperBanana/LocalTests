
import librosa

def analyze_pitch(audio_file):
    y, sr = librosa.load(audio_file)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    
    average_pitch = []
    for i, pitch in enumerate(pitches):
        non_zero_pitches = pitch[pitch != 0]
        average_pitch.append(sum(non_zero_pitches) / len(non_zero_pitches))
    
    return average_pitch

audio_file = "sample_audio.wav"
pitch_values = analyze_pitch(audio_file)

print("Average pitch values:")
print(pitch_values)
