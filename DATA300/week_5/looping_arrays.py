import numpy as np

#looping a 1d array
arr1 = np.array([1, 2, 3, 4])
#print the array
print(arr1)
#display the shape(dimensions) of the array
print( np.shape(arr1) )

#loop through the 1 dimensional array
for i in range(np.shape(arr1)[0]):
    print(arr1[i])

#A two dimensional array
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr2)
print( np.shape(arr2) )

#two nested loops to access all elements of
# the two dimensional array ar2
for ii in range(np.shape(arr2)[0]):
    for jj in range(np.shape(arr2)[1]):
        print(arr2[ii,jj])
        

#Exercise on Looping three dimensional Numpy Arrays
#import numpy as np only needed if not imported already:
import numpy as np
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
all_elements = [arr3[i][j][k] for i in range(arr3.shape[0]) for j in range(arr3.shape[1]) for k in range(arr3.shape[1])]
# all_elements_2 = [i for i in arr3.flat] # faster option

