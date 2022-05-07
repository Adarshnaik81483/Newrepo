#transpose the matrix
list_of_lists = [
    [201,202,203],
    [204,205,206],
    [207,208,209]
]
transposed = [[row[i] for row in list_of_lists] for i in range(len(list_of_lists[0]))]
print(transposed)