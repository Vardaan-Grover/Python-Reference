# Numpy Exercises and Boolean Masking


# %%
import numpy as np
# Load data from file
filedata = np.genfromtxt('C:/Users/coolv/Documents/Python/data.txt', delimiter=',')
print(filedata)
print()
# Copying the data in a particular format as specified
filedata = filedata.astype('int32')
print(filedata)


# %%
# Boolean Masking and Advance Indexing
true_false = filedata<50
print(true_false)


# %%
print(filedata[filedata > 50])


# %%
# You can index with a list in NumPy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1, 2, 8]])


# %%
# Test whether any array element along a given    axis evaluates to True.
np.any(filedata > 50, axis= 0)


# %%
# Test whether all array elements along a given    axis evaluate to True.
np.all(filedata>50, axis= 0)


# %%
((filedata >50) & (filedata<100)) 


# %%
# Reverse of the above 
(~((filedata>50) & (filedata<100)))


# %%
# EXERCISE
array = np.arange(1,31)
final_array = array.reshape(6,5)
print(final_array)
print()
print(final_array[2:4 , 0:2])


# %%
# EXERCISE
print(final_array[[0,1,2,3], [1,2,3,4]])


# %%
# EXERCISE 
print(final_array[[0,4,5], 3:5])

# %%
r = np.random.randn(100, 3)

H, edges = np.histogramdd(r, bins=(5, 8, 4))

H.shape, edges[0].size, edges[1].size, edges[2].size
((5, 8, 4), 6, 9, 5)

# %%
np.disp(mesg='This is the best library !!!')
# %%
np.random.uniform(low=0, high=100, size=10)