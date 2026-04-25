THREAT_WORDS = ["gun", "bomb", "attack", "grenade", "kill"]

def detect_threat(text):
    found = [w for w in THREAT_WORDS if w in text.lower()]
    return found
