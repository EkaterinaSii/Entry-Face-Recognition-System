import cv2
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import Screen


class CaptureImage(Screen):
    """
    Screen for capturing images using the device's camera for storage and ecoding.
    """

    def __init__(self, **kwargs):
        """
        Initialize the CaptureImage screen.
        
        Args:
            **kwargs: Arbitrary keyword arguments.
        """
        super(CaptureImage, self).__init__(**kwargs)
        self.capture = None
        self.current_frame = None

    def on_enter(self, *args):
        """
        Event handler for entering the screen.
        Start tje camera and schedule frame updates.
        
        Args:
            *args: Variable length argument list.
        """
        if not self.capture:
            self.capture = cv2.VideoCapture(0)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            Clock.schedule_interval(self.update, 1.0 / 30.0)

    def on_leave(self, *args):
        """
        Event handler for leaving the screen.
        Stops the camera
        
        Args:
            *args: Variable length argument list.
        """
        if self.capture:
            Clock.unschedule(self.update)
            self.capture.release()
            self.capture = None

    def update(self, dt):
        """
        Capture and display frames from the camera.
        
        Args:
            dt:float : Time interval between frames.
        """
        if self.capture:
            ret, frame = self.capture.read()
            if ret:
                self.current_frame = frame
                buf1 = cv2.flip(frame, 0)
                buf = buf1.tostring()
                image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
                image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                self.ids.camera_texture.texture = image_texture
                

    def capture_choice(self,choice):
        """
        Handling the choice of capturing thepicture or cancelling the operation
        
        Args:
            choice:str : The user's choice, either 'capture' or 'discard'.
        """
        sm = App.get_running_app().root
        
        if choice == 'capture':
            cv2.imwrite('PATH TO IMG', self.current_frame)

        sm.current = 'workermanagement'