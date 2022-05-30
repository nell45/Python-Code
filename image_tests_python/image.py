from PIL import Image
from PIL import ImageDraw


def open_image(path):
	img = Image.open(path)
	return img
	
def find_image_size(image):
	ims = image.size
	return ims
	
def image_text(image, size, text):
	imd = ImageDraw.Draw(image)
	width = size[0]
	height = size [1]
	newsize = (width/2, height/2)
	imd.text(newsize, text)
	return image

def image_save(image, filename):
	image.save(filename)

def main():
	image = open_image(r"C:\Users\k_nee\OneDrive\Documents\code\dragon_data\commonwelsho.jpg")
	size = find_image_size(image)
	textimage = image_text(image, size, "txt")
	image_save(textimage, r"C:\Users\k_nee\OneDrive\Documents\code\dragon_data\commonwelshtext.png")

main()
