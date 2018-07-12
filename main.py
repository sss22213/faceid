from GUI import *
from recognize import *
from Client import *
'''
from faceid import *
'''
import time
Display_result = 'System initialization...'
fingerprint_result = ''
picture_code = 0

def delay(_second):
    start_time = time.time()
    end_time = time.time()
    while(end_time - start_time >_second):
        end_time = time.time()
        break
    
def finger_face_job():
    global fingerprint_result
    global Display_result
    global picture_code
    picture_code = 0
    fc = faceid_client(500,500,'yourip','/Recognize')
    fg = finger()
    picture_code = 1
    Display_result = ' '
    #Display_result = 'Please press fingerprint...'
    fingerprint = fg.finger_cmp()
    while(fingerprint==-1):
        fingerprint = fg.finger_cmp()
    fingerprint_result = fingerprint
    picture_code = 2
    Display_result = ' '
    frame = fc.Display_take()
    #time.sleep(0.001)
    #Display_result = 'Put face before the webcam'
    picture_code = 0
    Display_result = 'Face analysis...'
    time.sleep(0.001)
    result = fc.Get_Recognize(frame)
    print(result)
    if fingerprint_result == result:
        Display_result = 'Welcome to IOT room'
    else:
        Display_result = 'Forbiden'
    time.sleep(30)
    
if __name__ == "__main__":
    thread = threading.Thread(target = finger_face_job)
    thread.start()
    WF = Windows_form((1280,1024),'image/background.jpg')
    while True:
        WF.Start_Windows()
        WF.Put_Text(Display_result)
        #background change
        if(picture_code == 0):
            WF.change_picture_path('image/background.jpg')
        elif(picture_code == 1):
            WF.change_picture_path('image/finger_resized.png')
        elif(picture_code == 2):
            WF.change_picture_path('image/face_resized.png')
        if thread.is_alive() == False:
            thread = threading.Thread(target = finger_face_job)
            thread.start()
