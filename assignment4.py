import numpy as np
from numpy import random
x=random.randint(1,8,(1,2))
y=random.randint(1,8,(1,2))
print(x,x.shape)
print(y,y.shape)
z=np.dstack((x,y))
a=z.reshape(2,2)
print(a,a.shape)
x1,y1=(a[0][0],a[0][1])
x2,y2=(a[1][0],a[1][1])
# print(x1)
# print(y1)
z1=np.zeros((x1,y1), dtype=np.int16)
z2=np.zeros((x2,y2), dtype=np.int16)
k=1
for i in range(x1):
    for j in range(y1): 
        z1[i][j]=k
        k+=1
k1=1
print(z1,z1.shape)
# for i in range(x2):
#     for j in range(y2): 
#         z2[i][j]=k1
#         k1+=1

# print(z2,z2.shape)
l=[]
for i in range(1,x1*y1):
    l.append(i)
print(l) 
arr=np.array(l)   
print(arr)
out=arr.reshape(x1,y1)
print(out)