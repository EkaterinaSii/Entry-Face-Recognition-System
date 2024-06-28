import os
import sqlite3
import numpy as np
import face_recognition

# Connection to the SQLite database
connection = sqlite3.connect("PATH TO DATABASE")
cursor = connection.cursor()
# Path where image will be saved
image_path = 'PATH TO IMAGE'

def encoding():
    """ 
    Encoding a face image with face_recognition library

    Returns:
        numpy.ndarray: Encoded faceimage
    """
    image = face_recognition.load_image_file(image_path)
    encode = face_recognition.face_encodings(image)[0]
    return encode

def convert_encoding():
    """
    Converting face encoding to bytes to store in SQLite.
    
    Returns:
        bytes: Byte representation of face encoding.
    """
    encode = encoding()
    image_blob = encode.tobytes()
    return image_blob

def save_db(workerId):
    """
    Save face encoding to the database.
    
    Args:
        workerId:int : ID of the worker to store the code encoding 
    """
    image_blob = convert_encoding()
    cursor.execute("INSERT INTO faceEncoding (workerId,encoding) VALUES (?,?)",(workerId,image_blob))
    connection.commit()
    os.remove(image_path)

def update_picture(workerId):
    image_blob = convert_encoding()
    cursor.execute("""UPDATE faceEncoding
                            SET encoding = (?)
                            WHERE workerId = (?)""",(image_blob,workerId,))
    connection.commit()
    os.remove(image_path)


def get_all_encodings():
    """
    Retrieve all face encodings and associated worker names from the database.
    Converting it to numpy arra to use for comparison in face recognition
    
    Returns:
        tuple: A tuple containing two lists - 
            - List of numpy arrays representing face encodings.
            - List of corresponding worker names.
    """
    cursor.execute('''SELECT faceEncoding.encoding, worker.name FROM faceEncoding
                   INNER JOIN worker on faceEncoding.workerId = worker.workerId''')
    results = cursor.fetchall()

    encodings = []
    names = []

    for record in results:
        encoding = np.frombuffer(record[0],dtype='float64')
        encodings.append(encoding)
        names.append(record[1])

    return encodings, names




