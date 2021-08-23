def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo
t = float(input('Entre com a taxa de imposto: '))
c = float(input('Entre com o custo: '))
somaImposto = round(somaImposto(t,c),2)
print('Valor com imposto: ', somaImposto)