import matplotlib.pyplot as plt
import cv2
import numpy as np

def frequencydomain(img):
    r,c = img.shape
    #fd = frequency domain
    #fds = centered frequency
    #h = filter
    #fdsh = filtered in frequency domain
    #fdh = invert shifted
    #sdh = invert in spatial domain
    fd = np.fft.fft2(img)
    fds = np.fft.fftshift(fd)
    #for printing fds_abs=np.log1p(np.abs(fds))
    #making low pass filter

    #butterworth filter
    h = np.zeros((r,c),dtype=np.float32)
    d0 = 20
    for u in range(r):
        for v in range(c):
            d = np.sqrt((u-r/2)**2+(v-c/2)**2)
            h[u,v]=1/(1+(d/d0)**2)
    #for printing 
    h_abs=np.log1p(np.abs(h))
    #filtered in frequency domain
    fdsh = fds*h_abs
    #for printing fdsh_abs=np.log1p(np.abs(fdsh))
    #inverse in spatial domain
    #inverse shifting
    fdh = np.fft.ifftshift(fdsh)
    #spatial domain
    sdh = np.abs(np.fft.ifft2(fdh))

    #high pass filter
    hp = 1 - h
    hp_abs = np.log1p(np.abs(hp))
    #filtered in frequency domain
    fdshp =  fds*hp
    fdhp = np.fft.ifftshift(fdshp)
    sdhp = np.abs(np.fft.ifft2(fdhp))

    img_set = [img,h_abs,sdh,hp_abs,sdhp]
    imshow(img_set,2,3)


    #gaussain filter
    h = np.zeros((r,c),dtype=np.float32)
    d0 = 40
    for u in range(r):
        for v in range(c):
            d = np.sqrt((u-r/2)**2+(v-c/2)**2)
            h[u,v] = np.exp(-(d**2)/(2*d0*d0))

    h_abs = np.log1p(np.abs(h))
    fdsh = fds*h
    fdh = np.fft.ifftshift(fdsh)
    sdh = np.abs(np.fft.ifft2(fdh))
    #highpass
    hp = 1 - h
    hp_abs = np.log1p(np.abs(hp))
    fdshp = fds*hp
    fdhp = np.fft.ifftshift(fdshp)
    sdhp = np.abs(np.fft.ifft2(fdhp))

    img_set = [img,h_abs,sdh,hp_abs,sdhp]
    imshow(img_set,2,3)




def imshow(img_set,x,y):
    for i in range(len(img_set)):
        plt.subplot(x,y,i+1)
        plt.imshow(img_set[i],'gray')
    plt.savefig('result')
    plt.show()

def plotshow(plt_list,x,y):
    for i in range(len(plt_list)):
        plt.subplot(x,y,i+1)
        plt.plot(plt_list[i],'red')
    plt.show()


def main():
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    frequencydomain(gray)
    


if __name__ == "__main__":
    main()
