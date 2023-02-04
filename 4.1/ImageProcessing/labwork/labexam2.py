import matplotlib.pyplot as plt
import cv2
import numpy as np


def equhist(img):
    r,c = img.shape
    img_size = r*c
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    cdf = hist.cumsum()
    cdf_min = cdf.min()

    equ_img = img.copy()
    for i in range(r):
        for j in range(c):
            equ_img[i,j] = ((cdf[img[i,j]]-cdf_min)/(img_size-cdf_min))*255

    equ_hist = cv2.calcHist([equ_img],[0],None,[256],[0,256])
    plt.plot(equ_hist)
    # plt.plot(equ_hist.keys(),equ_hist.values())
    plt.show()

def erosion(img,kernal):
    r,c = img.shape
    x,y = kernal.shape
    val = np.sum(kernal)*255  
    out = np.zeros((r-x+1,c-y+1),dtype=np.uint8)
    for i in range(r-x+1):
        for j in range(c-y+1):
            sum = np.sum(np.multiply(img[i:i+x,j:j+y],kernal))
            if(sum==val):
                out[i][j]=255
    return out

def dialation(img,kernal):
    r,c = img.shape
    x,y = kernal.shape
    out = np.zeros((r-x+1,c-y+1),dtype=np.uint8)
    for i in range(r-x+1):
        for j in range(c-y+1):
            sum = np.sum(np.multiply(img[i:i+x,j:j+y],kernal))
            if(sum>=255):
                out[i][j]=255
    return out

def butterworth(img):

    fd = np.fft.fft2(img)
    
    fds = np.fft.fftshift(fd)
    fd_abs = np.log1p(np.abs(fds))

    m,n = img.shape
    h = np.zeros((m,n),dtype=np.float32)
    d0 = 50
    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            h[u,v]=np.exp((-d**2)/(2*d0**2))
            # h[u,v] = 1/(1+(d/d0)**2)
    
    #filtered image
    hfds = h*fds
    
    #ifft
    hfd = np.fft.ifftshift(hfds)
    hsd = np.abs(np.fft.ifft2(hfd))

    #high pass fft
    hp = 1-h
    hpfds = hp*fds
    #ifft
    hpfd = np.fft.ifftshift(hpfds)
    hpsd = np.abs(np.fft.ifft2(hpfd))

    #img show
    img_set = [img,fd_abs,hsd,hpsd]
    img_title = ['original','fft','butterworth','high pass']
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(img_set[i],cmap='gray')
        plt.title(img_title[i])
    plt.show()

    
    


def main():
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    _,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    kernal = np.ones((3,3),dtype=np.uint8)
    butterworth(gray)





if __name__ == '__main__':
    main()