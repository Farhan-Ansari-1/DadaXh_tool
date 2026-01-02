#!/usr/bin/env python3
import warnings
warnings.filterwarnings("ignore")

import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
import edge_tts
import asyncio
import os
import sys
import random
import platform
from dotenv import load_dotenv  # <--- Ye library secret file padhegi

# --- 🔒 SECURITY UPGRADE ---
load_dotenv()  # Ye .env file ko dhundega
API_KEY = os.getenv("GEMINI_API_KEY")  # Ye us file se key uthayega

# Agar Key nahi mili to tool band ho jayega (Safety First)
if not API_KEY:
    print("\n❌ Error: API Key nahi mili!")
    print("👉 Solution: '.env' file bana aur usme GEMINI_API_KEY daal.")
    sys.exit()

console = Console()

# ... (Iske niche ka puraana code waise hi rehne de) ...

# --- BRAIN SETUP (Hacking Focus) ---
try:
    genai.configure(api_key=API_KEY)
    
    # Updated Instruction: Focus is on LEARNING HACKING now
    FARX_INSTRUCTION = """
    IDENTITY:
    Tera naam DadaXh hai. Tu farX (user) ka Hacking Mentor aur Coding Partner hai.

    USER PROFILE (farX):
    - **Goal:** Master Ethical Hacking & Python.
    - **Current Level:** Student (BSc IT), Learning Basics of Linux/Networking.
    - **Background:** Urdu Medium (Concepts ko simple, desi examples ke saath samjha).
    - **Project:** fXtooR (Sirf context ke liye yaad rakh, main focus Hacking sikhane pe hai).

    YOUR BEHAVIOR:
    1. **Tone:** Hacker, Underground vibe, "Boss/ya usse better" address kar.
    2. **Strictness:** Agar farX galat raaste pe ja raha hai (Script Kiddie ban raha hai), to usse rok aur sahi concept samjha.
    3. **Teaching Style:**
       - Theory kam, Practical zyada.
       - Code dene se pehle Logic bata.
       - Har technical term ko tod-tod ke samjha.
    
    4. **FORMATTING:**
       - **Bold** key terms.
       - `Code Blocks` for commands.
       - *Bullet Points* for steps.
    """

    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash', 
        system_instruction=FARX_INSTRUCTION 
    )

except Exception as e:
    console.print(f"[bold red]❌ API Error bhai:[/bold red] {e}")
    sys.exit()

async def generate_audio(text):
    # rate='+25%' ka matlab hai 25% tezi se bolega
    communicate = edge_tts.Communicate(text, "en-IN-PrabhatNeural", rate="+25%")
    await communicate.save("voice.mp3")

def speak(text):
    try:
        asyncio.run(generate_audio(text))
        os.system("mpg123 -q voice.mp3 > /dev/null 2>&1")
    except Exception as e:
        console.print(f"[red]Voice Error: {e}[/red]")

# --- RANDOM STARTUP MESSAGES ---
def get_startup_message():
    # Ye list mein se har baar ek alag line chunega
    messages = [
        "System Breach Detected... Welcome Boss.",
        "Neural Link Established. Ready to Hack.",
        "Establishing Secure Connection... Done.",
        "Protocol 0x99 Initiated. Waiting for Command.",
        "Mainframe Access Granted. Bolo kya karna hai?",
        "Security Shields Down. DadaXh is Online.",
        "Knowledge Database Loaded. Let's Learn.",
        "Connecting to the Matrix... Success."
    ]
    subtitles = [
        "[red]Red Team Mode[/red]",
        "[cyan]Learning Protocol[/cyan]",
        "[green]System: Online[/green]",
        "[yellow]Root Access: Granted[/yellow]"
    ]
    return random.choice(messages), random.choice(subtitles)

# --- CHAT LOOP ---
def start_chat():
    chat_session = model.start_chat(history=[])
    
    # Get Random Message
    msg, sub = get_startup_message()
    
    console.print(Panel.fit(
        f"[bold green]👾 {msg}[/bold green]", 
        border_style="green",
        subtitle=sub
    ))

    while True:
        try:
            user_input = console.input("\n[bold cyan]💀 farX (You):[/bold cyan] ")
            
            if user_input.lower() in ['exit', 'quit', 'bye', 'bhaag']:
                console.print("[yellow]Connection Terminated. 👋[/yellow]")
                speak("Connection Terminated. Good luck Boss.")
                break
            
            if not user_input.strip(): continue

            with console.status("[bold green]Decrypting Request...[/bold green]", spinner="dots"):
                response = chat_session.send_message(user_input)

            console.print("\n[bold purple]👾 DadaXh:[/bold purple]")
            console.print(Markdown(response.text))

            console.print("[dim italic]🔊 Speaking...[/dim italic]")
            clean_text = response.text.replace("*", "").replace("#", "").replace("`", "")
            speak(clean_text)

        except KeyboardInterrupt:
            console.print("\n[yellow]\nSession Interrupted.[/yellow]")
            break
        except Exception as e:
            console.print(f"[bold red]❌ Error:[/bold red] {e}")

if __name__ == "__main__":
    start_chat()