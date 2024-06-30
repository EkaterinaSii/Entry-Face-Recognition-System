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
* Jetson Nano 
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


## GETTING STARTED
To run the app use `COMMAND HERE`

## DATABASE SCHEMA
<img src="https://drive.google.com/uc?export=view&id=1jPlnVwot_rCT5jQefbLJTDXzHhPCJB8S" width="800">

## ANTI FACE-SPOOFING MODEL
There is a [link](https://github.com/vardanagarwal/Proctoring-AI/tree/master/face_detection/models) to pre-trained model was used.

