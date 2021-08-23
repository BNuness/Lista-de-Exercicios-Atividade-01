matriz  = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for l in range(0, 3):

    for c in range(0, 2):

       if l == c:
           matriz[l][c] = 1
       else:
            matriz[l][c] = (l+1) ** 2

print('=-'* 15)
for l in  range (0, 3):
    for c in range(0, 2):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
