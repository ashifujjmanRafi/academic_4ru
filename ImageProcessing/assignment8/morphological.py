import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
	img_path = "mountain.jpg"
	rgb = plt.imread(img_path)
	
	gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
	
	
	_,binary_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
	print(binary_img.shape)

	
	kernal1 = np.ones((5,5),dtype=np.uint8)
	#sharpen kernal
	kernal2 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype=np.uint8)
	#edge kernal
	kernal3 = np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]],dtype=np.uint8)
    

	img_erosion =  cv2.erode(binary_img,kernal1)
	img_dilation = cv2.dilate(binary_img,kernal1)

	opening = cv2.dilate(img_erosion,kernal1)
	closing = cv2.erode(img_dilation,kernal1)

	img_erosion1 =  cv2.erode(binary_img,kernal2)
	img_dilation1 = cv2.dilate(binary_img,kernal2)

	opening1 = cv2.dilate(img_erosion,kernal2)
	closing1 = cv2.erode(img_dilation,kernal2)

	img_erosion2 =  cv2.erode(binary_img,kernal3)
	img_dilation2 = cv2.dilate(binary_img,kernal3)

	opening2 = cv2.dilate(img_erosion,kernal3)
	closing2 = cv2.erode(img_dilation,kernal3)

	img_set = [img_erosion,img_dilation,opening,closing,img_erosion1,img_dilation1,opening1,closing1,img_erosion2,img_dilation2,opening2,closing2]
	img_title = ["Erosion","Dilation","Opening","Closing"]

	for i in range(len(img_set)):
		plt.subplot(3,4,i+1)
		if(i<4):
			plt.title(img_title[i])
		plt.imshow(img_set[i],'gray')
	plt.savefig("result")
	plt.show()


	
if __name__ == '__main__':
	main()
