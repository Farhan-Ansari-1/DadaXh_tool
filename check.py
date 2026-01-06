import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Key Load karo
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ API Key nahi mili .env mein!")
else:
    # 2. Configure karo
    genai.configure(api_key=api_key)

    print(f"🔍 Checking available models for Key ending in... {api_key[-5:]}")
    print("-" * 40)

    try:
        # 3. Google se list maango
        for m in genai.list_models():
            # Sirf wo models dikhao jo content generate kar sakte hain (Chat wale)
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ Name: {m.name}")
                
    except Exception as e:
        print(f"❌ Error aaya: {e}")