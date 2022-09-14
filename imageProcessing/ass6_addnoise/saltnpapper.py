import matplotlib.pyplot as plt
import cv2
import numpy as np


def histo(img):
    d = dict()
    for i in range(256):
        d[i]=0
    for i in img:
        for j in i:
            d[j] += 1
    return d

def saltnpaper(img):
    # print(img.shape)
    r,c = img.shape
    out_img = img.copy()
    t = (r*c)//50
    for i in range(t):
        x = np.random.randint(0,r)
        y = np.random.randint(0,c)
        if(i%2==0):
            out_img[x][y] = 255
        else:
            out_img[x][y]=0

    avg_kernal = np.ones((3,3))/9
    out = cv2.filter2D(img,-1,avg_kernal)
    print(avg_kernal)
    plt.subplot(2,2,1)
    plt.imshow(out,'gray')
    plt.show()

def erosion(img,kernal):
    r,c = img.shape
    x,y = kernal.shape
    cutoff = np.sum(kernal) * 255
    ero_out = np.zeros((r-x+1,c-y+1),dtype=np.uint8)
    for i in range(r-x+1):
        for j in range(c-y+1):
            sum = np.sum(np.multiply(img[i:i+x , j:j+y],kernal))
            if(sum==cutoff):
                ero_out[i][j]=255
    return ero_out

def dialation(img,kernal):
    r,c = img.shape
    x,y = kernal.shape
    dia_out = np.zeros((r-x+1,c-y+1),dtype=np.uint8)
    for i in range(r-x+1):
        for j in range(c-y+1):
            sum = np.sum(np.multiply(img[i:i+x , j:j+y],kernal))
            if(sum>=255):
                dia_out[i][j]=255
    return dia_out

def morphological_op(img,kernal):
    ero_out = erosion(img,kernal)
    dia_out = dialation(img,kernal)

    clo = erosion(dia_out,kernal)
    opn = dialation (ero_out,kernal)

    img_set = [ero_out,dia_out,opn,clo]
    for i in range(len(img_set)):
        plt.subplot(2,2,i+1)
        plt.imshow(img_set[i],'gray')
    plt.show()

def noise(img):
    r,c = img.shape
    t = (r*c) // 50
    out = img.copy()
    for i in range(t):
        x = np.random.randint(0,r)
        y = np.random.randint(0,c)
        if(i%2):
            out[x][y] = 255
        else:
            out[x][y] = 0

    plt.imshow(out)
    plt.show()

def main():
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
   
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    
    # saltnpaper(gray)
    kernal = np.ones((3,3),dtype=np.uint8)
    _,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    # morphological_op(binary,kernal)
    print(binary.shape)
    equlizehist(gray)

def equlizehist(img):

    g_hist = cv2.calcHist([img],[0],None,[256],[0,256])
    
    r,c = img.shape
    img_size = r*c
    cdf = g_hist.cumsum()
    cdf_min = cdf.min()

    equ_img = img.copy()
    for i in range(r):
        for j in range(c):
            equ_img[i,j]=((cdf[img[i,j]]-cdf_min)/(img_size-cdf_min))*255
    
    # equ_hist = cv2.calcHist([equ_img],[0],None,[256],[0,256])
    equ_hist = histo(equ_img)
    plt.plot(equ_hist.keys(),equ_hist.values())
    plt.show()



   


if __name__ =='__main__':
    main()

