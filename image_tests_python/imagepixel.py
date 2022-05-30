from PIL import Image

class image_ops:
	def __init__(self, image_path):
		self.image_path = image_path
		self.pil_image = Image.open(self.image_path)
	def get_image_size(self):
		size = self.pil_image.size
		return size
	def get_pixel_value(self, i, j):
		pixel_col = self.pil_image.getpixel((i,j))
		return pixel_col
				
	def invert_pixels(self):
		w_h = self.get_image_size()
		for i in range(0, w_h[0]):
			for j in range(0, w_h[1]):
				pixel_col = self.get_pixel_value(i,j)
				ri = 255 - pixel_col[0]
				gi = 255 - pixel_col[1]
				bi = 255 - pixel_col[2]
				self.pil_image.putpixel((i,j), (ri, gi, bi))
		return self.pil_image
				
				
	def sepia_pixels(self):
		w_h = self.get_image_size()
		sepia = [232, 202, 128]
		for i in range(0, w_h[0]):
			for j in range(0, w_h[1]):
				pixel_col = self.get_pixel_value(i,j)
				average_color = (pixel_col[0] + pixel_col[1] + pixel_col[2])/3
				tr = 0.393 * pixel_col[0] + 0.769 * pixel_col[1] + 0.189 * pixel_col[2]
				tg = 0.349 * pixel_col[0] + 0.686 * pixel_col[1] + 0.168 * pixel_col[2]
				tb = 0.272 * pixel_col[0] + 0.534 * pixel_col[1] + 0.131 * pixel_col[2]
				if tr > 255:
					r = 255 
				else:
					r = tr
				if tg > 255:
					g = 255 
				else: 
					g = tg
				if tb > 255:
					b = 255
				else:
					b = tb
				#sr = average_color * sepia[0]/255 + .3* average_color
				#sg = average_color * sepia[1]/255 + .3* average_color
				#sb = average_color * sepia[2]/255 + .3* average_color
				self.pil_image.putpixel((i,j), (int(r), int(g), int(b)))
		return self.pil_image

#testops = image_ops(r"C:\Users\k_nee\OneDrive\Documents\code\dragon_data\ukrainianironbelly.jpg")
#im = testops.sepia_pixels()
#im.show()
 
