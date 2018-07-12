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
        finger_database = [b'\x01',b'\x03',b'\x04']
        finger_name = ['name1','name2','name3']
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





        