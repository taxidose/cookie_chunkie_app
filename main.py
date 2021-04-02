import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainGrid(GridLayout):
    pass


class CookieChunkieApp(App):
    def build(self):
        return MainGrid()

        #return Button(
            #text="Hello", pos=(50, 50), size=(100, 100), size_hint=(None, None))


if __name__ == '__main__':
    CookieChunkieApp().run()
