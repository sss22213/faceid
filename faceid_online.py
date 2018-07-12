from flask import Flask, request, Response
import time
import face_recognition
import cv2
import numpy as np
import time
from collections import Counter
Display_timeout = 10

class face_id:
    def __init__(self):
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
            "face3_label"
        ]

    def Recognize(self,frame):
        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        Start_ticks = time.time()
        while True:
            End_ticks = time.time()
            # Resize frame of video to 1/4 size for faster face recognition processing
            #small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            small_frame = frame
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

#init
app = Flask(__name__)
fd = face_id()

@app.route('/Recognize', methods=['POST'])
def _Recognize():
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    result = fd.Recognize(img)
    return result[0][0]

# start flask app
app.run(host="0.0.0.0", port=8800)