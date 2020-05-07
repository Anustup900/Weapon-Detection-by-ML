

import numpy as np
import cv2 as cv2
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import *
import os
import imutils
import datetime





img = []

class eye:
	"""Here We Placed Button and read Instruction  label """
	def __init__(self,master):
		frame = Frame(master)   # Top frame
		frame.pack()
		#button1 = Button(frame,text="Upload",fg="white",bg="gray",width=7,height=2,command=self.upload).pack(side="left")
		button2 = Button(frame,text="Upload Video",fg="white",bg="gray",width=12,height=2,command=self.realtime).pack(side="right")
		dire0 = Label(master,text="read instruction:  ",fg="green")
		dire0.config(font=('Helvetica',13))
		dire0.pack()
		dire1 = Label(master,text="upload Button : to select video from project directory ",fg="red")
		dire1.config(font=('helvetica',14))
		dire1.pack()	
		dire3 = Label(master,text="Press 'q' to disable Webcam ",fg="red")
		dire3.config(font=('Helvetica',14))
		dire3.pack()
     
     
   		#In Upload Function we will Upload an image from Our Computer 
   		#Directory
   		#and then convert original image in Gray Scale Image
   		#apply haarcasCade Classifier in Gray Scale image to scan face part 
  
     
      	# Here we have have real time face detection Module
	def realtime(self):
    
		imgTemp = askopenfilename()
		camera = cv2.VideoCapture(imgTemp)
		gun_cascade = cv2.CascadeClassifier('cascade.xml')
		(grabbed, frame) = camera.read()
		firstFrame = None


		while True:
			(grabbed, frame) = camera.read()

    	       		# if the frame could not be grabbed, then we have reached the end of the video
			if not grabbed:
     	        		break

   		      	# resize the frame, convert it to grayscale, and blur it
			frame = imutils.resize(frame, width=500)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			gray = cv2.GaussianBlur(gray, (21, 21), 0)
			gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize = (100, 100))
			if len(gun) > 0:
        			gun_exist = True
        
			for (x,y,w,h) in gun:
				frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
				roi_gray = gray[y:y+h, x:x+w]
				roi_color = frame[y:y+h, x:x+w]    
			# if the first frame is None, initialize it
			if firstFrame is None:
				firstFrame = gray
				continue
	
			# draw the text and timestamp on the frame
			cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
			# show the frame and record if the user presses a key
			cv2.imshow("Security Feed", frame)
			key = cv2.waitKey(1) & 0xFF

			# When everything is done, release the capture


    
""" Quit Window """
def quit(root): 	
	root.destroy() 
root = Tk()  # Tkiniter Object(Window)
root.title("DA VINCI___")
root.geometry("600x300")
label1 = Label(root, 
	text="Firearm Detection Application ",
	fg = "light green",
 	bg = "dark green",
	font = "Helvetica 16 bold italic").pack()
	#label1 = Label(root,text="Face Detection Application ",width=67,height=13).pack()
button2 = Button(root,text="Exit",fg="green",bg="red",command=lambda root=root:quit(root)).pack()
root.configure(background="white")	
obj  = eye(root)   # pass window object eye Class

root.mainloop()
