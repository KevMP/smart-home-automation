from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel

Window.size = (800, 480)

<<<<<<< Updated upstream
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


=======
>>>>>>> Stashed changes
class SmartThermostatApp(MDApp):
    recent_icon = StringProperty('history')
    mj_icon = StringProperty('moon-full')
    #notification_text = StringProperty('No New Notifications')
    #def update_notification(self, new_message):
        #self.notification_text = new_message

    file_path = 'local-gui\main.kv'

    def build(self):
        layout = BoxLayout(orientation='vertical')
        notification_bar = NotificationBar()
        layout.add_widget(notification_bar)
        layout.add_widget(Builder.load_file(self.file_path))
        self.theme_cls.theme_style_switch_animation = 0.8
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "LightBlue"
        return Builder.load_file(self.file_path)

    def footer_button_pressed(self, button_text, next):
        print(f'{button_text} button pressed')
    
    def button_pressed(self, button_text, icon):
        print(f'{button_text} button pressed')
        print(self.recent_icon)
        self.recent_icon = icon
    
    def on_start(self):
        self.fps_monitor_start()

    # These two functions handle the theme setting functionality and the "Sun" to "Moon" icon 
    def mj_button_pressed(self):
        #checking if the theme is dark
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            self.mj_icon = 'weather-sunny'
            self.root.clear_widgets()
            self.root.add_widget(Builder.load_file(self.file_path))
        else:
            self.theme_cls.theme_style = 'Dark'
            self.mj_icon = 'moon-full'
            self.root.clear_widgets()
            self.root.add_widget(Builder.load_file(self.file_path))
            print(" UI has refreshed to apply new theme")
        
class NotificationBar(BoxLayout):
    def __init__(self, **kwargs):
        super(NotificationBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 40  # Adjust as necessary
        self.notification_label = MDLabel(size_hint_y=None, height=self.height,
                                          halign="center", valign="middle")
        self.add_widget(self.notification_label)
        self.messages = ["Welcome", "AC Unit Running Smoothly", "Filter Needs Replacement"]
        self.current_message = 0
        self.animate_notification()


    def animate_notification(self):
        message = self.messages[self.current_message]
        self.notification_label.text = message
        self.current_message = (self.current_message + 1) % len(self.messages)
        anim = Animation(opacity=0, duration=2) + Animation(opacity=1, duration=2)
        anim.bind(on_complete=self.on_animation_complete)
        anim.start(self.notification_label)

    def on_animation_complete(self, *args):
        self.animate_notification()
    
    def update_notification(self, message):
        self.notification_label.text = message

if __name__ == '__main__':
    SmartThermostatApp().run()
