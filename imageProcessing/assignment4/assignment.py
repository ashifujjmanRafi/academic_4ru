import numpy as np
import matplotlib.pyplot as plt
import cv2 



def histo(img):
    d = dict()
    for x in range(256):
        d[x] = 0  
    for x in img:
        for y in x:
            d[y] += 1
    return d


def conv(mat, kernel):
    row, col = mat.shape
    
    r, c = kernel.shape[0] // 2, kernel.shape[1] // 2
    r, c = r * 2, c * 2

    new_image = np.zeros((row - r, col - c), dtype=np.uint8)

    for i in range(row - r):
        for j in range(col - c):
            x = np.sum(np.multiply(mat[i:3+i, j:3+j], kernel))
            if x<0:
                new_image[i][j] =0
            elif x>255:
                new_image[i][j] =255
            else:
                new_image[i][j] = x
            
    return new_image 



def main():
    path = 'mountain.jpeg'
    rgb = plt.imread(path)

    red = rgb[:,:,0]
    red_dict = histo(red)
    plt.subplot(2,2,1)
    plt.title("Custom hisogram Function")
    plt.plot(red_dict.keys(), red_dict.values(), 'r')
    
    red = cv2.calcHist([rgb], [0], None, [256], [0, 256])
    plt.subplot(2,2,2)
    plt.title("Using calcHist Function")
    plt.plot(red, 'r')
    


    #2nd part:
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

    sharpen_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    
    sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
    plt.subplot(2,2,3)
    plt.title("Using Built Function")
    plt.imshow(sharpen, cmap='gray')

    sharpen_custom = conv(gray, sharpen_kernel)

    plt.subplot(2,2,4)
    plt.title("custom Function")
    plt.imshow(sharpen_custom, cmap='gray')
    plt.savefig("result")
    plt.show()

if __name__ == '__main__':
    main()
