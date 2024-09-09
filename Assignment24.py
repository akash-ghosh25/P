mat1 = []
mat2 = []
res = []

r1 = int(input("Enter number of rows for 1st matrix: "))
c1 = int(input("Enter number of columns for 1st matrix: "))
r2 = int(input("Enter number of rows for 2nd matrix: "))
c2 = int(input("Enter number of columns for 2nd matrix: "))

if c1 != r2:
    print("Matrix multiplication not possible.")
else:
    print("Enter 1st matrix: ")
    for i in range(r1):
        ele = []
        for j in range(c1):
            ele.append(int(input()))
        mat1.append(ele)

    print("Enter 2nd matrix: ")
    for i in range(r2):
        ele = []
        for j in range(c2):
            ele.append(int(input()))
        mat2.append(ele)

    for i in range(r1):
        res.append([0] * c2)

    for i in range(r1):
        for j in range(c2):
            sum = 0
            for k in range(c1):
                sum += mat1[i][k] * mat2[k][j]
            res[i][j] = sum

    print("Resultant matrix: ")
    for row in res:
        print(row)
