print('========================================')
print('Q1')

#  Import numpy as np and print the version number.

import numpy as np
print('NumPy version : {}'.format(np.__version__))

print('========================================')
print('Q2')

# Create a 1D array of numbers from 0 to 9

arr1 = np.arange(10)
print('Array : {}'.format(arr1))

print('========================================')
print('Q3')

# Create a 3×3 numpy array of all True’s

arr2 = np.ones((3,3))
arr3 = (arr2 == 1)
print('Array :\n{}'.format(arr3))

print('========================================')
print('Q4')

# Extract all odd numbers from arr

arr4 = np.arange(10)
print('Array : {}'.format(arr4))

arr5 = arr4[arr4%2 == 1]
print('Array of only odd numbers: {}'.format(arr5))

print('========================================')
print('Q5')

# Replace all odd numbers in arr with -1

arr6 = np.arange(10)
print('Array : {}'.format(arr6))

arr6[arr6%2 == 1] = -1
print('New Array that replaced odd numbers w/ -1 : {}'.format(arr6))

print('========================================')
print('Q6')

arr7 = np.arange(10)
print('Array (arr7): {}'.format(arr7))

arr8 = np.copy(arr7)
arr8[arr8%2 == 1] = -1
print('New Array that replaced odd numbers w/ -1 : {}'.format(arr8))

print('Original array (arr7) : {}'.format(arr7))

print('========================================')
print('Q7')

# Convert a 1D array to a 2D array with 2 rows

arr9 = np.arange(10)
print('1D array :\n{}'.format(arr9))

arr10 = np.reshape(arr9,(2,5))
print('2D array :\n{}'.format(arr10))

print('========================================')
print('Q8')

# Stack arrays a and b vertically

arr11 = np.reshape(np.arange(10),(2,5))
print('top part of the array:\n{}'.format(arr11))

arr12 = np.reshape(np.arange(10,20),(2,5))
print('bottom part of the array:\n{}'.format(arr12))

arr13 = np.vstack((arr11,arr12))
print('Arrays stacked vertically:\n{}'.format(arr13))

print('========================================')
print('Q9')

# Stack arrays a and b horizontally

arr14 = np.reshape(np.arange(10),(2,5))
print('left part of the array:\n{}'.format(arr14))

arr15 = np.reshape(np.arange(10,20),(2,5))
print('right part of the array:\n{}'.format(arr15))

arr16 = np.hstack((arr14,arr15))
print('Arrays stacked horizontally:\n{}'.format(arr16))

print('========================================')
print('Q10')

# Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
# a = np.array([1,2,3])
# custom array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

a = np.array([1,2,3])
print('a : {}'.format(a))
arr17 = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print('custom array : {}'.format(arr17))

print('========================================')
print('Q11')

# Get the common items between a and b

arr18 = np.arange(10)
print('First array : {}'.format(arr18))

arr19 = np.arange(7,17)
print('Second array : {}'.format(arr19))

arr20 = np.intersect1d(arr18,arr19)
print('Common number of the two arrays : {}'.format(arr20))

print('========================================')
print('Q12')

# From array a remove all items present in array b

arr21 = np.arange(10)
print('Array : {}'.format(arr21))
arr22 = np.array([3,7,8])
print('The number I want to remove : {}'.format(arr22))

arr23 = np.unique(arr22)
arr24 = np.setdiff1d(arr21,arr23)
print('The new array : {}'.format(arr24))

print('========================================')
print('Q13')

# Get the positions where elements of a and b match

# arr25 = np.arange(1,11)
arr25 = np.array([1,2,3,4,5,6,7,8,9])
print('First array : {}'.format(arr25))
arr26 = np.array([3,7,8,3,5,3,6,3,9])
print('Second Array : {}'.format(arr26))

"""
l1 = len(arr26)
arr27 = []
arr26[0]
for i1 in range(l1):
    t1 = np.where(arr25 == arr26[i1])
    arr27 += t1
print('Position of the elements :\n{}'.format(arr27))
"""

arr27 = np.where(arr26 == arr25)
print(arr27)
print('========================================')
print('Q14')

# Get all items between 5 and 10 from a.
# a = np.arange(20)

arr28 = np.arange(20)
print('a : {}'.format(arr28))
arr29 = arr28[(5 <= arr28) & (arr28 <= 10)]
# arr29 = arr28(np.logical_and(5 <= arr28,arr28 <= 10))
print('Array between 5 and 10 : {}'.format(arr29))

print('========================================')
print('Q15')

# Convert the function maxx that works on two scalars, to work on two arrays.

arr30 = np.random.randint(0,100,10)
print('First array : {}'.format(arr30))

arr31 = np.random.randint(0,100,10)
print('Second array : {}'.format(arr31))

def max_number_of_the_array_and_also_this_question_took_me_a_very_very_very_long_time_to_understand_it_lol(a, b):
    a1 = np.max(a)
    b1 = np.max(b)
    if a1 >= b1:
        return a1
    else:
        return b1

max_number = max_number_of_the_array_and_also_this_question_took_me_a_very_very_very_long_time_to_understand_it_lol(arr30,arr31)

print('The biggest number of the two arrays : {}'.format(max_number))

print('========================================')
print('Q16')

# Swap columns 1 and 2 in the array arr.

arr34 = np.arange(8).reshape(2,4)
print('2D array :\n{}'.format(arr34))

arr35 = arr34[[1,0],:]
print('Reverced array :\n{}'.format(arr35))

print('========================================')
print('Q17')

# Swap rows 1 and 2 in the array arr:

arr32 = np.arange(8).reshape(4,2)
print('2D array :\n{}'.format(arr32))

arr33 = arr32[:,[1,0]]
print('Reverced array :\n{}'.format(arr33))

print('========================================')
print('Q18')

# Reverse the rows of a 2D array arr.

arr36 = np.arange(16).reshape(4,4)
print('2D array :\n{}'.format(arr36))

arr37 = arr36[:,::-1]
print('Reverced array :\n{}'.format(arr37))

print('========================================')
print('Q19')

# Reverse the columns of a 2D array arr.

arr38 = np.arange(16).reshape(4,4)
print('2D array :\n{}'.format(arr38))

arr39 = arr38[::-1,:]
print('Reverced array :\n{}'.format(arr39))

print('========================================')
print('Q20')

# Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.

arr40 = np.random.uniform(5,10,(5,3))
print('2D array:\n{}'.format(arr40))

print('========================================')
print('Q21')

# Print or show only 3 decimal places of the numpy array rand_arr.

arr41 = np.random.random((5,3))
np.set_printoptions(precision=3)
print('2D array :\n{}'.format(arr41))

print('========================================')
