import tkinter as tk
import threading
import cv2
import time

class Windows_form:
    def __init__(self,size,picture_path):
        self.size = size
        self.picture_path = picture_path
        self.load_image()

    def load_image(self):
        self.image = cv2.imread(self.picture_path)
        self.image = cv2.resize(self.image,self.size,fx=0, fy=0, interpolation = cv2.INTER_CUBIC)

    def Start_Windows(self):
        cv2.namedWindow("Recognize System",cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Recognize System",self.image)
        cv2.waitKey(30)

    def change_picture_path(self,path):
        self.picture_path = path

    def Put_Text(self,text):
        self.load_image()
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(self.image,text,(self.size[0]//2-500,self.size[1]//2),font,3,(255,255,255),2,cv2.LINE_AA)

if __name__ == "__main__":
    WF = Windows_form((1280,1024),'image/background.jpg')
