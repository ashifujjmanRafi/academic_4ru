import matplotlib.pyplot as plt
import cv2
import numpy as np

def cus_hist(img):
	d = dict()
	for i in range(256):
		d[i]=0
	for i in img:
		for j in i :
			d[j] += 1
	return d
	
def convulation(img,kernal):
	row,col = img.shape
	r,c = kernal.shape[0]//2,kernal.shape[1]//2
	r,c = r*2,c*2
	ret_img = np.zeros((row-r,col-c),dtype = np.uint8)
	for i in range(row-r):
		for j in range(col-c):
			x = np.sum(np.multiply(img[i:3+i,j:3+j],kernal))
			if(x<0):
				ret_img[i][j]=0
			elif(x>255):
				ret_img[i][j]=255
			else:
				ret_img[i][j]=x
	return ret_img




def main():
	img_path = "mountain.jpg"
	print(img_path)
	rgb = plt.imread(img_path)
	print(rgb.shape)
	
	gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
	print(gray.shape)
	
	_,binary_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
	print(binary_img)
	
	kernal = np.ones((3,3),dtype = np.uint8)
	
	eroded_image = cv2.erode(binary_img,kernal)
	
	img1 = cus_hist(rgb[:,:,0])
	
	img2 = cv2.calcHist([rgb],[0],None,[256],[0,256])
	
	avarage_kernal = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
	
	custom_convo = convulation(gray,avarage_kernal)
	
	img3 = cv2.filter2D(gray,-1,avarage_kernal)
	
	masking = np.zeros((gray.shape),dtype=np.uint8)
	masking[110:180,80:100]=255
	masking=masking&gray
	
	plt.subplot(2,1,1)
	plt.plot(img1.keys(),img1.values(),'r')
	plt.subplot(2,1,2)
	plt.imshow(custom_convo,'gray')
	
	plt.show()	
	
	
if __name__ == '__main__':
	main()
