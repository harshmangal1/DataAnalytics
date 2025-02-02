import numpy as np
arr = np.array([10,20,30,40])
print(arr)

# Slicing of arrays
print(arr[0:3])
print(arr[3:])

arr = np.array([[10,20,30,40],[50,60,70,80]])
print(arr[:2,:2])

arr = np.array([[10,20,30,40],[50,60,70,80],[20,40,60,80]])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)