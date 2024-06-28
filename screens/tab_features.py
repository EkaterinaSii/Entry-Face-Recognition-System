from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class TabFeatures(Screen):
    """
    Screen for imitating the Panlle Tab. 
    Consists of buttons to navigate to: camera screen, code screen and admin screen
    """

    def button_pressed(self, choice):
        """
        Handle button presses for navigating to different screens based on user choice.
        Camera screen, Code screen and Admin screen
               
        Args:
            choice:str : button pressed by the user
        """
        sm = App.get_running_app().root
        if choice == 'camera':
            sm.current = 'camera'
        elif choice == 'code':        
            sm.current = 'code'
        elif choice == 'admin':
            sm.current = 'login'