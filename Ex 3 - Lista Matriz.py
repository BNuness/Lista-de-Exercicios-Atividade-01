matriza  = [[0, 3], [2, -5]]
matrizb  = [[-2, 4], [0, -1]]
matrizc  = [[4, 2], [-6, 0]]
matrizresult  = [[0, 0], [0, 0]]


for l in range(2):

    for c in range(2):

        matrizresult[l][c] = matriza[l][c] + matrizb[l][c] - (matrizc[l][c] *4)


print('=-'* 8)
for l in  range (2):
    for c in range(2):
        print(f'[{matrizresult[l][c]:^5}]', end='')

    print()
print('=-'* 8)