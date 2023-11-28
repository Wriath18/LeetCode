def convert(s, numRows):
    l = len(s)
    matrix = [[None for _ in range(l)] for _ in range(numRows)]
    row = 0
    col = 0 
    movingdown = True
    newstr = ""

    for i in s:
        matrix[row][col] = i
        if movingdown:
            if row == numRows - 1:
                movingdown = False
                row -= 1
                col += 1
            else:
                row += 1

        else:
            if row == 0:
                movingdown =True
                row += 1
            else:
                row -= 1
                col += 1

    for i in matrix:
        for j in i:
            if j is not None:
                newstr += j

    print(newstr)


convert("PAYPALISHIRING",3)

