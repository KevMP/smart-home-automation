from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.icon_definitions import md_icons

Window.size = (360, 640)

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    spacing: dp(8)
    size_hint_y: None
    height: self.minimum_height

    MDBoxLayout:
        size_hint_y: None
        height: dp(48)
        padding: dp(24), dp(8), dp(24), dp(8)

        MDLabel:
            text: 'Smart Home'
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: self.texture_size[1]
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color

    MDGridLayout:
        cols: 3
        size_hint_y: None
        height: self.minimum_height
        padding: dp(24), dp(8), dp(24), dp(8)
        spacing: dp(8)

        MDIconButton:
            icon: 'fan'
            user_font_size: '48sp'
            on_release: app.open_smart_vents()
            md_bg_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            ripple_color: app.theme_cls.accent_light

        MDIconButton:
            icon: 'air-conditioner'
            user_font_size: '48sp'
            on_release: app.view_ac_status()
            md_bg_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            ripple_color: app.theme_cls.accent_light

        MDIconButton:
            icon: 'cog-outline'
            user_font_size: '48sp'
            on_release: app.open_settings()
            md_bg_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            ripple_color: app.theme_cls.accent_light
'''

class SmartHomeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'  # Set your primary theme color here
        self.theme_cls.accent_palette = 'Amber'  # Set your accent color here
        self.theme_cls.theme_style = 'Dark'  # Choose between 'Light' or 'Dark'
        return Builder.load_string(KV)

    def open_smart_vents(self):
        print("Opening Smart Vents...")

    def view_ac_status(self):
        print("Viewing AC Status...")

    def open_settings(self):
        print("Opening Settings...")

SmartHomeApp().run()
