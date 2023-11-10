from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color
from kivy.graphics import Line 
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import NumericProperty, ListProperty
from kivy.graphics import Color, Line
from kivy.metrics import dp

Window.size = (800, 480)

KV = '''
BoxLayout:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

    MDFloatLayout:
        md_bg_color: 1, 0, 100/255, .1
    CircularProgressBar:  # Make sure this matches the name in your Python code
        size_hint: None, None
        size: dp(200), dp(200)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        bar_color: 1, 0, 0  # Change as needed
        bar_width: dp(10)
        temperature: 75  # Example temperature

    # Filler widget for spacing
    Widget:
        size_hint_y: None
        height: dp(48)

    # Centered grid of buttons
    GridLayout:
        cols: 4
        size_hint_y: None
        height: self.minimum_height
        size_hint_x: None
        width: self.minimum_width
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        padding: dp(10)
        spacing: dp(10)
        
        # First row of buttons
        MDFillRoundFlatButton:
            text: "Profile"
            on_release: app.on_profile()
        MDFillRoundFlatButton:
            text: "AI"
            on_release: app.on_ai()
        MDFillRoundFlatButton:
            text: "Alerts"
            on_release: app.on_alerts_messages()
        MDFillRoundFlatButton:
            text: "Service"
            on_release: app.on_service()
        
        # Second row of buttons
        MDFillRoundFlatButton:
            text: "Settings"
            on_release: app.on_settings()
        MDFillRoundFlatButton:
            text: "Weather"
            on_release: app.on_weather()
        MDFillRoundFlatButton:
            text: "System"
            on_release: app.on_system()
        MDFillRoundFlatButton:
            text: "Schedules"
            on_release: app.on_schedules()

    # Filler widget for spacing
    Widget:
        size_hint_y: None
        height: dp(48)

    # Separator line
    MDBoxLayout:
        size_hint_y: None
        height: "1dp"
        md_bg_color: app.theme_cls.divider_color

    # Footer with 'Back', 'Info', and 'Done' buttons
    MDBoxLayout:
        size_hint_y: None
        height: dp(69)
        MDFlatButton:
            text: "Back"
            pos_hint: {'center_y': 0.5}
            on_release: app.on_back()
        Widget:
        MDIconButton:
            icon: "information-outline"
            pos_hint: {'center_x': 0.5}
            on_release: app.on_info()
        Widget:
        MDFlatButton:
            text: "Done"
            pos_hint: {'center_y': 0.5}
            on_release: app.on_done()
'''
class CircularProgressBar(AnchorLayout):
    bar_color = ListProperty([1, 0, 0])  # Initial color: red
    bar_width = NumericProperty(10)
    temperature = NumericProperty(0)  # Default temperature

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        self.bind(temperature=self.update_progress)

    def update_progress(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bar_color, 1)  # Set the color for the progress bar
            Line(circle=(self.center_x, self.center_y, dp(100)), width=self.bar_width, angle_end=(self.temperature * 360) / 100)

def __init__(self, **kwargs):
    super(CircularProgressBar, self).__init__(**kwargs)
    self.bind(temperature=self.update_progress)

class SmartHomeApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_profile(self):
        print("Profile button pressed")

    def on_ai(self):
        print("AI button pressed")

    def on_alerts_messages(self):
        print("Alerts & Messages button pressed")

    def on_service(self):
        print("Service button pressed")

    def on_settings(self):
        print("Settings button pressed")

    def on_weather(self):
        print("Weather button pressed")

    def on_system(self):
        print("System button pressed")

    def on_schedules(self):
        print("Schedules button pressed")

    def on_back(self):
        print("Back button pressed")

    def on_info(self):
        print("Info button pressed")

    def on_done(self):
        print("Done button pressed")

if __name__ == '__main__':
    SmartHomeApp().run()
