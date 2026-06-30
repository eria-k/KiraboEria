import numpy as np
print(np.__version__)
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
for i in arr:
    for j in i:
        print(j,end=" ")
    print()
print(arr.dtype)
    