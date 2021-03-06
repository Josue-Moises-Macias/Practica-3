import numpy as np
from matplotlib import pyplot as plt
import cv2 #opencv

imagen1 = cv2.imread('mar.png')
imagen1_out= cv2.resize(imagen1,(400,200),interpolation= cv2.INTER_CUBIC)
imagen2 = cv2.imread('espacio.png')
imagen2_out= cv2.resize(imagen2,(400,200),interpolation= cv2.INTER_CUBIC)
res1 = cv2.resize(imagen1, (400,200), interpolation = cv2.INTER_CUBIC)
res2 = cv2.resize(imagen2, (400,200), interpolation = cv2.INTER_CUBIC)
suma_f = cv2.add(res1,res2) #suma
eg1 = cv2.cvtColor(imagen1, cv2.COLOR_RGB2GRAY)
eg2 = cv2.cvtColor(imagen2, cv2.COLOR_RGB2GRAY)
eg3 = cv2.cvtColor(suma_f, cv2.COLOR_RGB2GRAY)

#h1=cv2.calcHist([eg1],[0],None,[400],[0,255])
#h2=cv2.calcHist([eg2],[0],None,[400],[0,255])
#h3=cv2.calcHist([eg1],[0],None,[400],[0,255])
cv2.imshow('MAR1',imagen1_out)
cv2.imshow('ESPACIO1',imagen2_out)
cv2.imshow('SUMA1',suma_f)

fig=plt.figure(1)
width, height = eg1.shape
x = np.linspace(0,255, num=256, dtype = np.uint8)
y = np.zeros(256)
mejor = np.zeros(eg1.shape,eg1.dtype)
for w in range (width):
    for h in range (height):
        v = eg1[w,h]
        y[v] = y [v]+1;
plt.bar(x,y)
#k=255/(width*height)
#sumatoria1=0
#for w in range (width):
#    for h in range (height):
#        for s in range (eg1[w,h]):
#            sumatoria1 = sumatoria1 + y[s]
#        mejor[w,h] = k*sumatoria1
#        sumatoria1=0
#cv2.imshow ('MAR1', cv2.hconcat([imagen1_out,mejor]))
#pl1=fig.add_subplot(311)
#pl1.plot(h1)
plt.title('HISTOGRAMA MAR')
fig=plt.figure(2)
width, height = eg2.shape
x = np.linspace(0,255, num=256, dtype = np.uint8)
y = np.zeros(256)
for w in range (width):
    for h in range (height):
        v = eg2[w,h]
        y[v] = y [v]+1;
plt.bar(x,y)
#pl1=fig.add_subplot(311)
#pl1.plot(h2)
plt.title('HISTOGRAMA ESPACIO')
fig=plt.figure(3)
width, height = eg3.shape
x = np.linspace(0,255, num=256, dtype = np.uint8)
y = np.zeros(256)
for w in range (width):
    for h in range (height):
        v = eg3[w,h]
        y[v] = y [v]+1;
plt.bar(x,y)
#pl1=fig.add_subplot(311)
#pl1.plot(h3)
plt.title('HISTOGRAMA SUMA')
plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()
plt.close(fig)

