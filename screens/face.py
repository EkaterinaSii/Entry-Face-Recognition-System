import cv2
import time
import numpy as np
import face_recognition
from entry_app.open_lock import open_lock
from kivy.clock import Clock
from entry_app.db_management.image_encoding import get_all_encodings
from sklearn.externals import joblib
from kivy.uix.screenmanager import Screen
from kivy.graphics.texture import Texture
from db_management.worker_management import Worker
from db_management.record_management import Record

from collections import deque
import hashlib


class Face(Screen):
    """
    Screen for facial recognition functionality.

    Attributes:
        capture: cv2.VideoCapture: Video capture object for accessing the camera.
        current_frame: ndarray: Current frame captured by the camera.
        process_this_frame: bool: Flag to process each frame for face recognition.
        process_frame_count: int: Counter to track the number of frames processed.
        known_face_encodings: list: List of known face encodings.
        known_face_names: list: List of known face names corresponding to the encodings.
        detected_name: str: Name of the detected person.
        previous_detected_name: str: Previous detected name.
        last_detection_time: float: Timestamp of the last detection.
    """
    def __init__(self, **kwargs):
        super(Face, self).__init__(**kwargs)
        self.capture = None
        self.current_frame = None
        self.process_this_frame = True
        self.process_frame_count = 0
        self.known_face_encodings = []
        self.known_face_names = []
        self.detected_name = "None"
        self.previous_detected_name = None
        self.entered_time = 0

        self.spoofing_model = joblib.load("PATH TO THE ANTI FACE SPOOFING MODEL")
        
        # Spoof detection history
        self.spoof_detection_history = {}
        self.history_length = 10  # Number of frames to average
    
    def calc_hist(self,img):
        histogram = [0] * 3
        for j in range(3):
            histr = cv2.calcHist([img], [j], None, [256], [0, 256])
            histr *= 255.0 / histr.max()
            histogram[j] = histr
        return np.array(histogram)
    
    def check_if_spoof(self,face):
        img_ycrcb = cv2.cvtColor(face, cv2.COLOR_BGR2YCR_CB)
        img_luv = cv2.cvtColor(face, cv2.COLOR_BGR2LUV)
    
        ycrcb_hist = self.calc_hist(img_ycrcb)
        luv_hist = self.calc_hist(img_luv)
    
        feature_vector = np.append(ycrcb_hist.ravel(), luv_hist.ravel())
        feature_vector = feature_vector.reshape(1, len(feature_vector))
    
        prediction = self.spoofing_model.predict_proba(feature_vector)
        prob = prediction[0][1]

        return prob 


    def get_encodings(self):
        """
        Retrieve known face encodings and corresponding names from the database.
        """
        self.known_face_encodings, self.known_face_names = get_all_encodings()

    def on_enter(self, *args):
        """
        Actions to perform when the screen is entered.
        Starting the camera with resolution 1280x720.
        Updating the frames to show the video.
        """
        if not self.capture:
            self.capture = cv2.VideoCapture(0)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            self.get_encodings()
            Clock.schedule_interval(self.update, 1.0 / 50.0)

    def on_leave(self, *args):
        """
        Actions to perform when the screen is left.
        Closing the camera and stop capturing frames.
        """
        if self.capture:
            Clock.unschedule(self.update)
            self.capture.release()
            self.capture = None
            

    def enter(self, name):
        """
        Perform actions upon detecting a known face.
        Finding the id of the detected worker.
        Register the entry in the database.
        Open the door.

        Args:
            name: str: Name of the detected person.
        """
        
        worker = Worker()
        record = Record()
        worker_id = worker.find_id(name=name)
        record.add_record(worker_id)
        open_lock()

    def get_face_hash(self, face_encoding):
        return hashlib.sha256(face_encoding).hexdigest()
        
    def update(self, dt):
        """
        Update function to process each frame from the camera.
        Detecting the faces and encode it with face_recognition library.
        Comparing the fdetected face with already known encodings.
        Placing the rectangle around the detected face and placing the name of detected person
        If more than one person is detected, first one is registered in the database and in 10 seconds the other person will be registered
        if no person detected, variables for name storage reset in 15 seconds.        
        Args:
            dt: float: Time since the last update.
        """
        # check if the camera is not active
        if self.capture:
            # reads the frame from camera
            ret, frame = self.capture.read()
            # if Ture, proceeds
            if ret:
                # resizing the frame to 1/4 of its original size for faster processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                # convert from BGR (for openCV) to RGB (for face_recognition)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
                # detects the face location in the small RGB frame
                face_locations = face_recognition.face_locations(rgb_small_frame)
                # encode the face
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                # enpty list of names
                face_names = []
                # compare each face encoding with known 
                for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
                    face_to_check = frame[top*4:bottom*4, left*4:right*4]
                    spoof_prob = self.check_if_spoof(face_to_check)

                    face_hash = self.get_face_hash(face_encoding.tostring())
                    if face_hash not in self.spoof_detection_history:
                        self.spoof_detection_history[face_hash] = deque(maxlen=self.history_length)
                    
                    self.spoof_detection_history[face_hash].append(spoof_prob)
                    avg_spoof_prob = np.mean(self.spoof_detection_history[face_hash])
                    print(avg_spoof_prob)
                    if avg_spoof_prob < 0.8:
                        matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                        name = "Unknown"
                    # if mathc is found, get the corresponding name
                        if True in matches:
                            first_match_index = matches.index(True)
                            name = self.known_face_names[first_match_index]

                            # if the name is different from previous name, updates and calls enter
                            # also updates if 30 seconds passed from last entry
                            print(time.time() - self.entered_time )
                            if (name != self.detected_name  or (time.time() - self.entered_time > 30)) and name != "Unknown":
                                
                                print(time.time())
                                print(name)
                                print('new entry')
                                self.entered_time = time.time()
                                self.detected_name = name
                                self.enter(self.detected_name)

                        face_names.append(name)



                # making rectangle for each detected face    
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # scaling the face location back up to the original size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4
                    # drawing rectangle around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    # drawing ractangle below to place the name
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # flips the frame vertically 
            buf1 = cv2.flip(frame, 0)
            # converts to a string format suitable for displaying in kivy
            buf = buf1.tostring()
            # creating a new kivy texture with frame size and BGR format
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            # updating the texture with processed frame buffer
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display the frame
            self.ids.camera_texture.texture = image_texture