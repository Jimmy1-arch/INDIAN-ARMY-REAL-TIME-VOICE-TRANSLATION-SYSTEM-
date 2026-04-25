from pydub import AudioSegment
import uuid

def split_audio(file_path, chunk_length_ms=5000):
    audio = AudioSegment.from_file(file_path)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i+chunk_length_ms]
        name = f"chunk_{uuid.uuid4().hex}.wav"
        chunk.export(name, format="wav")
        chunks.append(name)
    return chunks
