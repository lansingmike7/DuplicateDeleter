# DuplicateDeleter

Deletes photos that are very similar and essentially duplicates inside of a folder. By default, all duplicates are moved into a duplicates folder in the script folder.

### Installation

DuplicateDeleter requires Python 3 and a few packages.

You can install the packages automatically with
```python
pip install -r requirements.txt
```

or manually with
```python
pip install pillow
pip install dhash
```

### Options

| Variable | Use |
| ------ | ------ |
| -i | Input Directory |
| -t | Tolerance Level of Detection [Optional] (Default = 23)|

 With tolerance, lower values will increase the amount of detections. A higher value will decrease the amount of detections.


### Example Use

To run the script in the currently selected folder
```python
python DupFinder.py
```
If you would like to specify a different directory
```python
python DupFinder.py -i INPUT_FOLDER -t 13
```
Here is an example of the script
```python
python DupFinder.py -i /home/jimbob/Pictures/face_recognition/je -t 13
```
