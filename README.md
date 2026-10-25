# Nova Voice Assistant 🎙️

An interactive voice assistant built in Python that listens to voice commands, provides text-to-speech feedback, opens apps/websites, tracks dates/time, and includes wake/sleep commands.

## ✨ Features
* **Wake Word Activation:** Toggle active state using the wake word `"nov"`.
* **Voice Control & Audio Feedback:** Uses streaming speech recognition and offline SAPI5 text-to-speech.
* **App Launcher:** Direct desktop integration for system utilities and application URI schemes like WhatsApp.
* **Smart Browser Automation:** Integrated with Google Chrome to auto-navigate common handles and web searches.

## 📋 Requirements
* Python 3.10 or later
* Active internet connection (required for Google Web Speech API transcription)
* PyAudio (system dependency for microphone access)

## 🚀 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Nova-Voice-Assistant.git
   cd Nova-Voice-Assistant
   ```

2. **Configure App Paths:**
   Ensure `CHROME_PATH` inside `nova_assistant.py` accurately points to your local Google Chrome installation executable.

3. **Run Environment Setup:**
   On Windows, double-click `setup.bat` to automatically build your virtual environment and install tracking components. Alternatively, manage dependencies manually:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Launch the Engine:**
   ```bash
   python nova_assistant.py
   ```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
