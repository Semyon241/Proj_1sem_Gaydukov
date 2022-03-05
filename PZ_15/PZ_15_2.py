matriza = [[-1, 2, 3], [4, -5, 6], [7, 8, 9]]
trigger = True
for i in range(len(matriza)):
    for j in range(3):
        if matriza[i][j] > 0:
            trigger = True
        else:
            pass
print(trigger)
