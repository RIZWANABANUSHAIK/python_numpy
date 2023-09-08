import numpy as np

# zeros/ ones

# x = np.array([
#     [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]], [[13,14,15], [16,17,18]]],
#     [[[1,1,1], [1,1,1]], [[1,1,1], [1,1,1]], [[1,1,1], [1,1,1]]] 
# ])

# indexing elements
# print(x[0][1])
# print(x[0])
# print("")
# print("")
# print(x[0,1])
# print("")
# print("")
# print(x[0,1,0])
# print("")
# print(x[0,1,0,2])

# slicing arrays
# print(x[0][1:][1][0][:2])

# zero/ ones arrays based on shapes
# arr = np.zeros(5, dtype=np.int8)

# arr[2] = 120
# arr[4] = -87

# print(arr)


arr = np.zeros( (2,5) )
print(arr)

arr = np.zeros( (1,2,3,4) )
# print(arr)


arr = np.ones( (10,) ,dtype = np.uint16)
# print(arr)

# uint8 0 255
# int8 -128  +127

# uint16 0 65500
# int16 -32.7K +32.7K

# uint32 0 +4B
# int32 -2B  +2B

# for i in range(10):
#     arr[i] = (i+1)*4

# # print(arr)
# arr[4] = -1
# print(arr)

# print(arr.mean())
# print(arr.std())

# print((arr.std())**2)
