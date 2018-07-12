import serial

class finger:
    def __init__(self):
        self.ser = serial.Serial(
            port='/dev/ttyACM0',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def Get_finger_number(self):
        x = self.ser.readline()
        if(len(x)==0):
            return -1
        else: 
            return x

    def finger_cmp(self):
        #finger database
        finger_database = [b'FPM1',b'FPM2',b'FPM3']
        finger_name = ['face1_label','face1_labe2','face1_labe3']
        fingerprint = self.Get_finger_number()
        result = []
        #Check finger
        for finger_result in range(len(finger_database)):
            if fingerprint == finger_database[finger_result]:
                result = finger_name[finger_result]
        #return 
        if(len(result) > 0):
            return result
        else:
            return -1





        