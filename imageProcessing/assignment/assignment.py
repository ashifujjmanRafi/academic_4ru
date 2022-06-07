import matplotlib.pyplot as plt
import cv2
import numpy

def fig1():
	img_path = 'mountain.jpg'
	
	#print(img_path)

	rgb_img = plt.imread(img_path)
	
	# img = cv2.imread(img_path)	
	
	#print(rgb_img.shape)
	#print(rgb_img)
	
	grayscale_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
	
	#print(grayscale_img.shape)
	
	_,binary_img = cv2.threshold(grayscale_img, 127, 255, cv2.THRESH_BINARY)
	
	#print(binary_img.shape)
	
	plt.figure(figsize = (30, 30))
	
	plt.subplot(2, 3, 1)
	plt.title('RGB')
	plt.imshow(rgb_img)
	
	plt.subplot(2, 3, 2)
	plt.title('Red')
	plt.imshow(rgb_img[:, :, 0], cmap = 'gray')
	
	plt.subplot(2, 3, 3)
	plt.title('Green')
	plt.imshow(rgb_img[:, :, 1], cmap = 'gray')
	
	plt.subplot(2, 3, 4)
	plt.title('Blue')
	plt.imshow(rgb_img[:, :, 2], cmap = 'gray')
	
	plt.subplot(2, 3, 5)
	plt.title('Grayscale')
	plt.imshow(grayscale_img, cmap = 'gray')
	
	plt.subplot(2, 3, 6)
	plt.title('Binary')
	plt.imshow(binary_img, cmap = 'gray')
	
	plt.show()













def main():
    # image path
    path = 'mountain.jpg'
    
 
    
    # read image
    img = plt.imread(path)
    
    # print shape, max and min value
    #print(img.shape, img.max(), img.min())

   
    
    
    # convert image into grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # convert image into binary
    _, binary = cv2.threshold(grayscale, 20, 255, cv2.THRESH_BINARY)

    # plot histogram
    red = cv2.calcHist([img], [0], None, [256], [0, 256])
    green = cv2.calcHist([img], [1], None, [256], [0, 256])
    blue = cv2.calcHist([img], [2], None, [256], [0,256])
    grayscale = cv2.calcHist([grayscale], [0], None, [256], [0, 256])
    binary = cv2.calcHist([binary], [0], None, [256], [0, 256])

    plt.figure(figsize = (20, 20))

    plt.subplot(2,3, 1)
    plt.title('RGB')

    plt.plot(red, 'r')
    plt.plot(green, 'g')
    plt.plot(blue, 'b')

    plt.subplot(2,3, 2)
    plt.title('Red')
    plt.plot(red, 'r')

    plt.subplot(2,3, 3)
    plt.title('Green')
    plt.plot(green, 'g')
    
    plt.subplot(2,3, 4)
    plt.title('Blue')
    plt.plot(blue, 'b')
    
    plt.subplot(2,3, 5)
    plt.title('Grayscale')
    plt.plot(grayscale, 'k')

    plt.subplot(2,3, 6)
    plt.title('Binary')
    plt.plot(binary, 'k')
    
    

    plt.show()

if __name__ == '__main__':	
    fig1()
    main()
    
