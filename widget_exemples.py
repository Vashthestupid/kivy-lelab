from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_file("widget_exemples.kv")

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