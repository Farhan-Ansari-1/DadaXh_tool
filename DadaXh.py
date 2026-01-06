#!/usr/bin/env python3
import warnings
warnings.filterwarnings("ignore")  # Faaltu ke warnings ko chup karao

from rich.markdown import Markdown
from modules.ui import console, print_banner
from modules.brain import init_brain
from modules.audio import speak
from modules.automation import execute_command

# --- CHAT LOOP (Baat-cheet shuru) ---
def start_chat():
    # Brain Initialize karo (API Key check modules/config.py me ho jayega)
    chat_session = init_brain()
    
    # Welcome Banner Print karo
    print_banner()

    while True:
        try:
            # User se input lo
            user_input = console.input("\n[bold cyan]💀 farX (You):[/bold cyan] ")
            
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
                cmd = parts[1].strip()            # Ye run karne wala command hai

            console.print("\n[bold purple]👾 DadaXh:[/bold purple]")
            console.print(Markdown(response_text))

            console.print("[dim italic]🔊 Speaking...[/dim italic]")
            clean_text = response_text.replace("*", "").replace("#", "").replace("`", "")  # Special chars hatao bolne ke liye
            speak(clean_text)
            
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