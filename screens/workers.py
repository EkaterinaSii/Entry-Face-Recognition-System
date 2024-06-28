from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from db_management.worker_management import Worker

class Workers(Screen):
    """
    Screen for displaying and managing workers.
    
    Attributes:
        mode:StringProperty : Property to hold the current mode (add, delete, manage).
        label_text:StringProperty : Property to hold the text to be displayed in the workers label.
    """

    mode = StringProperty()
    label_text = StringProperty("")
    
    def all_workers(self):
        """
        Retrieve and display all workers.
        Fetching all workers from the database, formating them, and updating the label text.
        """
        worker = Worker()
        all_workers = worker.find_all('worker')
        
        workers_display = []
        for worker in all_workers:
            workers_display.append(f"#{str(worker[0]):<3} | {str(worker[1]):<10} | {str(worker[2]):<15} | {str(worker[3]):<4}")
           

        self.label_text = "\n".join(workers_display)


    def button_pressed(self,choice):
        """
        Handle button presses for navigating to different screens or modes based on user choice.
        
        Args:
            choice:str : The label of the button pressed by the user, indicating the target action or screen.
        """
        sm = App.get_running_app().root
        if choice == 'back': sm.current = 'mainmenu'
        if choice == 'add_worker': 
            sm.get_screen('workermanagement').mode = 'add'
            sm.current = 'workermanagement'
        if choice == 'delete_worker':
            sm.get_screen('workermanagement').mode = 'delete'
            sm.current = 'workermanagement'
        if choice == 'manage_worker':
            sm.get_screen('workermanagement').mode = 'manage'
            sm.current = 'workermanagement'