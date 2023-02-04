import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    path = 'mountain.jpeg'
    rgb = plt.imread(path)
    plt.subplot(2,4,1)
    plt.title('RGB')
    plt.imshow(rgb)

    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    plt.subplot(2,4,2)
    plt.title('GRAY')
    plt.imshow(grayscale,cmap='gray')
    
    hor = np.array([[2,10,2],[0,0,0],[-2,-10,-2]])

    ver = np.array([[-2,0,2],[-10,0,10],[-2,0,2]])

    box = np.ones((3,3))/9

    sharpen = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

    edge = np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])
    

    horizon = cv2.filter2D(grayscale,-1,hor)
    plt.subplot(2,4,3)
    plt.title('HORIZONTAL_OP')
    plt.imshow(horizon,cmap='gray')

    vertex= cv2.filter2D(grayscale,-1,ver)
    plt.subplot(2,4,4)
    plt.title('VERTEX_OP')
    plt.imshow(vertex,cmap='gray')

    box = cv2.filter2D(grayscale,-1,box)
    plt.subplot(2,4,5)
    plt.title('BLUR_OP')
    plt.imshow(box,cmap='gray')

    sharpen = cv2.filter2D(grayscale,-1,sharpen)
    plt.subplot(2,4,6)
    plt.title('SHARPEN_OP')
    plt.imshow(sharpen,cmap='gray')

    edge = cv2.filter2D(grayscale,-1,edge)
    plt.subplot(2,4,7)
    plt.title('EDGE_OP')
    plt.imshow(edge,cmap='gray')

    plt.savefig('result after convulation')
    plt.show()

if __name__ == '__main__':
    main()