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


        Widget:
            size_hint_y: None
            height: dp(50)
        GridLayout:
            rows: 4
            cols: 4
            size_hint: None, None
            width: self.minimum_width
            height: self.minimum_height
            pos_hint: {'center_x': 0.5, 'y': 0.3}
            padding: dp(24)
            spacing: dp(24)
            x: self.parent.x + dp(80)
            MDIconButton:
                icon: 'thermostat'
                user_font_size: '64dp'
                halign: 'center'
                on_release: app.button_pressed('Comfort Profiles', 'thermostat')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(24)
            MDIconButton:
                icon: 'calendar-today'
                user_font_size: '64dp'
                halign: 'center'
                on_release: app.button_pressed('Schedules', 'calendar-today')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(24)
            MDIconButton:
                icon: 'beach'
                user_font_size: '64dp'
                halign: 'center'
                on_release: app.button_pressed('Vacation', 'beach')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(24)
            MDIconButton:
                icon: 'cogs'
                user_font_size: '64dp'
                halign: 'center'
                on_release: app.button_pressed('Settings', 'cogs')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(24)
            MDIconButton:
                icon: 'weather-partly-cloudy'
                user_font_size: '64dp'
                halign: 'center'
                on_release: app.button_pressed('Weather', 'weather-partly-cloudy')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(24)
            MDIconButton:
                icon: 'bell-outline'
                user_font_size: '64dp'
                halign: 'center'
                on_release: app.button_pressed('Alerts & Reminders', 'bell-outline')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(24)
            MDIconButton:
                icon: 'information-outline'
                user_font_size: '64dp'
                halign: 'center'
                on_release: app.button_pressed('System', 'information-outline')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(24)
            MDIconButton:
                icon: 'account-cog-outline'
                user_font_size: '64dp'
                halign: 'center'
                on_release: app.button_pressed('Service', 'account-cog-outline')
                md_bg_color: app.theme_cls.accent_color
                radius: dp(24)
            Widget:
                size_hint_y: None
                height: dp(50)

            

        #footer 
        MDBoxLayout:
            size_hint_y: None
            height: '40dp'
            md_bg_color: app.theme_cls.accent_color

            MDIconButton:
                icon: 'arrow-left'
                user_font_size: '32sp'
                on_release: app.footer_button_pressed('Back', 'arrow-left')
            MDLabel:
                text: 'No new Notifications'
                halign: 'center'
                valign: 'middle'
                theme_text_color: 'Secondary'
                size_hint_x: 0.8
            
            MDIconButton:
                id: mj_button
                user_font_size: '32sp'
                on_release: app.mj_button_pressed()
                radius: dp(24)

            MDIconButton:
                id: recent_button
                icon: app.recent_icon
                user_font_size: '32sp'
                on_release: app.footer_button_pressed('Recent', 'recent_button')
                radius: dp(24)
            
'''


class SmartThermostatApp(MDApp):
    recent_icon = StringProperty('history')
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "LightBlue"
        return Builder.load_string(KV)

    def button_pressed(self, button_text):
        print(f'{button_text} button pressed')

    def footer_button_pressed(self, button_text, next):
        print(f'{button_text} button pressed')
    
    def button_pressed(self, button_text, icon):
        print(f'{button_text} button pressed')
        print(self.recent_icon)
        self.recent_icon = icon

    def mj_button_pressed(self):
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            print("Its light ")
        else:
            self.theme_cls.theme_style = 'Dark'
            print("its dark")
        self.root.clear_widgets()
        self.root.add_widget(Builder.load_string(KV))
        print(" UI has refreshed to apply new theme")



    

if __name__ == '__main__':
    SmartThermostatApp().run()
