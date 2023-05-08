import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = "mountain.jpeg"
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    _,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    print(binary.shape)

    red = cv2.calcHist([rgb],[0],None,[256],[0,256])
    green = cv2.calcHist([rgb],[1],None,[256],[0,256])
    blue = cv2.calcHist([rgb],[2],None,[256],[0,256])
    gray = cv2.calcHist([gray],[0],None,[256],[0,256])

    plot_set = [red,green,blue,gray]
    for i in range(len(plot_set)):
        plt.subplot(2,2,1)
        plt.plot(plot_set[i])
    plt.show()
main()