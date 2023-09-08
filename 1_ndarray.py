import numpy
# Numerical Python
# based on Arrays
# uses C internally so very fast

x = [1,2,3,4,5]
y = numpy.array(x)
print(y, y.ndim, y.shape, y.dtype)


x2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
y2 = numpy.array(x2)
print(y2, y2.ndim, y2.shape)


y3 = numpy.array([
    [ [1,2], [3,4]],
    [ [5,6], [7,8] ],
    [ [9,10], [11,12]]
])
print(y3, y3.ndim, y3.shape)


x = numpy.array(
    [
       [[ [1,1,1], [1,1,1] ], [[1,1,1], [1,1,1]], [[1,1,1], [1,1,1]]],
       [[ [1,1,1], [1,1,1]], [[1,1,1], [1,1,1]], [[1,1,1], [1,1,1]]] 
    ]
)

print(x, x.dtype, x.ndim, x.shape)

