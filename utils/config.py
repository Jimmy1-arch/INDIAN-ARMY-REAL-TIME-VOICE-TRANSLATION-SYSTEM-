import os

# System Configuration
APP_NAME = "Project SENTINEL"
VERSION = "1.0.0 (Alpha)"

# Audio Configuration
SAMPLE_RATE = 16000
CHUNK_DURATION_MS = 30  # Frame duration for VAD
FRAME_SIZE = int(SAMPLE_RATE * CHUNK_DURATION_MS / 1000)
VAD_AGGRESSIVENESS = 3  # 0-3 (3 is most aggressive in filtering silence)

# Model Configuration
MODEL_SIZE = "tiny.en" # 'tiny', 'base', 'small', 'medium', 'large'
# Note: 'tiny.en' is English only, smaller and faster. Use 'tiny' for multilingual. 
# For Hackathon demo (often English scripts), tiny.en is safest. 
# If multilingual needed, switch to 'tiny'.

# Path Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # utils/
PROJECT_ROOT = os.path.dirname(BASE_DIR)              # SENTINEL/
THREATS_FILE = os.path.join(PROJECT_ROOT, "core", "threats.json")

# Visuals
THREAT_COLORS = {
    0: "#2ecc71", # Green (Safe)
    1: "#3498db", # Blue (Awareness)
    2: "#f1c40f", # Yellow (Suspicious)
    3: "#e67e22", # Orange (High Risk)
    4: "#e74c3c"  # Red (CRITICAL)
}
