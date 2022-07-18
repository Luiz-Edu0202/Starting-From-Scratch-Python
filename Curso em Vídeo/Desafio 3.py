print('Calculadora!')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('Digite 1 para somar')
print('Digite 2 para subtrair')
print('Digite 3 para multiplicar')
print('Digite 4 para dividir')
op = input('Qual a operação? ')
if op.isdigit() == True:
    if int(op) ==  1:
        s = n1 + n2
        print('A soma entre {} e {} vale {}!'.format(n1, n2, s))
    if int(op) ==  2:
        s = n1 - n2
        print('A subtrção entre {} e {} vale {}!'.format(n1, n2, s))
    if int(op) ==  3:
        s = n1 * n2
        print('A multiplicação entre {} e {} vale {}!'.format(n1, n2, s))
    if int(op) ==  4:
        s = n1 / n2
        print('A divisão entre {} e {} vale {}!'.format(n1, n2, s))

else:
    print('Por favor não tente quebrar a calculadora, Reinicie e digite corretamente por favor! ')
