Find-Waldo
==========
Contributors: Tim Yong, Patrick Wu, Eric Bronner, Edward Choi

The goal of this project is to ultimately build a biped robot with enabled visual imaging capabilities.
Given an image of an object, the robot will find an instance of that object within another image
	Ex: Find Waldo
This repo will contain the software for processing computer vision and imaging using a webcam as 'eyes'.

feed.py takes in an image taken from the webcam as input, and removes whitespace from it until there is a minimally large square of whitespace around the outermost border of the image.
