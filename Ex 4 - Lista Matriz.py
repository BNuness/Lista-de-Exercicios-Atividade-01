matriz = [[1, -1, 0 ], [2, 3, 4 ], [0, 1, -2 ]]
matrizresult  = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matrizt= list(map(list, zip(*matriz)))
print('Matriz A')
print('=-'* 8)
for j in matriz:
    print(j)
print()
print('Matriz A Transposta')
print('=-'* 8)
for j in matrizt:
    print(j)

for l in range(3):

    for c in range(3):
        matrizresult[l][c] = matriz[l][c] + matrizt[l][c]

print()
print('Matriz B = A + A Transposta')
print('=-'* 8)
for l in  range (3):
    for c in range(3):
        print(f'[{matrizresult[l][c]:^5}]', end='')

    print()
print('=-'* 8)