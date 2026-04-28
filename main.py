from kivy.app import App
from kivy.lang import Builder

from brain import ask_ai
from voice import speak
from mic import listen
from app_control import open_app

class JarvisApp(App):

    def build(self):
        self.ui = Builder.load_file("jarvis.kv")
        return self.ui

    def run_ai(self):
        self.ui.ids.output_text.text = "শুনছি..."

        query = listen()

        if not query:
            self.ui.ids.output_text.text = "কিছু বুঝতে পারিনি 😅"
            return

        # App control
        if any(app in query for app in ["youtube","facebook","whatsapp","messenger","chrome"]):
            result = open_app(query)
            self.ui.ids.output_text.text = result
            speak(result)
            return

        # AI response
        response = ask_ai(query)
        self.ui.ids.output_text.text = response
        speak(response)

JarvisApp().run()
