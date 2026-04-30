from openai import OpenAI
from config import OPENAI_API_KEY
from memory import get_context, save_memory

client = OpenAI(api_key=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)

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
