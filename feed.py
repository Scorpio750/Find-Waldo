import numpy as np #linear algebra
import cv2

class Box:
	def __init__(self):
		self.top = [0][0]
		self.left = [0][0]
		self.right = [0][0]
		self.bottom = [0][0]
	def area(self):
		return self.top * self.left
	
cam1 = cv2.VideoCapture(1)
while True:
	ret, img1 = cam1.read()
	box1 = Box()
	# work with img1
	print img1
	
	
	cv2.imshow('frame.png', img1)

	# I don't know what this does vv
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
	
	margincount = 0

	for i in range(len(img1)):
		
		for j in range(len(img1[i]):
			whiteTest = []
			
			for k in range(len(img1[i][j])):
				# eval whitespace in image
				whiteTest.append(testcolor(img1[i][j][k]))
			
			#if color is detected, store pixel in box param based on margincount
			if sum(whiteTest) > 0:
				if margincount == 0:
					box1.top = img[i][j]
					margincount += 1
				elif margincount == 1:
					box1.left = img[i][j]
					margincount += img

def testcolor(int color):
	if color == 0
		return 0
	else
		return 1
	


cap.release()
cv2.destroyAllWindows()
