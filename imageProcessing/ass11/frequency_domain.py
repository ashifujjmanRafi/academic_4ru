from unicodedata import name
import matplotlib.pyplot as plt
import cv2
import numpy as np

def gaussaian(img):
    m,n = img.shape
    #fd = frequency domain
    #fds = centered frequency
    #h = filter
    #fdsh = filtered in frequency domain
    #fdh = invert shifted
    #sdh = invert in spatial domain

    fd = np.fft.fft2(img)
    fds = np.fft.fftshift(fd)
    #for printing centered frequency abs will need
    fds_abs = np.log1p(np.abs(fds))

    #now making the low pass filter
    h = np.zeros((m,n),dtype=np.float32)
    d0 = 70
    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            h[u,v] = np.exp((-d)**2/(2*d0**2))
    h_abs = np.log1p(np.abs(h))
    fdsh= fds*h
    #filtered in frequency domain
    fdsh_abs = np.log1p(np.abs(fdsh))

    #converted to sptial domain
    fdh = np.fft.ifftshift(fdsh)
    sdh = np.abs(np.fft.ifft2(fdh))

    #high pass filter
    hp = 1-h
    hp_abs = np.log1p(np.abs(hp))
    #filtered in frequency domain
    fdshp = fds*hp
    #filtered in spatial domain
    fdhp = np.fft.ifftshift(fdshp)
    sdhp = np.abs(np.fft.ifft2(fdhp))


    img_set = [img,fds_abs,h_abs,sdh,hp_abs,sdhp]
    img_title = ['original','centered frequency','low pass filter','low pass filtered','high pass filter','high pass filtered']
    for i in range(len(img_set)):
        plt.subplot(3,2,i+1)
        plt.title(img_title[i])
        plt.imshow(img_set[i],'gray')
    plt.tight_layout()
    plt.savefig('gaussaian.png')
    plt.show()





def butterworth(img):
    m,n = img.shape
    h = np.zeros((m,n),dtype=np.float32)
    fd = np.fft.fft2(img)
    fds = np.fft.fftshift(fd)
    fds_abs = np.log1p(np.abs(fds))
    d0 = 30
    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            h[u,v] = 1/(1+(d/d0)**2)
    h_abs = np.log1p(np.abs(h))
    fdsh = fds*h
    fdh = np.fft.ifftshift(fdsh)
    sdh = np.abs(np.fft.ifft2(fdh))

    #highpass butterworth 
    hp = 1-h
    hp_abs = np.log1p(np.abs(hp))
    fdshp = fds*hp
    fdhp = np.fft.ifftshift(fdshp)
    sdhp = np.abs(np.fft.ifft2(fdhp))

    img_set = [img,fds_abs,h_abs,sdh,hp_abs,sdhp]
    img_title = ['original','centered frequency','butterworth lp filter','low pass filtered','butterworth hp filter','high pass filtered']
    for i in range(len(img_set)):
        plt.subplot(3,2,i+1)
        plt.title(img_title[i])
        plt.imshow(img_set[i],'gray')
    plt.tight_layout()
    plt.savefig('butterworth.png')
    plt.show()

def main():
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    gaussaian(gray)
    butterworth(gray)
if __name__=='__main__':
    main()