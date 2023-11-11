from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.properties import NumericProperty

Window.size = (800, 480)

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

<IconButton>:
    font_size: '16dp'
    size_hint: None, None
    size: '150dp', '150dp'
    # Placeholder for icon image
    canvas.before:
        Color:
            rgba: get_color_from_hex('#ffffff')
        Rectangle:
            size: self.size
            pos: self.pos
            source: 'path/to/icon.png'

<ClearButton@Button>:
    background_normal: ''
    background_color: (1, 1, 1, 0)  # RGBA: Fully transparent
    color: get_color_from_hex('#FFFFFF')
    size_hint: None, None
    size: '120dp', '40dp'
    font_size: '18dp'

BoxLayout:
    orientation: 'vertical'
    padding: '20dp'
    spacing: '20dp'
    canvas.before:
        Color:
            rgba: get_color_from_hex('#000000')
        Rectangle:
            pos: self.pos
            size: self.size

    GridLayout:
        cols: 4
        size_hint_y: None
        height: self.minimum_height
        spacing: '20dp'
        
        IconButton:
            text: 'Custom Profiles'
            on_release: app.button_pressed('Custom Profiles')
        IconButton:
            text: 'Schedules'
            on_release: app.button_pressed('Schedules')
        IconButton:
            text: 'Vacation'
            on_release: app.button_pressed('Vacation')
        IconButton:
            text: 'Settings'
            on_release: app.button_pressed('Settings')
        IconButton:
            text: 'Weather'
            on_release: app.button_pressed('Weather')
        IconButton:
            text: 'Alerts and reminders'
            on_release: app.button_pressed('Alerts and reminders')
        IconButton:
            text: 'System'
            on_release: app.button_pressed('System')
        IconButton:
            text: 'Service'
            on_release: app.button_pressed('Service')

    BoxLayout:
        size_hint_y: None
        height: '1dp'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1  # White color
            Rectangle:
                pos: self.pos
                size: self.size

    BoxLayout:
        size_hint_y: None
        height: '60dp'
        ClearButton:
            text: 'Back'
            on_release: app.footer_button_pressed('Back')
        Widget:
            size_hint_x: 1
        ClearButton:
            text: 'Home'
            on_press: root.start_animation()
            size: '140dp', '50dp'
            font_size: '22dp'
            on_release: app.go_to_home()

        Widget:
            size_hint_x: 1
        ClearButton:
            text: 'Done'
            on_release: app.footer_button_pressed('Done')
'''


class MyAnimationApp(App):
    index = NumericProperty(0) #keeping track of current frame
    print(index)
    max_index = 27 

    def build(self):
        self.root = Builder.load_string(KV)
        return self.root
    
    def animate(self, dt):
        self.index += 1
        if self.index > self.max_index:
            self.index = 0 # reset 
            print("im working!")
        self.root.ids.gif.source = f'frame_{self.index}.png'

    def start_anim(self):
        Clock.schedule_interval(self.animate, 0.1)
        print("Im working!")

class IconButton(ButtonBehavior, Label):
    pass

class SmartThermostatApp(App):
    def build(self):
        return Builder.load_string(KV)

    def button_pressed(self, button_text):
        print(f'{button_text} button pressed')

    def footer_button_pressed(self, button_text):
        print(f'{button_text} button pressed')

    def go_to_home(self):
        print('Home button pressed')

if __name__ == '__main__':
    SmartThermostatApp().run()
