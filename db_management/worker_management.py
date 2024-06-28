import sqlite3
from db_management.base_class import Base
from entry_app.screens.popup import BasePopup

class Worker(Base):
    """
    Class for managing worker information.
    Inherits from the Base class for database operations.
    """    
    def add_worker(self,name,position,entrykey):
        """
        Add a new worker to the database.

        Args:
            name: str: Name of the worker.
            position: str: Position of the worker.
            entrykey: str: Entry key of the worker.

        Raises:
            BasePopup: If a worker with the same entry key already exists.
        """

        try:
            worker = {'name':name,'position':position,'entryKey':entrykey}
            self.cursor.execute("INSERT INTO worker (name,position,entryKey) VALUES (:name,:position,:entryKey)",worker)
            self.connection.commit()
        except sqlite3.IntegrityError:
            popup = BasePopup(message = 'Worker already exists')
            popup.open()

    def delete_worker(self,id):
        """
        Delete a worker from the database.

        Args:
            id: int: ID of the worker to be deleted.
        """
        
        self.cursor.execute("DELETE FROM worker WHERE workerId = (?)",(id,))
        self.connection.commit()
        self.cursor.execute("DELETE FROM faceEncoding WHERE workerId = (?)",(id,))
        self.connection.commit()



    def update_worker(self,name,new_name,position,new_position,entrykey,new_entrykey):
        """
        Update a worker's information in the database.

        Args:
            name: str: Name of the worker.
            new_name: str: Updated name of the worker.
            position: str: Position of the worker.
            new_position: str: Updated position of the worker.
            entrykey: str: Entry key of the worker.
            new_entrykey: str: Updated entry key of the worker.

        Raises:
            BasePopup: If the worker with the specified information is not found.
        """

        if self.check_exist('worker',name=name,position=position,entryKey=entrykey) == True:
            self.cursor.execute("""UPDATE worker SET name = (?), position = (?), entryKey =(?)
                                WHERE name = (?) AND position = (?) AND entryKey = (?)""",(new_name,new_position,new_entrykey,name,position,entrykey))
            self.connection.commit()
            print('Updated')
        else:
            popup = BasePopup(message = 'Worker with this ID was not found')
            popup.open()


