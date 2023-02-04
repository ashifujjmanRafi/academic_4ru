import matplotlib.pyplot as plt
import cv2
import numpy as np

def calhist(img):
	d = dict()
	for i in range(256):
		d[i]=0
	for i in img:
		for j in i:
			d[j] += 1
	return d

def convulation(img,kernal):
	row,col = img.shape
	r,c = kernal.shape[0]//2,kernal.shape[1]//2
	r,c = r*2,c*2
	new_img = np.ones((row-r,col-c))
	for i in range(row-r):
		for j in range(col-c):
			x = np.sum(np.multiply(img[i:3+i,j:3+j],kernal))
			if(x>255):
				new_img[i][j]=255
			elif(x<0):
				new_img[i][j] = 0
			else:
				new_img[i][j] = x
	return new_img

def main():
	img_path ='mountain.jpeg'
	print(img_path)
	
	rgb = plt.imread(img_path)
	
	t1,t2 = 100,150
	
	gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
	
	r,c = gray.shape
	
	point_prox = np.ones((r,c),dtype = np.uint8)
	
	for i in range(r):
		for j in range(c) :
			if gray[i][j]>t1 and gray[i][j]<t2:
				point_prox[i][j] = 199
			else:
				point_prox[i][j] = gray[i][j]
	
	
	box_kernal =np.ones((3,3))/9
	
	box_conv = cv2.filter2D(gray,-1,box_kernal)
	
	
	r,c= gray.shape
	mask = np.zeros((r,c),dtype=np.uint8)
	mask[50:130,150:220]=255
	mask = mask & gray
	
	
	
	bit1 = np.zeros((r,c),dtype=np.uint8)
	bit1 = gray & 32
	his2= cv2.calcHist([gray],[0],None,[256],[0,255])
	
	
	x = convulation(gray,box_kernal)
	
	#print(calhist(gray))
	his = calhist(gray)
	plt.subplot(1,2,1)
	plt.imshow(box_conv,'gray')
	plt.subplot(1,2,2)
	plt.imshow(x,'gray')
	plt.show()
	
	print(gray.shape)
if __name__ == '__main__':
	main()
