import edge_tts
import asyncio
import os
import platform
from modules.ui import console

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

async def generate_audio(text):
    communicate = edge_tts.Communicate(text, "en-IN-PrabhatNeural", rate="+25%")
    await communicate.save("voice.mp3")

def speak(text):
    try:
        asyncio.run(generate_audio(text))
        if platform.system() == "Windows":
            import pygame
            pygame.mixer.init()
            pygame.mixer.music.load("voice.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.quit()
        else:
            os.system("mpg123 -q voice.mp3 > /dev/null 2>&1")
    except Exception as e:
        console.print(f"[red]Voice Error: {e}[/red]")