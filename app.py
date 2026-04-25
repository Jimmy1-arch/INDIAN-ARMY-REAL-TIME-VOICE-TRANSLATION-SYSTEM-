# # # import streamlit as st
# # # import time
# # # from datetime import datetime
# # # import os
# # # from core.ai_analyst import AIThreatAnalyst
# # # import utils.config as config
# # # from core.audio_stream import AudioMonitor
# # # from core.transcriber import Transcriber
# # # from core.threat_engine import ThreatScanner
# # #
# # #
# # # # Page Configuration
# # # st.set_page_config(
# # #     page_title="SENTINEL | Tactical AI",
# # #     page_icon="🛡️",
# # #     layout="wide",
# # #     initial_sidebar_state="expanded"
# # # )
# # #
# # # # Custom CSS for Army Aesthetic
# # # st.markdown("""
# # # <style>
# # #     .stApp {
# # #         background-color: #0e1117;
# # #         color: #e0e0e0;
# # #     }
# # #     .stButton>button {
# # #         background-color: #2c3e50;
# # #         color: white;
# # #         border: 1px solid #34495e;
# # #     }
# # #     .threat-level-0 { border-left: 5px solid #2ecc71; padding-left: 10px; }
# # #     .threat-level-1 { border-left: 5px solid #3498db; padding-left: 10px; }
# # #     .threat-level-2 { border-left: 5px solid #f1c40f; padding-left: 10px; }
# # #     .threat-level-3 { border-left: 5px solid #e67e22; padding-left: 10px; background-color: rgba(230, 126, 34, 0.1); }
# # #     .threat-level-4 { border-left: 5px solid #e74c3c; padding-left: 10px; background-color: rgba(231, 76, 60, 0.2); font-weight: bold;}
# # #
# # #     .big-alert {
# # #         font-size: 40px;
# # #         color: red;
# # #         font-weight: bold;
# # #         text-align: center;
# # #         animation: blinker 1s linear infinite;
# # #     }
# # #     @keyframes blinker {
# # #         50% { opacity: 0; }
# # #     }
# # # </style>
# # # """, unsafe_allow_html=True)
# # #
# # # # Application Header
# # # col1, col2 = st.columns([1, 4])
# # # with col1:
# # #     st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_India.svg", width=100) # Placeholder or local asset
# # # with col2:
# # #     st.title("PROJECT SENTINEL")
# # #     st.caption(f"Tactical Voice Intelligence System | v{config.VERSION}")
# # #
# # # # Sidebar
# # # st.sidebar.header("Mission Control")
# # # st.sidebar.markdown("---")
# # # status_indicator = st.sidebar.empty()
# # #
# # # # Initialize State
# # # if 'listening' not in st.session_state:
# # #     st.session_state.listening = False
# # # if 'logs' not in st.session_state:
# # #     st.session_state.logs = []
# # #
# # # def start_listening():
# # #     st.session_state.listening = True
# # #
# # # def stop_listening():
# # #     st.session_state.listening = False
# # #
# # # col_ctrl1, col_ctrl2 = st.sidebar.columns(2)
# # # with col_ctrl1:
# # #     start_btn = st.button("🔴 START OP", on_click=start_listening)
# # # with col_ctrl2:
# # #     stop_btn = st.button("⬛ HALT", on_click=stop_listening)
# # #
# # # # Main Display Area
# # # main_placeholder = st.empty()
# # # alert_placeholder = st.empty()
# # #
# # # # Processing Loop
# # # if st.session_state.listening:
# # #     status_indicator.markdown("## 🟢 STATUS: LIVE")
# # #
# # #     # Initialize Core Modules (Lazy loading to avoid startup lag)
# # #     if 'monitor' not in st.session_state:
# # #         with st.spinner("Initializing DSP & Neural Models..."):
# # #             st.session_state.monitor = AudioMonitor()
# # #             st.session_state.transcriber = Transcriber()
# # #             st.session_state.scanner = ThreatScanner()
# # #             st.success("Systems Online.")
# # #             time.sleep(1) # Visual confirmation
# # #
# # #     monitor = st.session_state.monitor
# # #     transcriber = st.session_state.transcriber
# # #     scanner = st.session_state.scanner
# # #
# # #     # Streaming Loop
# # #     # Note: In a real app, this would be a separate thread updating a queue.
# # #     # For Streamlit prototype, we run the generator directly.
# # #     try:
# # #         # We need a way to break the loop to update UI if needed,
# # #         # but st.empty() allows in-place updates.
# # #
# # #         # Display logs container
# # #         with main_placeholder.container():
# # #             st.subheader("Live Intecept Log")
# # #             log_container = st.container()
# # #
# # #         for audio_chunk in monitor.listen_loop():
# # #             if not st.session_state.listening:
# # #                 break
# # #
# # #             # 1. Transcribe
# # #             text = transcriber.transcribe(audio_chunk)
# # #
# # #             if text:
# # #                 # 2. Analyze
# # #                 level, keywords = scanner.scan(text)
# # #                 timestamp = datetime.now().strftime("%H:%M:%S")
# # #
# # #                 # 3. Store Log
# # #                 entry = {
# # #                     "time": timestamp,
# # #                     "text": text,
# # #                     "level": level,
# # #                     "keywords": keywords
# # #                 }
# # #                 st.session_state.logs.insert(0, entry) # Prepend
# # #
# # #                 # 4. Trigger Alerts
# # #                 if level >= 3:
# # #                      alert_placeholder.markdown(f'<div class="big-alert">⚠️ THREAT DETECTED: {", ".join(keywords).upper()}</div>', unsafe_allow_html=True)
# # #                 else:
# # #                     alert_placeholder.empty()
# # #
# # #                 # 5. Update UI
# # #                 with log_container:
# # #                      # Re-render logs (limit to last 20)
# # #                      for log in st.session_state.logs[:20]:
# # #                          css_class = f"threat-level-{log['level']}"
# # #                          st.markdown(f"""
# # #                          <div class="{css_class}">
# # #                             <span style="color: #888; font-size: 0.8em;">[{log['time']}]</span>
# # #                             <span style="font-weight: bold; color: {config.THREAT_COLORS[log['level']]};">LVL {log['level']}</span>:
# # #                             {log['text']}
# # #                          </div>
# # #                          """, unsafe_allow_html=True)
# # #
# # #     except Exception as e:
# # #         st.error(f"Operational Error: {e}")
# # #         st.session_state.listening = False
# # #
# # # else:
# # #     status_indicator.markdown("## ⚪ STATUS: STANDBY")
# # #     st.info("System is offline. Press 'START OP' to begin surveillance.")
# # #
# # #     # Show history even when stopped
# # #     if st.session_state.logs:
# # #         st.subheader("Mission Log History")
# # #         for log in st.session_state.logs:
# # #              css_class = f"threat-level-{log['level']}"
# # #              st.markdown(f"""
# # #              <div class="{css_class}">
# # #                 <span style="color: #888; font-size: 0.8em;">[{log['time']}]</span>
# # #                 <span style="font-weight: bold; color: {config.THREAT_COLORS[log['level']]};">LVL {log['level']}</span>:
# # #                 {log['text']}
# # #              </div>
# # #              """, unsafe_allow_html=True)
# #
# # import time
# # from datetime import datetime
# # import os
# #
# # # ---- Safe Session State Initialization ----
# # import streamlit as st
# # # ---- Safe Session State Initialization ----
# # st.session_state.setdefault("logs", [])
# # st.session_state.setdefault("monitor", None)
# # st.session_state.setdefault("transcriber", None)
# # st.session_state.setdefault("translator", None)
# #
# # import utils.config as config
# # from core.audio_stream import AudioMonitor
# # from core.transcriber import Transcriber
# # from core.live_translator import LiveTranslator
# #
# # # Page Configuration
# # st.set_page_config(
# #     page_title="SENTINEL | Field Translator",
# #     page_icon="🎧",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )
# #
# # # UI Styling
# # st.markdown("""
# # <style>
# #     .stApp { background-color: #0e1117; color: #e0e0e0; }
# #     .translation-box {
# #         border-left: 5px solid #3498db;
# #         padding-left: 12px;
# #         margin-bottom: 12px;
# #         background-color: rgba(52, 152, 219, 0.08);
# #     }
# # </style>
# # """, unsafe_allow_html=True)
# #
# # # Header
# # st.title("🎧 SENTINEL – Real-Time Field Translator")
# # st.caption("Live Speech Translation for Field Officers")
# #
# # # Sidebar
# # st.sidebar.header("Mission Control")
# # status_indicator = st.sidebar.empty()
# #
# # # API KEY INPUT
# # st.sidebar.markdown("### 🌐 Live Translation AI (Optional)")
# # api_key = st.sidebar.text_input("Enter ChatGPT API Key", type="password")
# #
# # if api_key:
# #     os.environ["OPENAI_API_KEY"] = api_key
# #     st.sidebar.success("Live Translation Enabled")
# # else:
# #     st.sidebar.caption("Running in Transcription-Only Mode")
# #
# # # State Init
# # if 'listening' not in st.session_state:
# #     st.session_state.listening = False
# # if 'logs' not in st.session_state:
# #     st.session_state.logs = []
# #
# # def start_listening():
# #     st.session_state.listening = True
# #
# # def stop_listening():
# #     st.session_state.listening = False
# #
# # col1, col2 = st.sidebar.columns(2)
# # col1.button("▶ START LISTENING", on_click=start_listening)
# # col2.button("⏹ STOP", on_click=stop_listening)
# #
# # main_placeholder = st.empty()
# #
# # # MAIN LOOP
# # if st.session_state.listening:
# #     status_indicator.markdown("### 🟢 STATUS: LISTENING")
# #
# #     # if 'monitor' not in st.session_state:
# #     #     with st.spinner("Initializing Audio & AI Models..."):
# #     #         st.session_state.monitor = AudioMonitor()
# #     #         st.session_state.transcriber = Transcriber()
# #     #         st.session_state.translator = LiveTranslator()
# #     if st.session_state.monitor is None:
# #         st.session_state.monitor = AudioMonitor()
# #         st.session_state.transcriber = Transcriber()
# #         st.session_state.translator = LiveTranslator()
# #         st.success("System Ready.")
# #         time.sleep(1)
# #
# #     monitor = st.session_state.monitor
# #     transcriber = st.session_state.transcriber
# #     translator = st.session_state.translator
# #
# #     try:
# #         with main_placeholder.container():
# #             st.subheader("🎙 Live Speech Translation")
# #             log_container = st.container()
# #
# #         # for audio_chunk in monitor.listen_loop():
# #         #     if not st.session_state.listening:
# #         #         break
# #             if st.button("🎤 RECORD 3 SECONDS"):
# #                 with st.spinner("Recording..."):
# #                     audio_data = monitor.record_push_to_talk()
# #                     audio_file = monitor.save_audio(audio_data)
# #
# #                 with st.spinner("Transcribing..."):
# #                     segments, info = transcriber.model.transcribe(audio_data, beam_size=5)
# #                     detected_lang = info.language
# #                     original_text = " ".join([seg.text for seg in segments]).strip()
# #
# #             # Speech → Text
# #             # text = transcriber.transcribe(audio_chunk)
# #             if st.button("🎤 RECORD 3 SECONDS"):
# #                 with st.spinner("Recording..."):
# #                     audio_data = monitor.record_push_to_talk()
# #                     audio_file = monitor.save_audio(audio_data)
# #
# #                 with st.spinner("Transcribing..."):
# #                     segments, info = transcriber.model.transcribe(audio_data, beam_size=5)
# #                     detected_lang = info.language
# #                     original_text = " ".join([seg.text for seg in segments]).strip()
# #
# #             if text:
# #                 # Text → English Translation
# #                 translated = translator.translate(text)
# #                 timestamp = datetime.now().strftime("%H:%M:%S")
# #
# #                 entry = {
# #                     "time": timestamp,
# #                     "original": text,
# #                     "translated": translated
# #                 }
# #                 st.session_state.logs.insert(0, entry)
# #
# #                 with log_container:
# #                     for log in st.session_state.logs[:20]:
# #                         st.markdown(f"""
# #                         <div class="translation-box">
# #                             <span style="color:#888;font-size:0.8em;">[{log['time']}]</span><br>
# #                             <b>🗣 Original:</b> {log['original']}<br>
# #                             <b>🌐 English:</b> {log['translated']}
# #                         </div>
# #                         """, unsafe_allow_html=True)
# #
# #     except Exception as e:
# #         st.error(f"Operational Error: {e}")
# #         st.session_state.listening = False
# #
# # else:
# #     status_indicator.markdown("### ⚪ STATUS: STANDBY")
# #     st.info("Press START LISTENING to begin real-time translation.")
# #
# #     if st.session_state.logs:
# #         st.subheader("Recent Translations")
# #         for log in st.session_state.logs:
# #             st.markdown(f"""
# #             <div class="translation-box">
# #                 <span style="color:#888;font-size:0.8em;">[{log['time']}]</span><br>
# #                 <b>🗣 Original:</b> {log['original']}<br>
# #                 <b>🌐 English:</b> {log['translated']}
# #             </div>
# #             """, unsafe_allow_html=True)
#
# import streamlit as st
# import time
# from datetime import datetime
# import os
#
# from core.audio_stream import AudioMonitor
# from core.transcriber import Transcriber
# from core.live_translator import LiveTranslator
#
# # ---------------- SESSION STATE INIT ----------------
# st.session_state.setdefault("logs", [])
# st.session_state.setdefault("monitor", None)
# st.session_state.setdefault("transcriber", None)
# st.session_state.setdefault("translator", None)
# st.session_state.setdefault("listening", False)
#
# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="SENTINEL | Field Translator",
#     page_icon="🎧",
#     layout="wide"
# )
#
# # ---------------- UI STYLE ----------------
# st.markdown("""
# <style>
# .stApp { background-color: #0e1117; color: #e0e0e0; }
# .translation-box {
#     border-left: 5px solid #3498db;
#     padding-left: 12px;
#     margin-bottom: 12px;
#     background-color: rgba(52, 152, 219, 0.08);
# }
# </style>
# """, unsafe_allow_html=True)
#
# # ---------------- HEADER ----------------
# st.title("🎧 SENTINEL – Real-Time Field Translator")
# st.caption("Push-to-talk translation system for field officers")
#
# # ---------------- SIDEBAR ----------------
# st.sidebar.header("Mission Control")
# status_indicator = st.sidebar.empty()
#
# api_key = st.sidebar.text_input("Enter ChatGPT API Key (Optional)", type="password")
# if api_key:
#     os.environ["OPENAI_API_KEY"] = api_key
#     st.sidebar.success("AI Translation Enabled")
# else:
#     st.sidebar.info("Running in transcription-only mode")
#
# def start():
#     st.session_state.listening = True
#
# def stop():
#     st.session_state.listening = False
#
# col1, col2 = st.sidebar.columns(2)
# col1.button("▶ START", on_click=start)
# col2.button("⏹ STOP", on_click=stop)
#
# # ---------------- MAIN ----------------
# if st.session_state.listening:
#     status_indicator.markdown("### 🟢 STATUS: LISTENING")
#
#     if st.session_state.monitor is None:
#         st.session_state.monitor = AudioMonitor()
#         st.session_state.transcriber = Transcriber()
#         st.session_state.translator = LiveTranslator()
#         st.success("System Ready.")
#         time.sleep(1)
#
#     monitor = st.session_state.monitor
#     transcriber = st.session_state.transcriber
#     translator = st.session_state.translator
#
#     st.subheader("🎙 Push-to-Talk Translator")
#
#     if st.button("🎤 RECORD 3 SECONDS"):
#         with st.spinner("Recording..."):
#             audio_data = monitor.record_push_to_talk()
#             audio_file = monitor.save_audio(audio_data)
#
#         with st.spinner("Transcribing..."):
#             segments, info = transcriber.model.transcribe(audio_data, beam_size=5)
#             detected_lang = info.language
#             original_text = " ".join([seg.text for seg in segments]).strip()
#
#         if original_text:
#             with st.spinner("Translating..."):
#                 result = translator.translate(original_text, detected_lang)
#
#             entry = {
#                 "time": datetime.now().strftime("%H:%M:%S"),
#                 "original": original_text,
#                 "translated": result["translation"],
#                 "confidence": result["confidence"],
#                 "audio": audio_file,
#                 "lang": detected_lang
#             }
#             st.session_state.logs.insert(0, entry)
#
#     st.subheader("📝 Recent Translations")
#
#     for log in st.session_state.logs[:15]:
#         st.markdown(f"""
#         <div class="translation-box">
#             <span style="color:#888;font-size:0.8em;">[{log['time']}]</span><br>
#             <b>🌍 Language:</b> {log['lang']}<br>
#             <b>🗣 Original:</b> {log['original']}<br>
#             <b>🌐 English:</b> {log['translated']}<br>
#             <b>📊 Confidence:</b> {log['confidence']}
#         </div>
#         """, unsafe_allow_html=True)
#
#         st.audio(log["audio"])
#
# else:
#     status_indicator.markdown("### ⚪ STATUS: STANDBY")
#     st.info("Press START to begin live translation.")
#
#     for log in st.session_state.logs:
#         st.markdown(f"""
#         <div class="translation-box">
#             <span style="color:#888;font-size:0.8em;">[{log['time']}]</span><br>
#             <b>🌍 Language:</b> {log['lang']}<br>
#             <b>🗣 Original:</b> {log['original']}<br>
#             <b>🌐 English:</b> {log['translated']}<br>
#             <b>📊 Confidence:</b> {log['confidence']}
#         </div>
#         """, unsafe_allow_html=True)

import streamlit as st
from datetime import datetime
from core.audio_stream import AudioMonitor
from core.transcriber import Transcriber
from core.translator import TextTranslator
from core.audio_utils import split_audio
from core.threat_detector import detect_threat

st.set_page_config(page_title="SENTINEL Dashboard", layout="wide")

st.title("🛡 SENTINEL Intelligence Dashboard")

st.session_state.setdefault("logs", [])

monitor = AudioMonitor()
transcriber = Transcriber()
translator = TextTranslator()

tab1, tab2 = st.tabs(["🎙 Live Translation", "📂 Audio Upload Analysis"])

# ---------------- LIVE MODE ----------------
with tab1:
    st.subheader("Push-to-Talk Translation")

    if st.button("🎤 Record 3 Seconds"):
        audio_data = monitor.record()
        audio_file = monitor.save_audio(audio_data)

        text, lang = transcriber.transcribe(audio_file)
        translated = translator.translate(text)
        threats = detect_threat(translated)

        st.session_state.logs.insert(0, {
            "time": datetime.now().strftime("%H:%M:%S"),
            "text": text,
            "translated": translated,
            "threats": threats,
            "audio": audio_file
        })

# ---------------- UPLOAD MODE ----------------
with tab2:
    uploaded = st.file_uploader("Upload audio file", type=["wav", "mp3"])
    if uploaded:
        with open("uploaded.wav", "wb") as f:
            f.write(uploaded.read())

        st.info("Splitting audio into segments...")
        segments = split_audio("uploaded.wav")

        for seg in segments:
            text, lang = transcriber.transcribe(seg)
            translated = translator.translate(text)
            threats = detect_threat(translated)

            st.session_state.logs.insert(0, {
                "time": datetime.now().strftime("%H:%M:%S"),
                "text": text,
                "translated": translated,
                "threats": threats,
                "audio": seg
            })
st.write("Upload section loaded")

# ---------------- DISPLAY ----------------
st.subheader("📋 Intelligence Feed")

for log in st.session_state.logs[:20]:
    color = "red" if log["threats"] else "#3498db"
    st.markdown(f"""
    <div style="border-left:5px solid {color}; padding-left:12px; margin-bottom:10px;">
        <b>[{log['time']}]</b><br>
        <b>Original:</b> {log['text']}<br>
        <b>English:</b> {log['translated']}<br>
        <b>Threat Words:</b> {", ".join(log['threats']) if log['threats'] else "None"}
    </div>
    """, unsafe_allow_html=True)

    st.audio(log["audio"])
