import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager

# Importing the screens 

from screens.face import Face
from screens.code import Code
from kivy.config import Config
from screens.login import Login
from screens.records import Records
from screens.workers import Workers
from screens.main_menu import MainMenu
from screens.tab_features import TabFeatures
from screens.capture_image import CaptureImage
from screens.worker_management import WorkerManagement



#Setting a window size
Window.size = (952, 488)

Config.set('kivy','keyboard_mode','multi')

# Setting the app full screen with no borders visible
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'borderless', '1')
Config.write()

# Remove full screen mode for debugging 
# Config.set('graphics', 'fullscreen', '0')  # Disable fullscreen
# Config.set('graphics', 'borderless', '0')  # Disable borderless
# Config.write()


# Dowloading the fonts
LabelBase.register(name="Ubuntu-Medium", fn_regular="/home/jetson/Desktop/entry_app/fonts/Ubuntu-Medium.ttf")
LabelBase.register(name="Barlow", fn_regular="/home/jetson/Desktop/entry_app/fonts/Barlow-Medium.ttf")


# Load KV files for screens
Builder.load_file('kv_files/camera.kv')
Builder.load_file('kv_files/code.kv')
Builder.load_file('kv_files/popup.kv')
Builder.load_file('kv_files/login.kv')
Builder.load_file('kv_files/mainmenu.kv')
Builder.load_file('kv_files/workers.kv')
Builder.load_file('kv_files/records.kv')
Builder.load_file('kv_files/workermanagement.kv')
Builder.load_file('kv_files/tabfeatures.kv')
Builder.load_file('kv_files/imagecapture.kv')

class windowManager(ScreenManager):
    """Initializes the Screen Manager for controlling the screens."""
    pass

# Adding all the screen widgets to Screen Manager
sm = windowManager() 
sm.add_widget(Face(name='camera'))
sm.add_widget(Login(name='login'))
sm.add_widget(Code(name='code'))
sm.add_widget(MainMenu(name='mainmenu'))
sm.add_widget(Workers(name='workers'))
sm.add_widget(WorkerManagement(name='workermanagement'))
sm.add_widget(Records(name='records'))
sm.add_widget(TabFeatures(name='tabfeatures'))
sm.add_widget(CaptureImage(name='capture'))

# The base of the app
class EntryGuardApp(App):
    """Main application class."""
    def build(self) -> windowManager:
        """Builds the application."""
        return sm
    
if __name__ == '__main__':
    EntryGuardApp().run()