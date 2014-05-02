# AUTHORED BY PATRICK WU
# I AM WORKING FROM TIM'S LAPTOP (> -_-)>

import numpy as np
import cv2

class Box:
	def __init__(self):
		self.top =  0xffffffff
		self.left = 0xffffffff
		self.right = -1
		self.bottom = -1
		self.image = [[]]
	def area(self):
		return self.top * self.left
				
def testcolor(color):
	if color == 0:
		return 0
	else:
		return 1
	


cam1 = cv2.VideoCapture(1)
while True:
	ret, img1 = cam1.read()
	box1 = Box()
	
	cv2.imshow('frame.png', img1)

	# I don't know what this does vv
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
	margincount = 0

	for i in range(len(img1)):
		for j in range(len(img1[i])):
			print i, j
			whiteTest = []
			
			for k in range(len(img1[i][j])):
				# eval whitespace in image
				whiteTest.append(testcolor(img1[i][j][k]))
			
			#if color is detected, store pixel in box
			if sum(whiteTest) > 0:
				if  i < box1.top:
					box1.top = i
				elif i > box1.bottom:
					box1.bottom = i
				elif j < box1.left:
					box1.left = j
				elif j > box1.right:
					box1.right = j

cap.release()
cv2.destroyAllWindows()
