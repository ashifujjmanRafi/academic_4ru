import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path = 'mountain.jpeg'
rgb = plt.imread(img_path)
gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

def bitslicing(img):
    r,c = img.shape
    bit1 = np.zeros((r,c),dtype = np.uint8)
    bit2 = np.zeros((r,c),dtype = np.uint8)
    bit3 = np.zeros((r,c),dtype = np.uint8)
    bit4 = np.zeros((r,c),dtype = np.uint8)
    bit5 = np.zeros((r,c),dtype = np.uint8)
    bit6 = np.zeros((r,c),dtype = np.uint8)
    bit7 = np.zeros((r,c),dtype = np.uint8)
    bit8 = np.zeros((r,c),dtype = np.uint8)

    bit1 = img & 1
    bit2 = img & 2
    bit3 = img & 4
    bit4 = img & 8
    bit5 = img & 16
    bit6 = img & 32
    bit7 = img & 64
    bit8 = img & 128
    
    img_set = [bit1,bit2,bit3,bit4,bit5,bit6,bit7,bit8]
    img_title = ['bit1','bit2','bit3','bit4','bit5','bit6','bit7','bit8']

    for i in range(len(img_set)):
        plt.subplot(4,2,i+1)
        plt.imshow(img_set[i],cmap='gray')
        plt.title(img_title[i])
    plt.tight_layout()
    plt.show()

def convulation(img):
    r,c = img.shape

    laplacian1 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    laplacian2 = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    laplacian3 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    laplacian4 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

    sobel1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    sobel2 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

    lap1 = cv2.filter2D(img,-1,laplacian1)
    lap2 = cv2.filter2D(img,-1,laplacian2)
    lap3 = cv2.filter2D(img,-1,laplacian3)
    lap4 = cv2.filter2D(img,-1,laplacian4)
    sov1 = cv2.filter2D(img,-1,sobel1)
    sov2 = cv2.filter2D(img,-1,sobel2)

    img_set = [lap1,lap2,lap3,lap4,sov1,sov2]
    img_title = ['Laplacian1','Laplacian2','Laplacian3','Laplacian4','Sobel1','Sobel2']
    for i in range(len(img_set)):
        plt.subplot(2,3,i+1)
        plt.imshow(img_set[i],cmap='gray')
        plt.title(img_title[i])
    plt.tight_layout()
    plt.show()

def masking(img):
    
    r,c = img.shape 
    mask = np.zeros((r,c),dtype = np.uint8)
    mask[50:120,80:200] = 255
    mask = mask & img

    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.subplot(1,2,2)
    plt.imshow(mask,cmap='gray')
    plt.show()



if __name__ == '__main__':
    bitslicing(gray)
    convulation(gray)
    masking(gray)

