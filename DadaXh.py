#!/usr/bin/env python3
import warnings
warnings.filterwarnings("ignore")  # Faaltu ke warnings ko chup karao

from rich.markdown import Markdown
from modules.ui import console, print_banner
from modules.brain import init_brain
from modules.audio import speak
from modules.automation import execute_command
from modules.memory import init_db, save_interaction, load_history
from modules.listen import listen

# --- CHAT LOOP (Baat-cheet shuru) ---
def start_chat():
    # 1. Memory Initialize karo
    init_db()
    old_chat = load_history(limit=50) # Ab pichle 50 messages yaad rakhega (Free hai!)
    
    # 2. Brain Initialize karo (Purani yaadein dekar)
    chat_session = init_brain(history_data=old_chat)
    
    # Welcome Banner Print karo
    print_banner()

    while True:
        try:
            # 1. Voice Input Try karo
            try:
                user_input = listen()
            except KeyboardInterrupt:
                # Agar user Ctrl+C dabaye mic ke time, to text mode pe jao
                user_input = None
            
            # 2. Agar Voice fail hui (Silence/Noise), to Text Input lo
            if not user_input:
                user_input = console.input("\n[bold cyan]⌨️  Likh ke bata (Mic fail):[/bold cyan] ")
            
            # Exit commands check karo
            if user_input.lower() in ['exit', 'quit', 'bye', 'bhaag']:
                console.print("[yellow]Connection Terminated. 👋[/yellow]")
                speak("Connection Terminated. Good luck Boss.")
                break
            
            if not user_input.strip(): continue  # Agar khali enter dabaya to skip karo

            # AI se response mango (Loading animation ke saath)
            with console.status("[bold green]Decrypting Request...[/bold green]", spinner="dots"):
                response = chat_session.send_message(user_input)

            # --- JARVIS LOGIC (Command vs Text) ---
            response_text = response.text
            cmd = None
            
            # Check karo agar AI ne koi command execute karne ko bola hai
            if "[EXECUTE]:" in response_text:
                parts = response_text.split("[EXECUTE]:")
                response_text = parts[0].strip()  # Ye bolne wala text hai
                
                # --- COMMAND CLEANING (Robust) ---
                cmd = parts[1].strip()
                cmd = cmd.replace("```", "").replace("`", "")  # Markdown hatao
                # Agar command quotes mein hai ("cmd" ya 'cmd'), to unhe hatao
                if (cmd.startswith("'") and cmd.endswith("'")) or (cmd.startswith('"') and cmd.endswith('"')):
                    cmd = cmd[1:-1]
                cmd = cmd.strip()

            console.print("\n[bold purple]👾 DadaXh:[/bold purple]")
            console.print(Markdown(response_text))

            console.print("[dim italic]🔊 Speaking...[/dim italic]")
            clean_text = response_text.replace("*", "").replace("#", "").replace("`", "")  # Special chars hatao bolne ke liye
            speak(clean_text)
            
            # --- MEMORY SAVE ---
            save_interaction(user_input, response_text)
            
            # Agar command thi, to ab run karo
            if cmd:
                execute_command(cmd)

        except KeyboardInterrupt:
            console.print("\n[yellow]\nSession Interrupted.[/yellow]")
            break
        except Exception as e:
            console.print(f"[bold red]❌ Error:[/bold red] {e}")

if __name__ == "__main__":
    start_chat()