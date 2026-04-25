from openai import OpenAI
import os

class AIThreatAnalyst:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.enabled = bool(api_key)
        if self.enabled:
            self.client = OpenAI(api_key=api_key)

    def analyze(self, text):
        if not self.enabled:
            return "AI analysis offline"

        prompt = f"""
You are an Indian Army tactical intelligence assistant deployed in a hostile region.

Analyze the intercepted speech for operational threats.

Speech: "{text}"

Return strictly:
Threat Level: (0-4)
Reason: (short tactical explanation)
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"AI analysis error: {e}"
