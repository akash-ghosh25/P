mat = []
t = []
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter 1st matrix: ")
for i in range(r):
    ele = []
    for j in range(c):
        ele.append(int(input()))
    mat.append(ele)

for i in range(r):
    ele = []
    for j in range(c):
        ele.append(mat[j][i])
    t.append(ele)

print("Matrix: ")
for val in mat:
    print(val)

print("Transpose matrix: ")
for val in t:
    print(val)
