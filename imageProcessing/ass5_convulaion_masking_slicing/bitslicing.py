import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = 'mountain.jpeg'
    rgb = plt.imread(path)
    print (rgb.shape)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape)

    r,c = grayscale.shape

    bit1 = np.zeros((r,c),dtype = np.uint8)
    bit2 = np.zeros((r,c),dtype = np.uint8)
    bit3 = np.zeros((r,c),dtype = np.uint8)
    bit4 = np.zeros((r,c),dtype = np.uint8)
    bit5 = np.zeros((r,c),dtype = np.uint8)
    bit6 = np.zeros((r,c),dtype = np.uint8)
    bit7 = np.zeros((r,c),dtype = np.uint8)
    bit8 = np.zeros((r,c),dtype = np.uint8)

    for i in range(r):
        for j in range(c):
            bit1[i][j]=grayscale[i][j] & 1


    bit2 = grayscale & 2
    bit3 = grayscale & 4
    bit4 = grayscale & 8
    bit5 = grayscale & 16
    bit6 = grayscale & 32
    bit7 = grayscale & 64
    bit8 = grayscale & 128

    img_set =[bit1,bit2,bit3,bit4,bit5,bit6,bit7,bit8]
    #print(bit1)
    plot_img(img_set)

def plot_img(img_set):
    n= len(img_set)

    for i in range(n):
        plt.subplot(4,2,i+1)
        plt.imshow(img_set[i],cmap='gray')
    plt.savefig("A1")    
    plt.show()


if __name__ == '__main__':
    main()