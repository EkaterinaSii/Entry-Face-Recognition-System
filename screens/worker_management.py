import os
from kivy.app import App
from entry_app.screens.popup import BasePopup, DeletePopup
from entry_app.db_management.image_encoding import save_db, update_picture
from kivy.uix.screenmanager import Screen
from db_management.worker_management import Worker
from kivy.properties import StringProperty,ObjectProperty

class WorkerManagement(Screen):
    """
    Screen for managing worker records including adding, updating, and deleting workers.
    
    Attributes:
        mode:StringProperty : Property to hold the current mode (add, delete, manage).
        worker_name:ObjectProperty : Property to hold the worker's name.
        worker_position:ObjectProperty : Property to hold the worker's position.
        worker_key:ObjectProperty : Property to hold the worker's entry key.
        worker_id:ObjectProperty : Property to hold the worker's ID.
        update_name:ObjectProperty : Property to hold the updated worker's name.
        update_position:ObjectProperty : Property to hold the updated worker's position.
        update_key:ObjectProperty : Property to hold the updated worker's entry key.
        worker_update:str : Property to hold the worker's data to be updated.
        worker:Worker : Instance of the Worker class for managing worker data.
    """

    mode = StringProperty()

    worker_name = ObjectProperty(None)
    worker_position = ObjectProperty(None)
    worker_key = ObjectProperty(None)
    worker_id = ObjectProperty(None)

    update_name = ObjectProperty(None)
    update_position = ObjectProperty(None)
    update_key = ObjectProperty(None)

    worker_update = ''


    worker = Worker()

    def add_worker(self):
        """
        Add a new worker to the database after validating input fields and checking for a taken picture.
        """
        sm = App.get_running_app().root
        name = self.worker_name.text
        position = self.worker_position.text
        entrykey = self.worker_key.text

        if len(name) != 0 and len(position) != 0 and len(entrykey) != 0:
            if os.path.exists('PATH TO IMG'):
                print('picture is taken')
                self.worker.add_worker(name,position,entrykey)
                id = self.worker.find_id(entryKey=entrykey)
                save_db(id)

                self.clear_fields()

                popup = BasePopup(message='Worker was successfully added')
                popup.open()

                sm.get_screen('workers').all_workers()
                sm.current = 'workers'
            else:
                popup = BasePopup(message = 'Picture was not taken!')
                popup.open()
        else:
            popup = BasePopup(message='Some fields are missing')
            popup.open()
       

    def manage_worker(self):
        """
        Part of manageing the exisiting user's information.
        Check if the user is in database. Take the existing information to put it to placeholders.

        
        Raises:
            ValueError: If the worker ID input is not a valid integer.
        """
        sm = App.get_running_app().root
        try:
            id = int(self.worker_id.text)
            if self.worker.check_exist('worker',workerId=id) == True:
                sm.get_screen('workermanagement').mode = 'add_update'
                sm.current = 'workermanagement'

                self.worker_update = self.worker.list_records('worker',workerId=id)

                self.update_name.text = self.worker_update[0][1]
                self.update_position.text = self.worker_update[0][2]
                self.update_key.text = self.worker_update[0][3]

            else:
                popup = BasePopup(message = 'Worker with this ID was not found')
                popup.open()

            self.clear_fields()

        except ValueError:
            self.worker_id.text = ''
            popup = BasePopup(message = 'Enter ID number to find worker')
            popup.open()
        
        
    def update_worker(self,worker_update):
        """
        Update an existing worker's information.
        Take the new information entered. Check that there is new information or picture.
        Update database.
        
        Args:
            worker_update: List: Worker's data to be updated.
        """
        sm = App.get_running_app().root
        name = worker_update[0][1]
        position = worker_update[0][2]
        key = worker_update[0][3]

        upd_name = self.update_name.text
        upd_position = self.update_position.text
        upd_key = self.update_key.text

        if len(upd_name) != 0 and len(upd_position) != 0 and len(upd_key) != 0:

            if upd_name == name and upd_position == position and upd_key == key and os.path.exists('PATH TO IMG') == False:
                popup = BasePopup(message = 'No information was changed')
                popup.open()

            else:
                self.worker.update_worker(name,upd_name, \
                                        position,upd_position, \
                                        key,upd_key)
                
                if os.path.exists('PATH TO IMG'):
                    id = self.worker.find_id(entryKey=upd_key)
                    update_picture(id)


                popup = BasePopup(message = 'Worker info was sucessfully changed')
                popup.open()

                self.update_name.text = ''
                self.update_position.text = ''
                self.update_key.text = ''

                sm.get_screen('workers').all_workers()
                sm.current = 'workers'
        
        else: 
            popup = BasePopup(message='Some fileds are missing')
            popup.open()

        
    def delete_worker(self):
        """
        Delete an existing worker's information.

        Raises:
           ValueError: If the worker ID input is not a valid integer.
        """
        sm = App.get_running_app().root
        try:
            id = int(self.worker_id.text)

            def on_delete_choice(choice):
                if choice:
                    print("Deleting worker...")
                    self.worker.delete_worker(id)
                    self.clear_fields()

                else:
                    print("Not deleting worker.")
                    self.clear_fields()

                sm.get_screen('workers').all_workers()
                sm.current = 'workers'

            if self.worker.check_exist('worker',workerId=id) == True:
                popup = DeletePopup(message='Are you sure you want to delete this worker?', callback=on_delete_choice)
                popup.open()
            else:
                popup = BasePopup(message='Worker with this ID was not found')
                popup.open()
                self.worker_id.text = ''

        except ValueError:
            self.worker_id.text = ''
            popup = BasePopup(message = 'Enter ID number to find worker')
            popup.open()



    def button_pressed(self,choice):
        """
        Perform action based on the button choice.
        
        Args:
            choice: str: The button choice (add, delete, manage, cancel, update, back).
        """
        sm = App.get_running_app().root
        if choice == 'add': self.add_worker()
        if choice == 'delete': 
            self.delete_worker()
        if choice == 'manage': self.manage_worker()
        if choice == 'cancel':
           if os.path.exists('PATH TO IMG'):
                os.remove('PATH TO IMG') 
           sm.get_screen('workermanagement').mode = 'manage'
           sm.current = 'workermanagement'
        if choice == 'update': self.update_worker(self.worker_update)
        if choice == 'back': 
            if os.path.exists('PATH TO IMG'):
                os.remove('PATH TO IMG')
            self.clear_fields()
            sm.current = 'workers'

    def capture(self):
        """
        Navigate to the screen for capturing a worker's picture.
        """
        sm = App.get_running_app().root
        sm.current = 'capture'


    def clear_fields(self):
        """
        Clear all input fields.
        """
        self.worker_name.text = ''
        self.worker_position.text = ''
        self.worker_key.text = ''
        self.worker_id.text = ''

