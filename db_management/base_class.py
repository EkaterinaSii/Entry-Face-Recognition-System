import sqlite3

class Base:
    """
    Base class for database operations.

    Attributes:
        database: str: Path to the SQLite database file.
        connection: sqlite3.Connection: Connection object to the database.
        cursor: sqlite3.Cursor: Cursor object for executing SQL queries.
    """
    def __init__(self) -> None:
        self.database = 'PATH TO DATABASE'
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        self.connection = connection
        self.cursor = cursor 

    def find_all(self,table):
        """
        Retrieve all records from the specified table.

        Args:
            table: str: Name of the table to retrieve records from.

        Returns:
            list: List of records retrieved from the table.
        """

        if table != 'record':
            self.cursor.execute(f"SELECT * FROM {table}")
            return self.cursor.fetchall()
        else:
            self.cursor.execute(f"""SELECT record.recordId, record.dateTime, worker.name, worker.position
                                 FROM record
                                INNER JOIN worker on record.workerId = worker.workerId""")
            return self.cursor.fetchall()
    
    def list_records(self, table, **kwargs):
        """
        Retrieve records from the specified table based on given conditions.

        Args:
            table: str: Name of the table to retrieve records from.
            **kwargs: Arbitrary keyword arguments for specifying conditions.

        Returns:
            list: List of records retrieved from the table based on the conditions.
        """
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)

        where_clause = " AND ".join(conditions)
        self.cursor.execute(f"SELECT * FROM {table} WHERE {where_clause}", values)
        return self.cursor.fetchall()
    
    def check_exist(self,table,**kwargs):
        """
        Check if a record exists in the specified table based on given conditions.

        Args:
            table: str: Name of the table to check for existence.
            **kwargs: Arbitrary keyword arguments for specifying conditions.

        Returns:
            bool: True if a record exists, False otherwise.
        """
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)

        where_clause = " AND ".join(conditions)
        self.cursor.execute(f"SELECT * FROM {table} WHERE {where_clause}", values)
        check = self.cursor.fetchall()

        if len(check) == 0: return False
        else: return True

    def find_id(self,**kwargs):
        """
        Find the ID of a record based on given conditions.

        Args:
            **kwargs: Arbitrary keyword arguments for specifying conditions.

        Returns:
            int: ID of the record found based on the conditions.
        """
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)

        where_clause = " AND ".join(conditions)
        self.cursor.execute(f"SELECT workerId FROM worker WHERE {where_clause}", values)
        
        return self.cursor.fetchall()[0][0]
