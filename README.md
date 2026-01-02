# 👾 DadaXh - AI Hacking Assistant (CLI)

**DadaXh** is a powerful, voice-activated AI assistant designed for **Ethical Hackers, Developers, and Students**. It runs directly in your terminal, providing instant coding help, hacking concepts, and project assistance with a unique "Hacker Persona".

Powered by **Google Gemini AI** and **Edge TTS** (Natural Voice).

---

## 🚀 Features

- **🧠 Smart AI Brain:** Powered by Google's Gemini Flash model for fast and accurate technical answers.
- **🗣️ Natural Voice Output:** Speaks responses using a high-quality Indian Male voice (Edge TTS).
- **💀 Hacker Persona:** Optimized to teach Ethical Hacking & Python concepts simply (Urdu/Hindi medium friendly).
- **🔒 Secure:** Uses `.env` variables to keep API keys safe.
- **🎨 Beautiful UI:** Rich text formatting (Bold, Tables, Code Blocks) in the terminal.
- **📱 Cross-Platform:** Works on **Kali Linux**, **Windows**, and **Android (Termux)**.

---

## 🛠️ Installation

### 1. Clone the Repository
Open your terminal and download the tool:
```bash
git clone [https://github.com/Farhan-Ansari-1/DadaXh_tool.git](https://github.com/Farhan-Ansari-1/DadaXh_tool.git)
cd DadaXh_tool

2. Install Dependencies

Make sure you have Python installed. Then run:
Bash

pip install -r requirements.txt

(Linux/Termux Users: You also need an audio player)
Bash

sudo apt install mpg123 -y   # For Kali/Ubuntu
pkg install mpg123 -y        # For Termux

3. Setup API Key (Important!) 🔑

You need a Google Gemini API Key.

    Get your key from Google AI Studio.

    Create a .env file in the project folder:
    Bash

nano .env

Add your key inside the file (No spaces, no quotes):
Plaintext

    GEMINI_API_KEY=Your_Secret_Key_Here

    Note: Never share your .env file.

⚡ Usage

Run the tool simply by typing:
Bash

python DadaXh.py

Pro Tip (Create a Shortcut)

Add this to your .zshrc or .bashrc to run it from anywhere by typing dadaxh:
Bash

echo "alias dadaxh='cd ~/DadaXh_tool && python DadaXh.py'" >> ~/.zshrc
source ~/.zshrc

🛡️ Disclaimer

DadaXh is strictly for Educational Purposes. This tool is designed to assist in learning Ethical Hacking and Cybersecurity. The author (@Farhan-Ansari-1) is not responsible for any misuse of the information provided by this AI. Always have permission before testing any system.
👨‍💻 Author

Farhan Ansari (farX)

    Cybersecurity Enthusiast & BSc IT Student
