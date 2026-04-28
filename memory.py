import json, os

FILE = "memory.json"

def load_memory():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(user, bot):
    data = load_memory()
    data.append({"user": user, "bot": bot})

    with open(FILE, "w") as f:
        json.dump(data[-10:], f)

def get_context():
    data = load_memory()
    return "\n".join([f"User: {d['user']} Jarvis: {d['bot']}" for d in data])
