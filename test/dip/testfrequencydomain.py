import matplotlib.pyplot as plt 
import cv2
import numpy as np 

def butterworth(img):
    m , n = img.shape
    fd = np.fft.fft2(img)
    fds = np.fft.fftshift(fd)
    
    h = np.zeros((m,n),dtype = np.float32)
    d0 = 50
    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            h[u,v] = 1/(1+(d/d0)**2)
    h_abs = np.log1p(np.abs(h))

    fdsh = fds*h
    fdh = np.fft.ifftshift(fdsh)
    sdh = np.abs(np.fft.ifft2(fdh))

    hp = 1 - h
    hp_abs = np.log1p(np.abs(hp))
    fdshp = fds*hp
    fdhp = np.fft.ifftshift(fdshp)
    sdhp = np.abs(np.fft.ifft2(fdhp))

    img_set = [img,h_abs,sdh,hp_abs,sdhp]
    for i in range(len(img_set)):
        plt.subplot(3,2,i+1)
        plt.imshow(img_set[i],'gray')
    plt.savefig('butterworth filter')
    plt.show()

def gaussain(img):
    m , n = img.shape
    fd = np.fft.fft2(img)
    fds = np.fft.fftshift(fd)
    
    h = np.zeros((m,n),dtype = np.float32)
    d0 = 10
    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            h[u,v] = np.exp(-(d**2)/(2*d0*d0))
    h_abs = np.log1p(np.abs(h))

    fdsh = fds*h
    fdh = np.fft.ifftshift(fdsh)
    sdh = np.abs(np.fft.ifft2(fdh))

    hp = 1 - h
    hp_abs = np.log1p(np.abs(hp))
    fdshp = fds*hp
    fdhp = np.fft.ifftshift(fdshp)
    sdhp = np.abs(np.fft.ifft2(fdhp))

    img_set = [img,h_abs,sdh,hp_abs,sdhp]
    for i in range(len(img_set)):
        plt.subplot(3,2,i+1)
        plt.imshow(img_set[i],'gray')
    plt.savefig('gaussain filter')
    plt.show()

def histogram(img):
    r,c = img.shape
    





def main():
    img_path = "mountain.jpeg"
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    # butterworth(gray)
    # gaussain(gray)
if __name__ =='__main__':
    main()