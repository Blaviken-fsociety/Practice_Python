m1 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

for i in range(len(m1)):
    if i != 0:
        for j in range(1, 10):
            x = m1[i][0] * j
            m1[i].append(x)

for i in range(len(m1)):
    for j in range(len(m1[0])):
        print(f"{m1[i][j]}", end=" ")
    print("")

print("\nBy Robisnel Paniza\n")