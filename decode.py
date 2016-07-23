# encoding:utf-8

import os,sys,urllib2,re,Image
import ImageFilter
import ImageDraw
import StringIO
import random

if __name__ == '__main__':
	filename = 'des.png'
	im = Image.open(filename)
	#im.show();
	print im.format,im.size,im.mode
	h,w = im.size
	draw = ImageDraw.Draw(im)
	#draw.polygon([(0,0), (h,0), (h,w), (0,w)],fill=(255,255,255))
	for i in range(h):
		print '%d:%d'%(h,i)
		for j in range(w):
			r,g,b = im.getpixel((i, j))
			r = r%2*255
			g = g%2*255
			b = b%2*255
			draw.point((i,j),fill=(r,g,b))
	im.show()