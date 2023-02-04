import matplotlib.pyplot as plt
import cv2
import numpy as np

def cus_ero(img,kernal):
    r,c = img.shape
    x,y = kernal.shape
    out = np.zeros((r-x-1,c-y-1))

    for i in range(r-x-1):
        for j in range(c-y-1):
            sum = np.sum(np.multiply(img[i:i+x,j:j+y],kernal))
            if(sum==2295):
                out[i][j]=255          
    return out
def cus_dila(img,kernal):
    r,c=img.shape
    x,y = kernal.shape
    out = np.zeros((r-x-1,c-y-1))
    for i in range(r-x-1):
        for j in range(c-y-1):
            sum=np.sum(np.multiply(img[i:i+x,j:j+y],kernal))
            if(sum>=255):
                out[i][j]=255
    return out

def main():
    img_path = "mountain.jpeg"
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    _,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    r,c=gray.shape
    print(gray.shape)

    kernal = np.ones((3,3),dtype = np.uint8)

    out1 = cus_ero(binary,kernal)
    out2 = cv2.erode(binary,kernal)

    out3 = cus_dila(binary,kernal)
    out4 = cv2.dilate(binary,kernal)
    img_set = [out1,out2,out3,out4]
    for i in range(len(img_set)):
        plt.subplot(2,2,i+1)
        plt.imshow(img_set[i],'gray')
    plt.show()



if __name__ == "__main__":
    main()