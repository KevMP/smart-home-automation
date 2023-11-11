from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (800, 400)

class PreSplashScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class TestScreen(Screen):
    pass


navigation_history = ()

def back_button_pressed(self):
    # Check what we have in history
    if len(self.navigation_history) > 1:
        # Test print: show the current navigation history
        print("Current navigation history: " + str(self.navigation_history))
        # Remove the current screen that we are on
        self.navigation_history.pop()
        # Access the previous screen in the list
        previous_screen = self.navigation_history[-1]
        # Switch to the previous screen without adding it to history
        self.screen_manager.current = previous_screen
    else:
        print("No previous screen to return to.")


class RegisterPage(MDApp):
    title = "test"

    def build(self):
        # lets make sure we are adding a new screen if its not a back action
        if self.screen_manager.current != screen_name:
            self.navigation_history.append(screen_name)
        self.screen_manager.current = screen_name
        # Load the content of the .kv files
        Builder.load_file("pre-splash.kv")
        Builder.load_file("register.kv")

        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(PreSplashScreen(name='PreSplash'))
        self.screen_manager.add_widget(RegisterScreen(name='Register'))
        self.screen_manager.add_widget(TestScreen(name=''))

        return self.screen_manager

if __name__ == "__main__":
    RegisterPage().run()
