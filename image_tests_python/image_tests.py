import sys
from PIL import Image,ImageDraw,ImageColor
import random
#def openImage(imageName):
	print(imageName)
	im=Image.open(imageName)
	im.show()
	return im
	
#def rotateImage(Imdat):
	Imdat.rotate(45).show()

#def scale(Imdat,imsize,imoffset):
	Imdat.putdata(data,scale=imsize,offset=imoffset).show()



#Imagedata=openImage("C:\\Users\\k_nee\\OneDrive\\Pictures\\minipix4.png")

#rotateImage(Imagedata)
#scale(Imagedata,3.0,100)


list[]

for i in range(0,100)
	list.append(i+)
	print(list)

#def crossDraw(Imdat):
	draw=ImageDraw.Draw(Imdat)
	draw.line((0,0)+Imdat.size, fill=0,width=8)
	draw.line((0,Imdat.size[1],Imdat.size[0],0),fill=(255,255,255),width=8)
	

#crossDraw(Imagedata)
#Imagedata.show()

#def makeImage(mode,size,color):
	Imdat=Image.new(mode,size,color)
	Imdat.show()
	return Imdat

#def colorhalf(Imagedata,color1):
	for x in range(0,Imagedata.size[0]):
		for y in range(0,Imagedata.size[1]):
			if(( y <= Imagedata.size[1]/2)):
				Imagedata.putpixel((x,y),color1)
	Imagedata.show()		
	return Imagedata
	
	
	
#def borders_5(Imagedata, border= 5):
	for i in range (0,50):
		r_rand = random.randint(0,255)
		g_rand = random.randint(0,255)
		b_rand = random.randint(0,255)
		for x in range(0,Imagedata.size[0]):
			for y in range(0,Imagedata.size[1]):
				
					
					
					
					if (x >= i*border and x <= ((i+1)*border) and y>i*border and y<(Imagedata.size[1]-(i+1)*border)):
						Imagedata.putpixel((x,y),(r_rand,g_rand,b_rand))
					if (y >= i*border and y <= ((i+1)*border) and x>i*border and x<(Imagedata.size[0]-(i+1)*border)):
						Imagedata.putpixel((x,y),(r_rand,g_rand,b_rand))
					if (x <= (Imagedata.size[0]-i*border) and x >= (Imagedata.size[0]-(i+1)*(border))and y>i*border and y<(Imagedata.size[1]-i*border)):
						Imagedata.putpixel((x,y),(r_rand,g_rand,b_rand))
					if (y <= (Imagedata.size[1]-i*border) and y >= (Imagedata.size[1]-(i+1)*(border))and x>i*border and x<(Imagedata.size[0]-i*border)):
						Imagedata.putpixel((x,y),(r_rand,g_rand,b_rand))
				
	Imagedata.show()		
	return Imagedata	
	
#def colorgradient(Imagedata,color1,border= 5,border2= 10):
	for x in range(0,Imagedata.size[0]):
		for y in range(0,Imagedata.size[1]):
			Imagedata.putpixel((x,y),(255,255-y,0))
			if (x <= border or x > Imagedata.size[0]- border):
				Imagedata.putpixel((x,y),(0,0,0))
			if (y <= border or y > Imagedata.size[1]- border):
				Imagedata.putpixel((x,y),(0,0,0))
			if (x >= border and x <= (border+border2) and y>border and y<(Imagedata.size[1]-border)):
				Imagedata.putpixel((x,y),(0,255,255))
			if (y >= border and y <= (border+border2) and x>border and x<(Imagedata.size[0]-border)):
				Imagedata.putpixel((x,y),(0,255,255))
			if (x <= (Imagedata.size[0]-border) and x >= (Imagedata.size[0]-(border+border2))and y>border and y<(Imagedata.size[1]-border)):
				Imagedata.putpixel((x,y),(0,255,255))
			if (y <= (Imagedata.size[1]-border) and y >= (Imagedata.size[1]-(border+border2))and x>border and x<(Imagedata.size[0]-border)):
				Imagedata.putpixel((x,y),(0,255,255))
	Imagedata.show()		
	return Imagedata

#def getWitdhHeight(stripeThickness,numstripes):
	h=numstripes*stripeThickness
	w=h*2
	
	return w,h
#def DrawLine(lineThickness,Imagedata,numstripes,):
	w=Imagedata.size[0]
	h=Imagedata.size[1]
	usa_red= (191,10,48)
	currentColor="white"
	previousColor="white"
	draw=ImageDraw.Draw(Imagedata)
	for i in range(0,numstripes):
		P1=(0,lineThickness*i+lineThickness*0.5)
		P2=(w,lineThickness*i+lineThickness*0.5)
		if (previousColor==usa_red):
			currentColor="white"
		else:
			currentColor=usa_red
			
		draw.line((P1[0],P1[1],P2[0],P2[1]), fill=currentColor,width=lineThickness)
		previousColor = currentColor
	Imagedata.show()
	return Imagedata
	
#def drawsquare(Imagedata,color,regionW,regionH):
		wstep=int(regionW/7)
		hstep=int(regionH/10)
		draw=ImageDraw.Draw(Imagedata)
		for i in range(int(hstep),regionH-int(hstep/2),hstep):
			for j in range(int(wstep/2),regionW-int(wstep/2),wstep):
				x0=j-4
				y0=i-4
				x1=j+4
				y1=i+4
				draw.rectangle([x0,y0,x1,y1],fill =color)
		Imagedata.show()



#def dictionary_test():

	bookfairWish={"poster":9.99,"Goes bananas":6.99,"Super gifted":7.99,"Dog's best friend": 8.99,"The big game":6.99,"Just beyond":9.99}
	list=["x",5,3,7]
	for num in list:
		print num

	for i in range (0, len(list)):
		print list[i]
	

 list1=[]
 
 for i in range(0,100):
	list1[i] = i+1
	print (list1)
 
 
 

#str_thickness=40
#line_thickness= 40
#num_stripes =13
#width,height=getWitdhHeight(line_thickness,num_stripes)
#newim=makeImage("RGB",(255,255),ImageColor.getrgb("red"))													
#stripes=DrawLine(line_thickness,newim,num_stripes)
#fadeyellow=borders_5(newim)
#whiteStar=drawsquare(partblue,ImageColor.getrgb("white"),int(width*2/5),7*line_thickness)
