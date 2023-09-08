import numpy as np
x=np.array([
    [1,2],
    [3,4],
    [5,6]])
print(x.reshape(1,6))
print(x.reshape(6))
print(x.reshape(6,1))
print(x.reshape(2,3))
print(x.reshape(-1))#automatically all elements puts in a line



x=np.array([1,2,3,4,5,6,7,8])
print(x.reshape(4,-1))
print(x.reshape(2,2,2))
print(x.reshape(2,2,-1))#aytomatically find out the shape in place of -1