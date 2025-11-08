import numpy as np

array = np.array(
    [
        [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
        [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
        [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]],
    ]
)
print(array.ndim)  # Number of dimension
print(array.shape)  # Dimension, Rows, Columns
print(array[0][0][0])  # Chain indexing
print(array[0, 1, 2])  # Multidimension indexing


first_name = (
    array[1, 2, 2]
    + array[0, 2, 2]
    + array[2, 0, 1]
    + array[0, 2, 2]
    + array[1, 0, 1]
    + array[2, 2, 2]
)

last_name = (
    array[2, 0, 0]
    + array[0, 2, 1]
    + array[0, 0, 0]
    + array[1, 2, 2]
    + array[1, 1, 0]
    + array[0, 0, 0]
)

word = first_name + last_name
print(word)
