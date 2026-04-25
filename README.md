# 🛡 INDIAN ARMY REAL-TIME VOICE TRANSLATION SYSTEM (PROJECT SENTINEL)

A real-time voice intelligence system designed for mission-critical environments.  
The system captures live audio, converts speech to text, translates it, and detects potential threats using keyword analysis.

---

## 🚀 FEATURES

- 🎙 Real-time voice capture (Push-to-Talk)
- 🌐 Speech-to-text transcription
- 🔄 Language translation (multi-language support)
- ⚠️ Threat keyword detection system
- 📂 Audio upload + batch processing
- 📊 Live intelligence dashboard (Streamlit UI)
- 🔊 Audio playback for verification

---

## 🧠 SYSTEM ARCHITECTURE

Audio Input → Transcriber → Translator → Threat Detector → Dashboard

- **AudioMonitor** → captures real-time audio  
- **Transcriber** → converts speech → text  
- **Translator** → translates text to English  
- **Threat Detector** → identifies suspicious keywords  
- **Streamlit UI** → displays logs + alerts  

---

## 🛠 TECH STACK

- Python  
- Streamlit  
- Speech Recognition Models (Whisper / similar)  
- APIs (Google / OpenAI – optional)  
- Custom Threat Detection Engine  

---

## 📂 PROJECT STRUCTURE

core/
 ├── audio_stream.py  
 ├── transcriber.py  
 ├── translator.py  
 ├── threat_detector.py  
 ├── audio_utils.py  

app.py  
utils/  

---

## ⚙️ INSTALLATION

```bash
git clone https://github.com/your-username/project-sentinel.git
cd project-sentinel
pip install -r requirements.txt

RUN THE PROJECT
streamlit run app.py

🔹 Audio Capture
audio_data = monitor.record()
audio_file = monitor.save_audio(audio_data)
🔹 Transcription
text, lang = transcriber.transcribe(audio_file)
🔹 Translation
translated = translator.translate(text)
🔹 Threat Detection
threats = detect_threat(translated)
🔹 Logging System
st.session_state.logs.insert(0, {
    "time": datetime.now().strftime("%H:%M:%S"),
    "text": text,
    "translated": translated,
    "threats": threats,
    "audio": audio_file
})
📡 CURRENT STATUS
✅ Real-time transcription working
✅ Translation working (API-based)
✅ Threat detection working
⚠️ Currently depends on online APIs
🔧 ISSUE (CURRENT)
ModuleNotFoundError: No module named 'googletrans'
✔️ Fix:
pip install googletrans==4.0.0-rc1
🔮 FUTURE WORK (IMPORTANT)
🎯 OFFLINE MODEL IMPLEMENTATION (IN PROGRESS)

Currently:

Uses online APIs for translation

Target:

Fully offline system using trained models
Planned Improvements:
🔹 Offline translation using MarianMT / HuggingFace models
🔹 Custom trained NLP model for threat detection
🔹 Edge deployment (Raspberry Pi / field devices)
🔹 Real-time streaming (no push-to-talk)
🔹 Multilingual support without internet
🧪 EXAMPLE OUTPUT
[12:45:32]
Original: "Enemy approaching from north"
English: "Enemy approaching from north"
Threat Words: enemy, attack
🛡 USE CASES
Military communication support
Border surveillance intelligence
Disaster response coordination
Law enforcement monitoring systems
