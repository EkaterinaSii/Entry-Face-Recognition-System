from kivy.app import App
from kivy.uix.screenmanager import Screen


class MainMenu(Screen):
    """
    Screen for the main menu, providing navigation to other screens.
    """

    def button_pressed(self, choice):
        """
        Handle button presses for navigating Workers, Records Screens and Logout button.

        Args:
            choice:str : pressed button to change screen - workers/records/logout
        """

        sm = App.get_running_app().root
        if choice == 'workers':
            sm.get_screen('workers').all_workers()
            sm.current = 'workers'
        elif choice == 'records':
            sm.get_screen('records').all_records()
            sm.current = 'records'
        elif choice == 'logout':
            sm.current = 'login'