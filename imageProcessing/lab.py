import matplotlib.pyplot as plt
import numpy as np

def main():
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    red = rgb[:,:,0]
    green = rgb[:,:,1]
    blue = rgb[:,:,2]
    r,c = red.shape
    gray = np.zeros((r,c))

    gray = .299*red + .587*green +.114* blue

    print(red.max(),red.min())
    
    img_set = [rgb,red,green,blue,gray]
    img_tittle = ['RGB','RED','GREEN','BLUE','GRAY']
    
    for i in range(len(img_set)):
        plt.subplot(2,3,i+1)
        if(i==0):
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i],'gray')
        plt.title(img_tittle[i])

    plt.show()
    

if __name__ =='__main__':
    main()
