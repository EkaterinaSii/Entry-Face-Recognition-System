# Entry-Face-Recognition-System
**Bachelor Degree Thesis.**
> Enhancing Access Control: Practical Implementation of Facial Recognition Technology for Entry Monitoring and Database Storage.

According to the American Lost and Found Statistics of 2023, 60% of individuals reported losing an item in the past year, with keys, cell phones, wallets,and sunglasses being the most common. 
This raises the question: what if physical keys were no longer necessary?

This thesis explores the implementation of facial recognition technology in a security entry system to enhance security, improve access tracking, and eliminate the need for physical keys in secure areas. 
The system developed is a software solution running on the Jetson Nano, integrated with a camera, display, electromagnetic lock, and Arduino Uno. The system operates autonomously, with the use of facial recognition technology granting access to authorized users stored in the database. It also includes backup entry methods like an entry code and allows administrators to manage access permissions and review entry logs through a dedicated interface.

The final system demonstrated reliable facial recognition and anti-spoofing capabilities, though with room for improvement in accuracy. 
The work serves as a foundation for developing autonomous access control systems applicable in different areas

## REQUIREMENTS
- Python 3.8.x
- Ubuntu 20.04.6

  ### Python Libraries
- Kivy 2.1.0
- Scikit-learn (sklearn) 0.22
- Numpy 1.16.5
- Face Recognition 1.2.3
- OpenCV (cv2) 4.8.0
- PySerial 3.4  

**Note:**
* Jetson Nano comes with Ubuntu 18.04, which is too old. Here is a [link](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image) to dowload Ubuntu 20.4 OS image.
* To use the same pre-trained anti-face-spoofing model, Scikit-learn version 0.19.1 - 0.22.0 is required. Starting from version 0.23.1, it will not run.

## HARDWARE COMPONENTS
* Jetson Nano
* Arduino (I used Arduino Uno)
* Relay
* 12v DC Adapter
* Electromagnetic lock
* Touch Screen (BIGTREETECH HDMI 7 in my case)
* Web Camera
* DC Power Supply 12v for lock
* DC Power Supply 5v for Jetson Nano

## SCHEMATIC
<img src="https://drive.google.com/uc?export=view&id=18_Wwx-Y6DJazKv0eb_-yJuabARP7sOPu" width="800">

### ARDUINO UNO SCHEMA
<img src="https://drive.google.com/uc?export=view&id=1F47PXbSt1xT7HPwhILVsSjDEXubr2_F0" width="800">

## ANTI FACE-SPOOFING MODEL
There is a [link](https://github.com/vardanagarwal/Proctoring-AI/tree/master/face_detection/models) to pre-trained model was used.

## HARDWARE CONFIGURATION

Before running the code, ensure that the camera and Arduino ports are correctly configured. Check and update the ports in the code to match your setup:

1. **Camera Port**: Ensure that the camera is connected and recognized by the system. You can check the camera port using:
   ```bash
   ls /dev/video*

2. **Arduino Port**: Ensure that the Arduino is connected and recognized by the system. You can check the Arduino port using:
   ```bash
   ls /dev/ttyUSB*
   
## GETTING STARTED
1. Clone the repository
```bash
git clone https://github.com/EkaterinaSii/Entry-Face-Recognition-System.git
```
2. Install the required dependencies
```cd Entry-Face-Recognition-System```
```pip install -r requirements.txt```
3. Run the app
```python3 main.py```

## SUPPORTED OPERATIONS
* Entry and lock opening with face recognition
* Entry and lock opening with a code (personal code assigned while creating a new worker/user)
* Adding a new worker/user
* Updating an existing worker/user (personal details and/or face encoding)
* Deleting an existing worker/user
* Listing all entry information (date/worker/position)
* Listing all workers/users (ID/worker/position/entry code)

## DATABASE SCHEMA
<img src="https://drive.google.com/uc?export=view&id=1jPlnVwot_rCT5jQefbLJTDXzHhPCJB8S" width="800">

## APP SCREENSHOTS
* Working Face Recognition 
<img src="https://drive.google.com/uc?export=view&id=1VioeesABHbJgW4WNTrymQcgWv59sig30" width="500">
* Main Screen with Face Recognition
<img src="https://drive.google.com/uc?export=view&id=1zdcAXBTSDqkxb5dW5M0mKlYCzlSxTKnz" width="500">
* Screen with Code Entry
<img src="https://drive.google.com/uc?export=view&id=1Cc7k3I47tXeV70XRwrGYMQCWWRYVu8Ig" width="500">
* Admin Login Screen to access Worker Management Functions
<img src="https://drive.google.com/uc?export=view&id=1lydWZcfE5Y6dsQki-RZ_VXgPrbNM9auk" width="500">
* Main Menu of Admin Mode
<img src="https://drive.google.com/uc?export=view&id=19QV_Ana_1swcc6IofhqLkHZ6tkJGBdaP" width="500">
* Worker Screen with Access to Add/Manage/Delete Functions
<img src="https://drive.google.com/uc?export=view&id=15uawRy02oSaH0YM_sDEjMkwsKXCKVBCV" width="500">
* Records Screen
<img src="https://drive.google.com/uc?export=view&id=10jY1NtajCAf8OVizV54q9t0nVet052EC" width="500">
* Example of PopUps, deleting user
<img src="https://drive.google.com/uc?export=view&id=1lDaxfk6bqLPIykGQNhp1s4RMCia878WX" width="500">

#### DESKTOP IMAGE :)
<img src="https://drive.google.com/uc?export=view&id=1tNobuVJldC7bpTEmD0SKmR1nANnjleKU" width="50">

