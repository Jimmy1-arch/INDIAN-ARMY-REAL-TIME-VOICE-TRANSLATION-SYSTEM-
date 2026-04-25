import json
import os
import utils.config as config
from collections import deque
import time

class ThreatScanner:
    def __init__(self):
        self.threats = self._load_threats()
        # Persistence window: Keep track of recent threats to escalate level if needed
        # (Not fully implemented for basic scan, but ready for logic extension)
        self.history = deque(maxlen=10) 

    def _load_threats(self):
        if not os.path.exists(config.THREATS_FILE):
            print(f"[WARNING] Threat file not found at {config.THREATS_FILE}")
            return []
        
        with open(config.THREATS_FILE, 'r') as f:
            data = json.load(f)
            return data.get("keywords", [])

    def scan(self, text: str):
        """
        Scans only the current text segment for threats.
        Returns: (max_level, detected_keywords_list)
        """
        text_lower = text.lower()
        max_level = 0
        detected = []

        for item in self.threats:
            word = item["word"]
            # Basic substring match - for Production use Regex allows word boundaries
            if word in text_lower: 
                level = item["level"]
                detected.append(word)
                if level > max_level:
                    max_level = level
        
        return max_level, list(set(detected)) # Unique keywords
