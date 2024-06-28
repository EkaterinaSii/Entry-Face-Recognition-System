import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []
# List all avalable ports
for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))


# Set serial same as in Arduino file
serialInst.baudrate = 9600
# Set the port of the camera, can be checked from the portList above
serialInst.port = "/dev/ttyUSB0"


def open_lock():
    """
    Opens serial connection if it's not and sends a command "open" to open the lock.
    """
    if not serialInst.is_open:
        serialInst.open()


    command = "open"
    serialInst.write(command.encode('utf-8'))  # Ensure command matches expected format
