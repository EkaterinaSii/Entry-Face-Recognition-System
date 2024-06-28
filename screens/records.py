from datetime import datetime
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from db_management.record_management import Record

class Records(Screen):
    """
    Screen for displaying log records.
    
    Attributes:
        label_text:StringProperty : Text to be displayed in the records label.
    """

    label_text = StringProperty("")
    
    def all_records(self,choice='date'):
        """
        Retrieve and display all records.
        Fetching all records from the database, formats them, and updates the label text.
        """
        record = Record()
        all_records = record.find_all('record')
        records_display = []

        if choice == 'date':
            all_records = sorted(all_records,key=lambda log: datetime.strptime(log[1],"%d/%m %H:%M"),reverse=True)
        if choice == 'name':
            all_records = sorted(all_records,key=lambda log: log[2])



        for log in all_records:
            records_display.append(f"{str(log[1]):<11} | {str(log[2]):<5} | {str(log[3]):<15}")
        
        self.label_text = "\n".join(records_display)


    def button_pressed(self,choice):
        """
        Handle button presses for navigating back to the main menu.
        
        Args:
            choice:str : button pressed - back only for now
        """
        sm = App.get_running_app().root
        if choice == 'back': sm.current = 'mainmenu'