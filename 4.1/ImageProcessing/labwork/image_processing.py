import matplotlib.pyplot as plt
import cv2
def main():
    img_path = "mountain.jpeg"
    print(img_path)
    rgb = plt.imread(img_path)
    
    red = rgb[:,:,0]
    green = rgb[:,:,1]
    blue = rgb[:,:,2]
    print(red.shape)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(gray.shape)
    red = rgb[:,:,0]
    green = rgb[:,:,1]
    blue=rgb[:,:,2]
    print(blue.shape)

    r = cv2.calcHist([rgb],[0],None,[256],[0,256])
    g = cv2.calcHist([rgb],[1],None,[256],[0,256])
    b = cv2.calcHist([rgb],[2],None,[256],[0,256])
    gra = cv2.calcHist([gray],[0],None,[256],[0,256])
    rr = cv2.calcHist([red],[0],None,[256],[0,256])
    img_show = [r,g,b,gra,rr]
    img_set = [rgb,gray,red,green,blue]
    img_title=["rgb","gray","red","green","blue"]
    show_title=["red","green","blue","gray","red"]

    for i in range(len(img_set)):
        plt.subplot(2,5,i+1)
        plt.title(img_title[i])
        plt.imshow(img_set[i],'gray')
        

        plt.subplot(2,5,i+6)
        plt.title(show_title[i])
        plt.plot(img_show[i])
        
    plt.tight_layout()
    plt.show()






if __name__ == '__main__':
    main()
