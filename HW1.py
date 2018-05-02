import numpy as np
import cv2
#import matplotlib.pyplot as plt

#read image
key1 = cv2.imread('key1.png')
key2 = cv2.imread('key2.png')
imgI = cv2.imread('I.png')
imgE = cv2.imread('E.png')
imgEprime = cv2.imread('Eprime.png')

cv2.imshow('image',key1)
cv2.waitKey(0)
cv2.destroyAllWindows()

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

#wk
#xk
#ak

while(epoch == 1 or epoch<maxlterlimit and w[0]-w[1]>a):
    for i in range[0,W]:
        for j range[0,H]:
            x[i,j] = [k1[i,j],k2[i,j],I[i,j]]
            ak[i,j] = w[i,j]*x[i,j]
            e[i,j] = E[i,j] - ak[i,j]
            w[i+1,j+1] = w[i,j] + a*e[i,j]*x[i,j]
    epoch = epoch + 1





        