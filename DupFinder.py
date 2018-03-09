import dhash
import sys
import os
from PIL import Image
dhash.force_pil()
COMPARE_PERCENTAGE = 23

ImageFolder = sys.argv[1]
ToDelete = []
NotDone = True
i = 0
Reset = False
ListOfImages = []
for subdir, dirs, files in os.walk(ImageFolder):
	for file in files:
			ListOfImages.append(os.path.join(subdir, file))
while NotDone:
	image = Image.open(ListOfImages[i])
	row, col = dhash.dhash_row_col(image)
	BaseHash = dhash.format_hex(row, col)
	BaseHash = "0x"+BaseHash
	for j in range(i+1, len(ListOfImages)):
		image = Image.open(ListOfImages[j])
		row, col = dhash.dhash_row_col(image)
		CompareHash = dhash.format_hex(row, col)
		CompareHash = "0x"+CompareHash
		if(dhash.get_num_bits_different(int(BaseHash, 16), int(CompareHash, 16))<COMPARE_PERCENTAGE):
			if(ListOfImages[j] not in ToDelete):
				ToDelete.append(ListOfImages[j])
		sys.stdout.write('\rComparing file %s with %s' % (ListOfImages[i], ListOfImages[j]))
	if(len(ToDelete) == 0 and Reset):
		NotDone = False
	else:
		Reset = False
	for k in ToDelete:
		os.remove(k)
	ToDelete = []
	ListOfImages = []
	for subdir, dirs, files in os.walk(ImageFolder):
		for file in files:
				ListOfImages.append(os.path.join(subdir, file))
	i+=1
	if(i>=len(ListOfImages)):
		i = 0
		Reset = True

			
