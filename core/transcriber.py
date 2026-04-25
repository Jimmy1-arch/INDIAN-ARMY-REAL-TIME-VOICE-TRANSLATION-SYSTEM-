# from faster_whisper import WhisperModel
# import numpy as np
# import utils.config as config
# import os
#
# class Transcriber:
#     def __init__(self):
#         print(f"[SENTINEL] Loading Whisper Model ({config.MODEL_SIZE})...")
#         # Run on CPU with INT8 quantization for widespread device support
#         try:
#             self.model = WhisperModel(config.MODEL_SIZE, device="cpu", compute_type="int8")
#             print("[SENTINEL] Model Loaded Successfully.")
#         except Exception as e:
#             print(f"[ERROR] Failed to load model: {e}")
#             self.model = None
#
#     def transcribe(self, audio_bytes: bytes) -> str:
#         """
#         Transcribes raw audio bytes (PCM 16-bit 16kHz) to text.
#         """
#         if not self.model:
#             return ""
#
#         # Convert raw bytes to float32 numpy array
#         # 1. From bytes to int16
#         audio_int16 = np.frombuffer(audio_bytes, np.int16)
#         # 2. To float32 normalized between -1 and 1
#         audio_float32 = audio_int16.astype(np.float32) / 32768.0
#
#         try:
#             segments, info = self.model.transcribe(
#                 audio_float32,
#                 beam_size=5,
#                 language="en", # Force English for hackathon demo consistency, or remove to auto-detect
#                 condition_on_previous_text=False
#             )
#
#             full_text = " ".join([segment.text for segment in segments])
#             return full_text.strip()
#         except Exception as e:
#             print(f"[TRANSCRIPTION ERROR] {e}")
#             return ""

from faster_whisper import WhisperModel

class Transcriber:
    def __init__(self):
        self.model = WhisperModel("base", device="cpu", compute_type="int8")

    def transcribe(self, audio_path):
        segments, info = self.model.transcribe(audio_path)
        text = " ".join([seg.text for seg in segments]).strip()
        return text, info.language
