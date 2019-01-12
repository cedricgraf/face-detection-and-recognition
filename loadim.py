from PIL import Image
import glob
import face_recognition
image_list = []
encodings = []
names = []
for filename in glob.glob('know/CI2019/*.jpg'): #assuming jpg
	c= face_recognition.load_image_file(filename)
	name = filename[12:-4]
	names.append(name)
	c_encoding_name = face_recognition.face_encodings(c)[0]
	encodings.append(c_encoding_name)
print names

