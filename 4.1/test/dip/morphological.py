import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'mountain.jpeg'
    gray = cv2.cvtColor(plt.imread(img_path),cv2.COLOR_RGB2GRAY)
    _,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

    # binary2 = gray.copy()
    # binary2[binary2<127] = 0
    # binary2[binary2>=127] = 255

    
    img_set=[gray,binary]
    for i in range(len(img_set)):
        plt.subplot(1,3,i+1)
        plt.imshow(img_set[i],'gray')
    plt.show()


main()