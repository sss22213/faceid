import face_recognition
import cv2
import numpy as np
import time
from collections import Counter
from recognize import *

#Display timeout
Display_timeout = 5

class face_id:
    def __init__(self,hight,widgth):
        
        #Camera,Screen hight,widgth
        self.hight = hight
        self.widgth = widgth

        self.obama_image = face_recognition.load_image_file("face1.jpg")
        self.obama_face_encoding = face_recognition.face_encodings(self.obama_image)[0]

        # Load a second sample picture and learn how to recognize it.
        self.biden_image = face_recognition.load_image_file("face2.jpg")
        self.biden_face_encoding = face_recognition.face_encodings(self.biden_image)[0]

        # Load a second sample picture and learn how to recognize it.
        self.ss_image = face_recognition.load_image_file("face3.jpg")
        self.ss_face_encoding = face_recognition.face_encodings(self.ss_image)[0]

        # Create arrays of known face encodings and their names
        self.known_face_encodings = [
            self.obama_face_encoding,
            self.biden_face_encoding,
            self.ss_face_encoding
        ]
        self.known_face_names = [
            "face1_label",
            "face2_label",
            "face3_label
        ]
    
    def Display_take(self):
        Start_ticks = time.time()
        video_capture = cv2.VideoCapture(0)
        #Take face 
        for i in range(1000):
            ret, frame = video_capture.read()
            #Reserve origin image
            frame = cv2.resize(frame, (self.hight, self.widgth), fx=0, fy=0)
            cv2.rectangle(frame, (self.hight//2-200, self.widgth//2-300), (self.hight//2+200,self.widgth//2+200), (0, 255, 0), 2)
            cv2.namedWindow("Image",cv2.WINDOW_FULLSCREEN)
            cv2.imshow('Image', frame)
            End_ticks = time.time()
            #origin
            cv2.waitKey(15)
            if End_ticks-Start_ticks > Display_timeout:
                break
        cv2.destroyAllWindows()
        video_capture.release()
        return frame[self.widgth//2-350:self.widgth//2+250,self.hight//2-250:self.hight//2+250]

    def take(self):
        frame = self.Display_take()
        return frame

    def Recognize(self):
        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        #Get image
        frame = self.take()
        Start_ticks = time.time()

        while True:
            End_ticks = time.time()
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                face_names = []

                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_face_names[first_match_index]
                face_names.append(name)

            process_this_frame = not process_this_frame

            if End_ticks-Start_ticks > Display_timeout:
                break
        #Get high Frequency
        word_counts = Counter(face_names)
        top_name = word_counts.most_common(1)
        return top_name

if __name__ == "__main__":
    fd = face_id(1280,1024)
    fg = finger()
    fingerprint = fg.finger_cmp()
    print("init3")
    while(fingerprint==-1):
        fingerprint = fg.finger_cmp()
    print(fingerprint)

    '''
    result = fd.Recognize()
    print(result)
    '''


