matriz  = [[0, 0, 0 , 0], [0, 0, 0 , 0], [0, 0, 0 , 0]]
a = int
b = int

for l in range(3):

    for c in range(4):

       if l == c:
           matriz[l][c] = ((l+1)+(c+1))
       else:
            matriz[l][c] = ((2*l)+1)-((2*c)+1)
a = matriz[1][1]
b = matriz[2][3]


print('=-'* 15)


for l in  range (3):
    for c in range(4):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print()
print('A soma dos valores na posição a22 e a34 é igual a:', a+b)
