from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


Builder.load_file("layout_exemples.kv")


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
