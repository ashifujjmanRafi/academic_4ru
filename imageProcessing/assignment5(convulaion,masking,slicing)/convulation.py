import cv2 
import matplotlib.pyplot as plt
import numpy as np

def main():
    path = 'mountain.jpeg'
    rgb = plt.imread(path)

    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    laplacian1 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    lap1 = cv2.filter2D(grayscale,-1,laplacian1)

    laplacian2 = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    lap2 = cv2.filter2D(grayscale,-1,laplacian2)

    laplacian3 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    lap3 = cv2.filter2D(grayscale,-1,laplacian3)

    laplacian4 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    lap4 = cv2.filter2D(grayscale,-1,laplacian4)

    shovel1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    sov1 = cv2.filter2D(grayscale,-1,shovel1)
    shovel2 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    sov2 = cv2.filter2D(grayscale,-1,shovel2)


    img_set = [rgb,grayscale,lap1,lap3,lap2,lap4,sov1,sov2]
    img_tittle = ["RGB","GRAY","LAPLACIAN1","LAPLACIAN2","LAPLACIAN3","LAPLACIAN4","SOBEL1","SOBEL2"]

    plot_show(img_set,img_tittle)


def plot_show(img_set,img_tittle):

    n = len(img_set)
    
    for i in range(n):

        plt.subplot(4,2,i+1)
        plt.title(img_tittle[i])
        plt.imshow(img_set[i],'gray')
    plt.savefig("A3")
    plt.show()


if __name__ == '__main__':
    main()