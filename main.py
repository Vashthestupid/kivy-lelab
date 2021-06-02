from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp


class WidgetExemple(GridLayout):
    mon_texte = StringProperty("1")
    compteur_actif = BooleanProperty(False)
    compteur = 1
    # slider_value_txt = StringProperty("O")
    text_input_str = StringProperty("toto")

    def on_button_click(self):
        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte = str(self.compteur)

    def on_toggle_button_state(self, toggle_button):
        if toggle_button.state == "normal":
            print("OFF")
            toggle_button.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            toggle_button.text = "ON"
            self.compteur_actif = True

    def on_switch_active(self, switch):
        print("Switch" + " " + str(switch.active))

    def on_text_validate(self, text):
        self.text_input_str = text.text


class MainWidget(Widget):
    pass


class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-tb"
        for i in range(0,100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


class AnchorLayoutExemple(AnchorLayout):
    pass


class GridLayoutExemple(GridLayout):
    pass


class BoxLayoutExemple(BoxLayout):
    pass
    """    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        self.add_widget(b1)
        b2 = Button(text="Hi Guy")
        self.add_widget(b2)
        b3 = Button(text="BIIIIIIIIP")
        self.add_widget(b3)"""


class LelabApp(App):
    pass


LelabApp().run()