soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos valores pares: {}'.format(soma))
print('A quantidade de valores pares: {}'.format(cont))
