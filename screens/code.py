from kivy.app import App
from entry_app.screens.popup import BasePopup
from entry_app.open_lock import open_lock
from kivy.uix.screenmanager import Screen
from db_management.record_management import Record


class Code(Screen):
     """
     Screen for entering and validating access codes.
     
     Attributes:
        entered_code:str : The code entered by the user.
        record:Record : Instance of the Record class for managing records.
     """
     entered_code = ''
     record = Record()

     def entry_code(self, button_number):
        """
        Handle button presses for entering the access code.
        
        Args:
            button_number:str : The label of the button pressed by the user.
        """
        sm = App.get_running_app().root
        code_label = self.ids.code_label

        if button_number == 'Enter':
             code_label.text = ""

             if self.record.check_exist('worker',entryKey=self.entered_code) == True:
                id = self.record.find_id(entryKey=self.entered_code)
                self.record.add_record(id)
                open_lock()
                popup = BasePopup(message = 'Access Granted')
                popup.open()

                sm.current = 'camera'
             else:
                popup = BasePopup(message = 'Access Denied')
                popup.open()

             self.entered_code = ''
        
        elif button_number == 'Clear':
             self.entered_code = self.entered_code[:-1]
             code_label.text = code_label.text[:-1]
        else:
             self.entered_code += str(button_number)
             code_label.text += f"{str(button_number)}"