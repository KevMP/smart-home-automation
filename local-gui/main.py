from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp

Window.size = (800, 480)

KV = '''
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        
        Widget:
            size_hint_y: None
            height: self.parent.height * 0.2

        MDGridLayout:
            cols: 4
            size_hint: None, None
            size: self.minimum_size
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            spacing: dp(24)
            padding: dp(24)

            MDIconButton:
                icon: 'thermostat'
                user_font_size: '96sp' 
                on_release: app.button_pressed('Comfort Profiles')
            MDIconButton:
                icon: 'calendar-today'
                user_font_size: '96sp'
                on_release: app.button_pressed('Schedules')
            MDIconButton:
                icon: 'beach'
                user_font_size: '96sp'
                on_release: app.button_pressed('Vacation')
            MDIconButton:
                icon: 'cogs'
                user_font_size: '96sp'
                on_release: app.button_pressed('Settings')
            MDIconButton:
                icon: 'weather-partly-cloudy'
                user_font_size: '96sp'
                on_release: app.button_pressed('Weather')
            MDIconButton:
                icon: 'bell-outline'
                user_font_size: '96sp'
                on_release: app.button_pressed('Alerts & Reminders')
            MDIconButton:
                icon: 'information-outline'
                user_font_size: '96sp'
                on_release: app.button_pressed('System')
            MDIconButton:
                icon: 'account-cog-outline'
                user_font_size: '96sp'
                on_release: app.button_pressed('Service')

        # Bottom Spacer - reduced to take less space
        Widget:
            size_hint_y: None
            height: self.parent.height * 0.2

    MDBoxLayout:
        size_hint_y: None
        height: '60dp'
        padding: dp(8)
        MDIconButton:
            icon: 'arrow-left'
            user_font_size: '48sp'
            on_release: app.footer_button_pressed('Back')
        MDLabel:
            text: 'Temperature: 72°F | Humidity: 40%'
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_style: 'H5'
            size_hint_x: None
            width: self.texture_size[0] + dp(48)
'''

class SmartThermostatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # will change to light if it looks better
        return Builder.load_string(KV)

    def button_pressed(self, button_text):
        print(f'{button_text} button pressed')

    def footer_button_pressed(self, button_text):
        print(f'{button_text} button pressed')

if __name__ == '__main__':
    SmartThermostatApp().run()
