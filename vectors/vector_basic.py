import numpy as np

asList = [1, 2, 3]
asArray = np.array([1, 2, 3])  # 1D array
rowVec = np.array([[1, 2, 3]])  # row
colVec = np.array([[1], [2], [3]])  # column

print(f"asList: {type(asList)}")
print(f"asArray: {type(asArray)}")
print(f"rowVec: {type(rowVec)}")
print(f"colVec: {type(colVec)}")

print(f"asList: {np.shape(asList)}")
print(f"asArray: {asArray.shape}")
print(f"rowVec: {rowVec.shape}")
print(f"colVec: {colVec.shape}")
