
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDFlatButton

from kivymd.uix.label import MDLabel #importing for text
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager   #import screen for managing screen
import pyttsx3
engine=pyttsx3.init()


class DemoApp(MDApp):
    engine=pyttsx3.init()

    def build(self):

        self.theme_cls.theme_style="Dark"
        screen=Builder.load_file("demo.kv")
        return screen


    def speak(self):
        self.engine.save_to_file(self.root.ids.text.text, "voice.mp3")
        self.engine.runAndWait()

    def demo(self):
        self.engine.say(self.root.ids.text.text)
        self.engine.runAndWait()
if __name__ == '__main__':
    DemoApp().run()
