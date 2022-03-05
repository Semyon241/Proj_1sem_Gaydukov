matriza = [[2, 5, 6], [1, 7, 3], [4, 8, 9]]
for i in range(len(matriza)):
    for j in range(3):
        if i == 0 and j == 0:
            pass
        elif i == 1 and j == 1:
            pass
        elif i == 2 and j == 2:
            pass
        else:
            matriza[i][j] = matriza[i][j] * 2
print(matriza)
