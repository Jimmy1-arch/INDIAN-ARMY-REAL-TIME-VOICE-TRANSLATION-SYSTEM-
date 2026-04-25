import numpy as np
import sounddevice as sd
import wave
import uuid

class AudioMonitor:
    def __init__(self, sample_rate=16000, duration=3):
        self.sample_rate = sample_rate
        self.duration = duration

    def record(self):
        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="float32"
        )
        sd.wait()
        return audio.flatten()

    def save_audio(self, audio_data):
        filename = f"temp_{uuid.uuid4().hex}.wav"
        audio_int16 = (audio_data * 32767).astype(np.int16)
        with wave.open(filename, "w") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(self.sample_rate)
            wf.writeframes(audio_int16.tobytes())
        return filename
