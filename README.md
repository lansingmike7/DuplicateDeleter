# DuplicateDeleter
Deletes Photos that are very similar and essentially duplicates, given a folder of images

Provide a non empty folder This isnt stress tested chances are youll break it and find bugs and optimizations to be made
wrote this in 30 minutes for something im working on.

First Install Dependencies 

pip install pillow
pip install dhash


To Increase or decrease the strictness of Similarity 
change the -t argument 
0 is The same Image 100 is Completely different Default is 23

Run from teminal second command line argument is the path to in folder of images to compare 



python3 DupFinder.py -i PATH_TO_IMAGE_FOLDER -t INT_TOLORANCE
-t is optional default is 23

 eg python3 DupFinder.py -i /home/jimbob/Pictures/face_recognition/je -t 13
