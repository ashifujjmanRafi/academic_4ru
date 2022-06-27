import matplotlib.pyplot as plt
import cv2
import numpy as np
def imread():
	img_path = 'mountain.jpeg'
	print(img_path)
	
	rgb = plt.imread(img_path)
	print(rgb.shape)
	
	gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
	print(gray.shape)
	
	r,c = gray.shape
	
	
	calchist = cv2.calcHist([gray],[0],None,[256],[0,255])
	kernal = np.ones((3,3))/9
	convo = cv2.filter2D(gray,-1,kernal)
	print(convo.shape)
	
	#point processing
	#tresh hold values
	t1,t2 = 100,150
	epsilon = 10e-6
	
	
	
	
	
	
	
	
	
	
	
	img_set = [rgb,gray,convo]
	img_title = ['RGB','GRAY','CONVULATION']
	
	for i in range(len(img_set)):
		plt.subplot(2,2,i+1)
		plt.imshow(img_set[i],'gray')
		plt.title(img_title[i])
	plt.subplot(2,2,4)
	plt.plot(calchist,'r')
	plt.show()
		
	
if __name__ == '__main__':
	imread()
