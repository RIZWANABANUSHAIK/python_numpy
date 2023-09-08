import numpy as np
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
arr=np.zeros((R,C), dtype=np.int16)
# print(arr)
# print(arr.ndim)
k=1
for i in range(R):
    for j in range(C): 
        arr[i][j]=k
        k+=1

print(arr)
# def average(list):
#     return sum (list)/len(list)
    
# # list=[2,3,4,5] 
# list=[]
# n=int(input("enter the  no .of elements:"))
# for i in range(0,n):
#     ele=int(input("enter the elements:"))
#     list.append(ele)
# average=average(list)
# print("average og the list=",round(average,2))