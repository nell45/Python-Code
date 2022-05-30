from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
from PIL import ImageDraw
from PIL import ImageFont
import sys

code_path = r"C:\Users\k_nee\OneDrive\Documents\code"

sys.path.append(code_path)
from imagepixel import image_ops


class Dragon():
	def __init__(self, breed, color, native, rating, image_path):
		self.breed = breed
		self.color = color
		self.native = native
		self.rating = rating
		self.image_path = image_path
		
	def get_breed(self):
		return self.breed
		
	def get_color(self):
		return self.color
		
	def get_native(self):
		return self.native
	
	def get_rating(self):
		return self.rating	
		
	def show_image(self):
		im = Image.open(self.image_path)
		im.show()
	def emboss_image(self):
		im = Image.open(self.image_path)
		img = im.filter(ImageFilter.EMBOSS)
		img.show()
	def contour_image(self):
		im = Image.open(self.image_path)
		img = im.filter(ImageFilter.CONTOUR)
		img.show()
	def blur_image(self):
		im = Image.open(self.image_path)
		img = im.filter(ImageFilter.GaussianBlur(4))
		img.show()
	def invert_image(self):
		im = Image.open(self.image_path)
		img = ImageOps.invert(im)
		img.show()
		
	def neel_invert(self):
		imp = image_ops(self.image_path)
		im = imp.invert_pixels()
		im.show()
	def neel_sepia(self):
		image = image_ops(self.image_path)
		im = image.sepia_pixels()
		im.show()
	def find_edges_on_image(self):
		im = Image.open(self.image_path)
		img = im.filter(ImageFilter.FIND_EDGES)
		img.show()

drag_list = [{"breed":"Hungarian Horntail", "color": "black", "native":"Hungary", "rating":5, "image_path":r"image_data\hungarianhorntail.jpg"},
{"breed":"Chinese Fireball", "color":"red", "native":"China", "rating":4, "image_path":r"image_data\chinesefireball.jpg"},
{"breed":"Swedish Short Snout", "color":"blue and grey", "native":"Sweden", "rating":3, "image_path":r"image_data\swedishshortsnout.jpg"},
{"breed":"Hebridian Black", "color":"black", "native":"Hebrides", "rating":4, "image_path":r"image_data\hebridianblack.png"},
{"breed":"Norwegian Ridgeback", "color":"black", "native":"Norway", "rating":3, "image_path":r"image_data\norbertwo.jpg"},
{"breed":"Ukranian Ironbelly", "color":"grey and black", "native":"Ukraine", "rating":5, "image_path":r"image_data\ukrainianironbelly.jpg"},
{"breed":"Common Welsh Green", "color":"green", "native":"Wales", "rating":3, "image_path":r"image_data\commonwelsho.jpg"}]




drag_obj_list= []

for dragon in drag_list:
	dragobj = Dragon(dragon['breed'], dragon['color'], dragon['native'], dragon['rating'], dragon['image_path'])
	drag_obj_list.append(dragobj)

print("Options: Hungarian Horntail, Chinese Fireball, Swedish Short Snout, Hebridian Black, Norwegian Ridgeback, Ukranian Ironbelly, or the Common Welsh Green")	
breed = input()
for drag in drag_obj_list:
	if breed == drag.get_breed():
		drag.show_image()
		drag.emboss_image()
		drag.contour_image()
		#drag.invert_image()
		drag.neel_sepia()
		drag.neel_invert()
		drag.find_edges_on_image()
		drag.find_image_size()
		print("The breed name of this dragon is the " +str (drag.get_breed()))
		print("This dragon lives in " +str (drag.get_native()))
		print("The color of this dragon is " +str (drag.get_color()))
		print("The danger level of this dragon is " +str (drag.get_rating()) +" out of 5!")
		

	
'''
for dragobj in drag_obj_list:
	print(dragobj.get_breed())
	print(dragobj.get_color())
	print(dragobj.get_native())
	print(dragobj.get_rating())

	if dragobj.get_rating() >= 4 :
		print(dragobj.get_breed())
		print(dragobj.get_color())
		print(dragobj.get_native())
		print(dragobj.get_rating())
'''