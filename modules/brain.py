import google.generativeai as genai
from modules.config import API_KEY, FARX_INSTRUCTION
from modules.ui import console
import sys

def init_brain(history_data=[]):
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(
            model_name='gemini-2.5-flash', 
            system_instruction=FARX_INSTRUCTION 
        )
        return model.start_chat(history=history_data)
    except Exception as e:
        console.print(f"[bold red]❌ API Error bhai:[/bold red] {e}")
        sys.exit()