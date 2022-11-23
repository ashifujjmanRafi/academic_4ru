import cv2
import matplotlib.pyplot as plt
import numpy as np



def custom_hist(img):
    d = dict()
    for i in range(256):
        d[i]=0
    for i in img:
        for j in i:
            d[j] += 1
    return d

def convulation(img,kernal):

    row , col = img.shape

    r , c = kernal.shape[0]//2 , kernal.shape[1]//2

    r , c = r*2 , c*2

    new_image = np.zeros((row-r,col-c),dtype=np.uint8)
    print(new_image.shape) 

    for i in range(row-r):
        for j in range(col-c):
            x = np.sum(np.multiply(img[i:3+i,j:3+j],kernal))
            if(x < 0):
                new_image[i][j] = 0
            elif(x > 255):
                new_image[i][j] = 255
            else:
                new_image[i][j] = x
    return new_image

def main(): 
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    #custom function:
    print(rgb.shape)
    avarage_kernal = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    r = rgb[:,:,0]
    red = custom_hist(r)
    print(gray.shape)

    custom_conv = convulation(gray,avarage_kernal)

    #builtin function :
    
    bu_red = cv2.calcHist([rgb],[0],None,[256],[0,256])
    bu_conv = cv2.filter2D(gray,-1,avarage_kernal)

    plt.subplot(2,2,1)
    plt.title("Custom hisogram Function")
    plt.plot(red.keys(),red.values(),'r')
    plt.subplot(2,2,2)
    plt.title("Using calcHist Function")
    plt.plot(bu_red,'r')

    plt.subplot(2,2,3)
    plt.title("Custom convulation Function")
    plt.imshow(custom_conv,cmap='gray')
    plt.subplot(2,2,4)
    plt.title("Using Built Function")
    plt.imshow(bu_conv,cmap='gray')
    plt.tight_layout()
    plt.show()







if __name__ == '__main__':
    main()
