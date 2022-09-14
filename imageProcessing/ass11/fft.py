import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    
    #converted to frequency domain
    fd = np.fft.fft2(gray)
    fds= np.fft.fftshift(fd)

    #abs valu for ploting
    fd_abs = np.log1p(np.abs(fd))
    fds_abs = np.log1p(np.abs(fds))

    #gaussain filter
    m,n = gray.shape
    h = np.zeros((m,n),dtype=np.float32)

    # cuttoff f = 10
    d0 = 80 
    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            h[u,v] = np.exp((-d**2)/(2*d0*d0))
    
    #filtered in fd
    gs = fds*h
    gs_abs = np.log1p(np.abs(gs))

    #inverse fft
    g = np.fft.ifftshift(gs)
    filtered_gray = np.abs(np.fft.ifft2(g))

    #high pass filter
    hp = 1-h
    hgs = fds*hp
    hgs_abs = np.log1p(np.abs(hgs))
    hg = np.fft.ifftshift(hgs)
    hg_abs = np.log1p(np.abs(hg))

    #inverse fft
    hfiltered_gray = np.abs(np.fft.ifft2(hg))


    img_set = [gray,fd_abs,fds_abs,gs_abs,filtered_gray,hp,hg_abs,hgs_abs,hfiltered_gray]
    for i in range(len(img_set)):
        plt.subplot(5,2,i+1)
        plt.imshow(img_set[i],'gray')
    plt.show()





if __name__ == "__main__":
    main()