def trasnpose(matrix):

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result



trasnpose([[1,2,3],[4,5,6],[7,8,9]])