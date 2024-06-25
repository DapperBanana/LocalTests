letion(id='chatcmpl-9e5reJrphx4GC4lu1Om2RVbFmn2ul', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import librosa
import numpy as np

# Load an audio file
audio_file = 'audio.wav'
y, sr = librosa.load(audio_file)

# Extract pitch from the audio data
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

# Get the pitch with the highest magnitude
index = np.argmax(magnitudes)
pitch = pitches[index]

print(f"The pitch of the audio is: {pitch}")', role='assistant', function_call=None, tool_calls=None))], created=1719342690, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=93, prompt_tokens=23, total_tokens=116)