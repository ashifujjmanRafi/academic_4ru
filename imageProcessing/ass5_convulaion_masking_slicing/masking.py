import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():    
    path = 'mountain.jpeg'
    rgb = plt.imread(path)

    #print (rgb.shape)   
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    #print(grayscale.shape)

    r,c = grayscale.shape
    #mask = grayscale.copy()
    mask = np.zeros((r,c),dtype=np.uint8)
    mask[40:120,50:250] = 255
    mask = mask & grayscale

    plt.subplot(1,2,1)
    plt.imshow(rgb,'gray')

    plt.subplot(1,2,2)
    plt.imshow(mask,'gray')
    plt.savefig("A2")
    plt.show()


if __name__ == '__main__':
    main()