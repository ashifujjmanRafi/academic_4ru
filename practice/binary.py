import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    img_path = "mountain.jpg"
    rgb = plt.imread(img_path)
    print(rgb.shape)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    _, bi1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    print(bi1)
    bi2 = gray.copy()
    bi2[bi2 < 127] = 0
    bi2[bi2 > 127] = 1

    print(bi1[99:100, :300])

    r, c = gray.shape

    bi3 = np.zeros((r, c), dtype=np.uint8)

    for i in range(r):
        for j in range(c):
            if(gray[i][j] < 127):
                bi3[i][j] = 0
            else:
                bi3[i][j] = 255

    plt.subplot(1, 2, 1)
    plt.imshow(bi2, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.imshow(bi3, 'gray')
    plt.show()


main()
