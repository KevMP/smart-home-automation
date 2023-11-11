from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty


Window.size = (800, 480)

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'

        MDBoxLayout:
            size_hint_y: None
            height: '70dp'
            MDLabel:
                text: '72°F | 40% Humidity'
                font_style: 'H5'
                halign: 'center'
                valign: 'middle'
                theme_text_color: 'Secondary'
                size_hint_x: 1

        # Icon grid centered
        GridLayout:
            cols: 4
            size_hint: 1, None
            height: self.minimum_height
            padding: dp(24)
            spacing: dp(24)

            # Define buttons
            MDIconButton:
                icon: 'thermostat'
                user_font_size: '48dp'
                on_release: app.button_pressed('Comfort Profiles', 'comfort profiles')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(12)
            MDIconButton:
                icon: 'calendar-today'
                user_font_size: '48dp'
                on_release: app.button_pressed('Schedules', 'schedules')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(12)
            MDIconButton:
                icon: 'beach'
                user_font_size: '48dp'
                on_release: app.button_pressed('Vacation', 'vacation')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(12)
            MDIconButton:
                icon: 'cogs'
                user_font_size: '48dp'
                on_release: app.button_pressed('Settings', 'settings')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(12)
            MDIconButton:
                icon: 'weather-partly-cloudy'
                user_font_size: '48dp'
                on_release: app.button_pressed('Weather', 'weather')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(12)
            MDIconButton:
                icon: 'bell-outline'
                user_font_size: '48dp'
                on_release: app.button_pressed('Alerts & Reminders', 'alerts & reminders')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(12)
            MDIconButton:
                icon: 'information-outline'
                user_font_size: '48dp'
                on_release: app.button_pressed('System', 'system')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(12)
            MDIconButton:
                icon: 'account-cog-outline'
                user_font_size: '48dp'
                on_release: app.button_pressed('Service', 'service')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(12)

        # Fancy Notification bar in the footer
        MDBoxLayout:
            size_hint_y: None
            height: '40dp'
            md_bg_color: app.theme_cls.accent_color

            MDIconButton:
                icon: 'arrow-left'
                user_font_size: '32sp'
                on_release: app.footer_button_pressed('Back')
            MDLabel:
                text: 'No new Notifications'
                halign: 'center'
                valign: 'middle'
                theme_text_color: 'Secondary'
                size_hint_x: 0.8
            
            MDIconButton:
                id: recent_button
                icon: app.recent_icon
                user_font_size: '32sp'
                on_release: app.footer_button_pressed('Recent', 'history')
            
'''

class SmartThermostatApp(MDApp):
    recent_icon = StringProperty('history')
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Teal" 
        return Builder.load_string(KV)

    def button_pressed(self, button_text):
        print(f'{button_text} button pressed')

    def footer_button_pressed(self, button_text):
        print(f'{button_text} button pressed')
    
    def button_pressed(self, button_text, icon):
        print(f'{button_text} button pressed')
        print(self.recent_icon)
        self.recent_icon = icon
    

if __name__ == '__main__':
    SmartThermostatApp().run()
