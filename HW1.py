import numpy as np
import imageio
import matplotlib.pyplot as plt
#import cv2

#read image
key1 = imageio.imread('key1.png')
key2 = imageio.imread('key2.png')
I = imageio.imread('I.png')
E = imageio.imread('E.png')
Eprime = imageio.imread('Eprime.png')


epoch = 1

weight = np.random.rand(3)#給weight 0到1之間的隨機數值

print(weight)

a = 0.00001
#learning rate
maxlterlimit = 3
#the maximal number of epochs allowed to train the network
size = key1.shape
H = size[0]#image height
W = size[1]#image width


while(epoch == 1 or epoch<maxlterlimit and np.any(np.absolute(weight[1]-weight[0]))>a):
    for i in range(0,H):
        for j in range(0,W):
            xk = [key1[i][j],key2[i][j],I[i][j]]
            ak = weight[0]*xk[0] + weight[1]*xk[1] + weight[2]*xk[2]
            e = E[i][j] - ak
            weight[0] = weight[0] + a*e*xk[0]
            weight[1] = weight[1] + a*e*xk[1]
            weight[2] = weight[2] + a*e*xk[2]
    
    print("epoch = ",epoch)
    epoch = epoch + 1

print("weight = ",weight)

finalpic = (Eprime-(weight[0]*key1)-(weight[1]*key2))/weight[2]
#equation(1)

plt.imshow(finalpic, cmap='gray')
plt.savefig("finalpic.png")






        