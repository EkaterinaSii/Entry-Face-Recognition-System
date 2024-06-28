import kivy
kivy.require('2.1.0')
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.properties import StringProperty

class BasePopup(Popup):
    """
    Base class for all popups and handels the simple notifications like door acess or worker management.
    
    Attributes:
        message:str : handling the content of the popup
    """

    message = StringProperty()

    def close_popup(self, dt:float):
        """
        Automatic closing the popup after a specified time.

        Args:
            dt:float : time after which the popu will be closed
        """ 
        self.dismiss()

    def open(self, *args, **kwargs):
        """
        Open the popup and close it. 

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().open(*args, **kwargs)
        Clock.schedule_once(self.close_popup, 3)

class DeletePopup(Popup):
    """ 
    Popup for confirmation of deletion. 
    The content of popup is handled via message varoiable.

    Attributes:
        message:str : handling the content of the popup
    """
    message = StringProperty()

    def __init__(self, message='', callback=None, **kwargs):
        """
        Delete Popup to confirm from the user the will to delete the worker.

        Args:
            message:str : the mesasge to display 
            callback (callavle): function to be called after the user confirms the deletion.
            **kwargs: Arbitrary keyword arguments.
        """
        super(DeletePopup, self).__init__(**kwargs)
        self.message = message
        self.callback = callback

    def delete_choice(self, choice):
        """
        Handle the choice to delete or not.

        Args:
            choice:str : user choice yes/no

        Returns:
            bools: True for 'yes' choice and False for 'no' 
        """
        if choice == 'yes': self.callback(True)
        elif choice == 'no': self.callback(False)
     
