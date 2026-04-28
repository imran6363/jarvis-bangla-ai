import os

APPS = {
    "youtube": "com.google.android.youtube",
    "facebook": "com.facebook.katana",
    "whatsapp": "com.whatsapp",
    "messenger": "com.facebook.orca",
    "chrome": "com.android.chrome"
}

def open_app(query):
    query = query.lower()

    for name, package in APPS.items():
        if name in query:
            os.system(f"am start -n {package}/.MainActivity")
            return f"{name} খুলছি 🚀"

    return "App পাওয়া যায়নি 😅"
