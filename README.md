Jarvis is a Python-powered voice assistant that listens, speaks, and executes commands 
it wakes up after hearing the code word "Jarvis"....don' try to enter wrong code word or it will hack your system.
it can open any browser, search things in Youtube,
it does basic tasks for now and soon will rule upon us 

# features
- Speech Recognition using speech_recognition
- Text-to-Speech with pyttsx3
- Web Automation via webbrowser
- Custom Activation Sounds (MP3 beeps)
- Smart Command Loop with timeout and fallback logic
- Device Selection & Audio Routing
- integrated with GOOGLE_GEMINI for real-time response
- Built for experimentation, personalisation, and fun!

# Installation
git clone https://github.com/syed/Jarvis.git
cd Jarvis
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

Make sure your microphone and speakers are configured properly.

# How to Use
- Run the main script:
python jarvis.py
- Say the wake word (e.g. "Jarvis")
- Speak your command (e.g. "Open YouTube")
- Jarvis responds and executes your request
- After some seconds of silence, it exits gracefully

🧩 Customization
- Change the assistant name in jarvis.py for better speech recognition
- Add new commands in the process_command() function
- Modify voice settings in pyttsx3.init() for pitch, rate, and gender
- Replace activation sounds with your own MP3s

📦 Dependencies
- speech_recognition
- pyttsx3
- webbrowser
- pygame (for sound playback)
- python-dotenv (for secure config)

🧠 Future Plans
- Add GUI interface (Tkinter or PyQt)
- Integrate with APIs (weather, openai, etc.) - done integrating with Google Gemini on 16 of sep
- Push to GitHub Pages or Streamlit for demo
- add new songs to music.lib

# Contributing
Pull requests are welcome! If you have ideas, bug fixes, or want to add new features, feel free to fork and submit.

