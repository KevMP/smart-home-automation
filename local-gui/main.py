from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Directly loading KV string
kv_code = """
BoxLayout:
    orientation: 'vertical'
    padding: '20dp'
    spacing: '20dp'
    canvas.before:
        Color:
            rgba: [0, 0, 0, 1]
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: 'Smart Home'
        font_size: '32sp'
        size_hint_y: 0.2
        color: [1, 1, 1, 1]

    GridLayout:
        cols: 3
        spacing: '20dp'
        size_hint_y: 0.7

        Button:
            text: '[size=24sp]⬢[/size]Smart Vents'
            font_size: '16sp'
            markup: True
            background_normal: ''
            background_color: [0.5, 0.5, 0.5, 1]
            on_press: root.open_smart_vents()

        Button:
            text: '[size=24sp]⬣[/size]Smart AC'
            font_size: '16sp'
            markup: True
            background_normal: ''
            background_color: [0.5, 0.5, 0.5, 1]
            on_press: root.view_ac_status()

        Button:
            text: '[size=24sp]⚙[/size]Settings'
            font_size: '16sp'
            markup: True
            background_normal: ''
            background_color: [0.5, 0.5, 0.5, 1]
            on_press: root.open_settings()
"""

Builder.load_string(kv_code)

class SmartHomeRemote(BoxLayout):
    def open_smart_vents(self):
        print("Opening Smart Vents...")

    def view_ac_status(self):
        print("Viewing AC Status...")

    def open_settings(self):
        print("Opening Settings...")

class SmartHomeApp(App):
    def build(self):
        return SmartHomeRemote()

if __name__ == '__main__':
    SmartHomeApp().run()
