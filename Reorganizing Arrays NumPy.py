# Reorganizing Arrays NumPy
# %%
import numpy as np
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)


# %%
# Changing the shape of an array
before.shape = (8,1)
print(before)
# OR
after = before.reshape((2,2,2))
print(after)


# %%
# Vertical stacking vectors/ matrix
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack(tup= [v1,v2,v2,v1]))


# %%
# Horizontal Stacking vectors/matrixes
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack([h2, h1]))
 


