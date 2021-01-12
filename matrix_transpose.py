matrix = [[1,2,3],[4,5,6],[7,8,9]]
tran_matrix =[]
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(matrix[j][i])
    tran_matrix.append(temp)
print(tran_matrix)


