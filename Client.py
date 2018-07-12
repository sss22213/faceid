import requests
import cv2
import time
Display_timeout = 5

class faceid_client:
    def __init__(self,hight,widgth,addr,api):
        #init
        self.addr = addr
        self.test_url = addr + api
        self.hight = hight
        self.widgth = widgth
        
    
    def Display_take(self):
        Start_ticks = time.time()
        video_capture = cv2.VideoCapture(0)
        #Take face 
        for i in range(1000):
            ret, frame = video_capture.read()
            #Reserve origin image
            frame = cv2.resize(frame, (self.hight, self.widgth), fx=0, fy=0)
            cv2.rectangle(frame, (self.hight//2-200, self.widgth//2-200), (self.hight//2+200,self.widgth//2+200), (0, 255, 0), 2)
            cv2.namedWindow("Image",cv2.WINDOW_FULLSCREEN)
            cv2.imshow('Image', frame)
            End_ticks = time.time()
            #origin
            cv2.waitKey(15)
            if End_ticks-Start_ticks > Display_timeout:
                break
        cv2.destroyAllWindows()
        video_capture.release()
        return frame[self.widgth//2-200:self.widgth//2+200,self.hight//2-200:self.hight//2+200] 

    def Get_Recognize(self):      
        # prepare headers for http request
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}
        frame = self.Display_take()
        img = cv2.resize(frame, (500, 500), fx=0, fy=0)
        # encode image as jpeg
        _, img_encoded = cv2.imencode('.jpg', img)
        # send http request with image and receive response
        r = requests.post(self.test_url, data=img_encoded.tostring(), headers=headers)
        return r.text

    def Get_Recognize(self,frame):      
        # prepare headers for http request
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}
        img = cv2.resize(frame, (500, 500), fx=0, fy=0)
        # encode image as jpeg
        _, img_encoded = cv2.imencode('.jpg', img)
        # send http request with image and receive response
        r = requests.post(self.test_url, data=img_encoded.tostring(), headers=headers)
        return r.text

if __name__ == "__main__":
    fc = faceid_client(1280,1024,'YourIP','/Recognize')
    print(fc.Get_Recognize())

