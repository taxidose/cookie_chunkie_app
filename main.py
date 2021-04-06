import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


class MainWindow(Screen):
    pass


class InfoWindow(Screen):
    pass


class BaukastenWindow(Screen):
    ingredients = []

    def add_ingredient(self, ingredient):
        if self.ingredients.count(ingredient) < 2:
            self.ingredients.append(ingredient)
        #else:


        print(self.ingredients)

    def delete_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def clear_ingredients(self):
        self.ingredients.clear()

    def logout_baukasten(self):
        logut_popup(self.ingredients)


class WindowManager(ScreenManager):
    pass


def logut_popup(ingredients):
    ingredients_string = ""
    for i in ingredients:
        ingredients_string += i + " "

    layout = GridLayout(cols=1, padding=10)
    popupLabel = Label(text=ingredients_string + "Cookie")
    closeButton = Button(text="Close the pop-up")

    layout.add_widget(popupLabel)
    layout.add_widget(closeButton)

    pop = Popup(title="Dein Cookie", content=layout)

    pop.open()

    closeButton.bind(on_press=pop.dismiss)


kv = Builder.load_file("cookiechunkie.kv")


class CookieChunkieApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    CookieChunkieApp().run()
