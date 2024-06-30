# Entry-Face-Recognition-System
**Bachelor Degree Thesis.**
> Enhancing Access Control. Practical Implementation of Facial Recognition Technology for Entry Monitoring and Database Storage.

## REQUIREMENTS
- Python 3.8.x
- Ubuntu 20.04.6
- Kivy 2.1.0
- Sklearn 0.22

**Note:**
* Jetson Nano comes with Ubuntu 18.04 and this version is too old. 
Here is a [link](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image) to dowload Ubuntu 20.4 OS image
* To use same pre-trained anti face-spoofing model Sklearn version 0.19.1 - 0.22.0 required. Starting from version 0.23.1 it will not run.

## HARDWARE COMPONENTS
* Jetson Uno
* Arduino (I used Arduino Nano)
* Relay
* 12v DC Adapter
* Electromagnetic lock
* Touch Screen (BIGTREETECH HDMI 7 in my case)
* Web Camera
* DC Power Supply 12v for lock
* DC Power Supply 5v for Jetson Nano

## SCHEMATIC
<img src="https://drive.google.com/uc?export=view&id=1N9AkYic_cDQYoCd4rAZMJcxF8xsY6ceS" width="800">

### ARDUINO UNO SCHEMA
<img src="https://drive.google.com/uc?export=view&id=1F47PXbSt1xT7HPwhILVsSjDEXubr2_F0" width="800">

## ANTI FACE-SPOOFING MODEL
There is a [link](https://github.com/vardanagarwal/Proctoring-AI/tree/master/face_detection/models) to pre-trained model was used.

## GETTING STARTED
To run the app use `python3 main.py`

## SUPPORTED OPERATIONS
* Entry and Lock opening with Face Recognition
* Entry and Lock opening with Code (Personal Code assigned while creating new worker/user)
* Adding new worker/user
* Updating existed worker/user (Personal details and/or Face Encoding)
* Deleting existed worker/user
* List all the entry information (date/worker/position)
* List all workers/users (ID/worker/position/entry code)

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

