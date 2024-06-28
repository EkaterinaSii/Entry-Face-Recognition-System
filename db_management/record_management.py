import sqlite3
from datetime import datetime
from db_management.base_class import Base

class Record(Base): 
    """
    Class for managing records of worker entries.
    Inherits from the Base class for database operations.
    """       
    def add_record(self,worker_id):
        """
        Add a record of a worker's entry to the database.

        Args:
            worker_id: int: ID of the worker.
        """

        check_worker = self.check_exist('worker',workerId=worker_id)

        if check_worker == True:
            try:
                record = {'dateTime':datetime.now().strftime('%d/%m %H:%M'),'workerId':worker_id}
                self.cursor.execute("INSERT INTO record (dateTime,workerId) VALUES (:dateTime,:workerId)",record)
                self.connection.commit()
            except sqlite3.IntegrityError:
                pass
        else:
            print('Worker does not exist')