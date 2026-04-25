# # import os
# # from openai import OpenAI
# #
# # class LiveTranslator:
# #     def __init__(self):
# #         api_key = os.getenv("OPENAI_API_KEY")
# #         self.enabled = bool(api_key)
# #         if self.enabled:
# #             self.client = OpenAI(api_key=api_key)
# #
# #     def translate(self, text):
# #         if not self.enabled:
# #             return "Translation offline"
# #
# #         prompt = f"""
# # You are a real-time military field translator.
# #
# # Translate the following spoken sentence into clear English.
# # Keep it short and natural.
# #
# # Speech: "{text}"
# # """
# #
# #         try:
# #             response = self.client.chat.completions.create(
# #                 model="gpt-4o-mini",
# #                 messages=[{"role": "user", "content": prompt}],
# #                 temperature=0.2,
# #             )
# #             return response.choices[0].message.content.strip()
# #         except Exception as e:
# #             return f"Translation error: {e}"
#
# import os
# from openai import OpenAI
#
# class LiveTranslator:
#     def __init__(self):
#         api_key = os.getenv("OPENAI_API_KEY")
#         self.enabled = bool(api_key)
#         if self.enabled:
#             self.client = OpenAI(api_key=api_key)
#
#     def translate(self, text, source_lang="unknown"):
#         if not self.enabled:
#             return {
#                 "translation": "Translation offline",
#                 "confidence": "N/A"
#             }
#
#         prompt = f"""
# You are a military field translator.
#
# Detected Language: {source_lang}
#
# Translate the speech into clear English.
#
# Then estimate how confident you are in the translation (0–100%).
#
# Return ONLY in this format:
# Translation: <english sentence>
# Confidence: <number>%
# Speech: "{text}"
# """
#
#         try:
#             response = self.client.chat.completions.create(
#                 model="gpt-4o-mini",
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.2,
#             )
#
#             reply = response.choices[0].message.content.strip()
#
#             lines = reply.split("\n")
#             translation = lines[0].replace("Translation:", "").strip()
#             confidence = lines[1].replace("Confidence:", "").strip()
#
#             return {
#                 "translation": translation,
#                 "confidence": confidence
#             }
#
#         except Exception as e:
#             return {
#                 "translation": f"Translation error: {e}",
#                 "confidence": "0%"
#             }

import os
from openai import OpenAI

class LiveTranslator:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.enabled = bool(api_key)
        if self.enabled:
            self.client = OpenAI(api_key=api_key)

        # Simple offline fallback dictionary (extendable)
        self.offline_dict = {
            "ruk": "stop",
            "bhaag": "run",
            "idhar": "here",
            "udhar": "there",
            "jaldi": "quickly",
            "rukho": "wait",
            "kya": "what",
            "kaun": "who",
            "ghar": "house",
            "aaj": "today",
            "kal": "tomorrow",
            "bandook": "gun",
            "fauj": "army",
            "police": "police",
            "hamla": "attack",
        }

    def offline_translate(self, text):
        words = text.lower().split()
        translated_words = [self.offline_dict.get(w, w) for w in words]
        return " ".join(translated_words)

    def translate(self, text, source_lang="unknown"):
        # Try API first if available
        if self.enabled:
            try:
                prompt = f"""
You are a military field translator.

Detected Language: {source_lang}

Translate the speech into clear English.
Then estimate your confidence (0–100%).

Return ONLY in format:
Translation: <english>
Confidence: <number>%
Speech: "{text}"
"""

                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2,
                )

                reply = response.choices[0].message.content.strip().split("\n")
                translation = reply[0].replace("Translation:", "").strip()
                confidence = reply[1].replace("Confidence:", "").strip()

                return {
                    "translation": translation,
                    "confidence": confidence
                }

            except Exception:
                # API failed → fallback
                pass

        # Offline fallback
        fallback = self.offline_translate(text)
        return {
            "translation": fallback,
            "confidence": "Low (offline fallback)"
        }
