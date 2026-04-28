from openai import OpenAI
from config import OPENAI_API_KEY
from memory import get_context, save_memory

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_ai(prompt):
    context = get_context()

    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role":"system","content":"You are Jarvis. Always reply in Bangla."},
                {"role":"user","content": context + "\nUser: " + prompt}
            ]
        )

        reply = res.choices[0].message.content
        save_memory(prompt, reply)
        return reply

    except Exception as e:
        return "Error: " + str(e)
