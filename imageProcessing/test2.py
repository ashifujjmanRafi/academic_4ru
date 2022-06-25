import cv2
import matplotlib.pyplot as plt
import numpy as np
def hist(img):

	d = dict()
	for i in range(256):
		d[i]=0
	#print(d)
	for i in img:
		for j in i:
			d[j] += 1
	#print(d)
	return d

def convulation(img,kernal):
	
	row,col = img.shape
	print(img.shape)
	r,c = kernal.shape[0]//2,kernal.shape[1]//2
	r, c = r*2, c*2	
	
	out = np.ones((row-r,col-c))
	
	for i in range(row-r):
		for j in range(col-c):
			x = np.sum(np.multiply(img[i:3+i,j:3+j],kernal))
			if(x<0):
				out[i][j]=0
			elif(x>255):
				out[i][j]=255
			else:
				out[i][j]=x
	return out
	

def main():
	img_path = 'mountain.jpeg'
	print(img_path)
	
	rgb  = plt.imread(img_path)
	gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
	red = rgb[:,:,0]
	
	kernal = np.array([[1,2,1],[2,4,2],[1,2,1]])
	
	rhist = hist(red)
	conv = convulation(gray,kernal)
	
	plt.subplot(2,2,1)
	plt.plot(rhist.values())
	plt.subplot(2,2,2)
	plt.imshow(conv,'gray')
	
	plt.show()	

if __name__ == '__main__':
	main()
