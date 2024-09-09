mat1 = []
mat2 = []
res = []

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
print("Enter 1st matrix: ")
for i in range(r):
    ele = []
    for j in range(c):
        ele.append(int(input()))
    mat1.append(ele)

print("Enter 2nd matrix: ")
for i in range(r):
    ele = []
    for j in range(c):
        ele.append(int(input()))
    mat2.append(ele)

for i in range(r):
    ele = []
    for j in range(c):
        ele.append(mat1[i][j] + mat2[i][j])
    res.append(ele)

print("Resultant matrix: ")
for val in res:
    print(val)