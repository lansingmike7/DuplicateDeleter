import dhash
import sys
import os
import shutil
import argparse
from PIL import Image
dhash.force_pil()



os.system('cls' if os.name=='nt' else 'clear')

parser = argparse.ArgumentParser();
parser.add_argument('-i', type=str, help='Folder of Images to Process.', required=True)


parser.add_argument('-t', type=int, help='Tolerance of similarity detection, higher is stricter.', default=23)
#This is the severity of comparision between Images
args = vars(parser.parse_args())
ImageFolder = args['i']
tol = args['t']

COMPARE_PERCENTAGE = 23






outdir = str(str(os.path.splitext(ImageFolder)[-1]) + "Duplicates");

#check if output directory already exists, and if not, create it
os.makedirs(outdir, exist_ok=True)


ToMove = []
NotDone = True
i = 0
Reset = False
ListOfImages = []
for subdir, dirs, files in os.walk(ImageFolder):
	for file in files:
		ListOfImages.append(os.path.join(subdir, file))
#continue until all images have been checked and if no duplicates are found

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
			if(ListOfImages[j] not in ToMove):
				ToMove.append(ListOfImages[j])
		sys.stdout.write('\rComparing file %s with %s' % ((ListOfImages[i][ListOfImages[i].rfind("/")+1:]), (ListOfImages[j][ListOfImages[j].rfind("/")+1:])))
	if(len(ToMove) == 0 and Reset):
		NotDone = False
	else:
		Reset = False
	for k in ToMove:
		shutil.move(k, outdir)
	ToMove = []
	ListOfImages = []
	for subdir, dirs, files in os.walk(ImageFolder):
		for file in files:
			ListOfImages.append(os.path.join(subdir, file))
	i+=1
	if(i>=len(ListOfImages)):
		i = 0
Reset = True
			
