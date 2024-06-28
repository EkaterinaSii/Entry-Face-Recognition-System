from kivy.app import App
from entry_app.screens.popup import BasePopup
from db_management.base_class import Base
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class Login(Screen):
     """
     Screen for user login.
    
     Attributes:
         id_number:ObjectProperty : Property to hold the ID number entered by the user.
         entry_key:ObjectProperty : Property to hold the entry key entered by the user.
         admin:Base : Instance of the Base class for managing admin checks.
     """
     id_number = ObjectProperty(None)
     entry_key = ObjectProperty(None)

     admin = Base()


     def login_button(self):
          """
          Handle login button press. 
          Check user credentials and navigate to the main menu if valid.
          """
          sm = App.get_running_app().root
          id_number = self.id_number.text
          entry_key = self.entry_key.text

          if self.admin.check_exist('admin',idNumber=id_number,loginKey=entry_key):
               sm.current = 'mainmenu'
          else:
               popup = BasePopup(message='Access Denied')
               popup.open()
     
          self.id_number.text = "" 
          self.entry_key.text = "" 