import matplotlib.pyplot as plt
import cv2
import numpy as np

def imgcompress(img):
    img_set = [img]
    img_title = ["Original"]
    
    fd = np.fft.fft2(img)
    fd_sort = np.sort(np.abs(fd.flatten()))
    size = len(fd_sort)

    for keep in (.7,.4,.2,.1,.05):

        thresh = fd_sort[int(np.floor(size*(1-keep)))]
        index = np.abs(fd) > thresh
        compressed = fd*index
        after_com = np.fft.ifft2(compressed).real
        print(after_com.size)

        img_set.append(after_com)
        img_title.append("Keep: "+str(keep*100)+"%")
    
    for i in range(len(img_set)):
        plt.subplot(3,2,i+1)
        plt.imshow(img_set[i],cmap="gray")
        plt.title(img_title[i])
    plt.tight_layout()
    plt.savefig("output.png")
    plt.show()
    

def main():
    img_path = "mountain.jpeg"
    rgb = cv2.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    imgcompress(gray)

if __name__ == "__main__":
    main()