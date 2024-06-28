import sqlite3
from entry_app.screens.popup import BasePopup
from db_management.base_class import Base

class Recognition(Base):
    """
    Class for managing facial recognition encodings.

    Inherits from the Base class for database operations.
    """

    def add_encoding(self,workerId,encoding):
        """
        Add a facial encoding to the database for a worker.

        Args:
            workerId: int: ID of the worker.
            encoding: str: Facial encoding data.

        Raises:
            BasePopup: If the worker with the specified ID is not found.
        """

        if self.check_exist('worker',workerId=workerId):
            try:
                face_encoding = {'workerId':workerId,'encoding':encoding}
                self.cursor.execute("INSERT INTO faceEncoding (workerId,encoding) VALUES (:workerId,:encoding)",face_encoding)
                self.connection.commit()
            except sqlite3.IntegrityError:
                print('Worker already exists')
        else: 
            popup = BasePopup(message = 'Worker with this ID was not found')
            popup.open()

    def manage_encoding(self,workerId,encoding):
        """
        Manage an existing facial encoding in the database for a worker.

        Args:
            workerId: int: ID of the worker.
            encoding: str: Updated facial encoding data.

        Raises:
            BasePopup: If the worker with the specified ID is not found.
        """
        if self.check_exist('faceEncoding',workerId=workerId) == True:
            try:
                self.cursor.execute("""UPDATE faceEncoding SET workerId = (?), encoding =(?)
                                    WHERE workerId = (?)""",(workerId,encoding))
                self.connection.commit()
            except sqlite3.IntegrityError:
                print('Worker already exists')
        else:
            popup = BasePopup(message = 'Worker with this ID was not found')
            popup.open()