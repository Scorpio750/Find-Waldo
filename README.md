Find-Waldo
==========
Contributors: Tim Yong, Patrick Wu, Eric Bronner, Edward Choi

The goal of this project is to ultimately build a robot which can detect an image of Waldo from one of the popular "Where's Waldo" books.
This repo will contain the software for processing computer vision and imaging using a webcam as 'eyes'.

feed.py takes in an image taken from the webcam as input, and removes whitespace from it until there is a minimally large square of whitespace around the outermost border of the image.
