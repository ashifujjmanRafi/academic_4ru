import matplotlib.pyplot as plt
import cv2
import numpy as np

def butterworthFilter(img):

    #converted to frequency domain
    #fd= fre domain
    #sd = spatial domain
    # sd = spatial domain, fd = frequency domain, fds = shifted frequency domain
    # hfds = high pass filtered in frequency domain shifted ,hfd = high pass filtered in frequency domain
    # hsd = high pass filtered in spatial domain
    #sd > fd > fds > h*fds > hfds > hfd > hsd

    fd = np.fft.fft2(img)
    fds = np.fft.fftshift(fd)
    fds_abs = np.log1p(np.abs(fds))

    #create butterworth lowpass filter
    m,n = img.shape
    h = np.zeros((m,n),dtype=np.float32)
    #cuttoff fre 
    d0 = 80
    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            h[u,v] = 1/(1+(d/d0)**2)
    # filtering image
    ffds = fds*h
    ffds_abs = np.log1p(np.abs(ffds))
    #converted to spatial domain
    ffd = np.fft.ifftshift(ffds)
    fsd = np.abs(np.fft.ifft2(ffd))


    #butterworth high pass filter
    hp = 1-h
    #filtering image
    hfds = fds*hp
    hfds_abs = np.log1p(np.abs(hfds))
    #converted to spatial domain
    hffd = np.fft.ifftshift(hfds)
    hsd = np.abs(np.fft.ifft2(hffd))

    img_set = [img,fds_abs,ffds_abs,fsd,hfds_abs,hsd]
    for i in range(len(img_set)):
        plt.subplot(2,3,i+1)
        plt.imshow(img_set[i],'gray')
    plt.savefig('butterworth.png')
    plt.show()



def gaussainFilter(img):      
    
    m,n = img.shape

    fd = np.fft.fft2(img)
    fds = np.fft.fftshift(fd)
    fds_abs = np.log1p(np.abs(fds))

    #create filter
    h = np.zeros((m,n),dtype=np.float32)
    d0 = 10 
    # cutoff fre
    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            h[u,v] = np.exp((-d**2)/(2*d0*d0))
    #filtered in fd
    ffds= fds*h
    ffds_abs = np.log1p(np.abs(ffds))
    #converted to spatial domain
    ffd = np.fft.ifftshift(ffds)
    fsd = np.abs(np.fft.ifft2(ffd))


    #high frequency
    hp = 1-h
    hffds = fds*hp
    hffds_abs = np.log1p(np.abs(hffds))

    hffd = np.fft.ifftshift(hffds)
    hfsd = np.abs(np.fft.ifft2(hffd))

    img_set = [img,fds_abs,ffds_abs,fsd,hffds_abs,hfsd]
    for i in range(len(img_set)):
        plt.subplot(2,3,i+1)
        plt.imshow(img_set[i],'gray')
    plt.savefig('gaussain.png')
    plt.show()






def main():
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    butterworthFilter(gray)
    gaussainFilter(gray)
    


if __name__ == "__main__":
    main()
