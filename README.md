# DuplicateDeleter
Deletes Photos that are very similar and essentially duplicates given a folder of images

First Install Dependencies 

pip install pillow
pip install dhash

run from teminal second command line argument is the path to in folder of images to compare 

To Increase or decrease the strictness of Similarity 
Edit the variable COMPARE_PERCENTAGE 
0 is The same Image 100 is Completely different Default is 23

python3 DupFinder.py PATH_TO_IMAGE_FOLDER

 eg python3 DupFinder.py /home/jimbob/Pictures/face_recognition/je
