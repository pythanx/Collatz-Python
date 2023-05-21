# hipotese de Collatz

# o usuario digita o numero
c0 = int(input("Digite um numero: "))

# contador que verifica quantas etapas foram necessarias ate que c0 se tornasse igual a 1
count = 0
while c0 != 1:
    # verifica se c0 é par
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        # se for impar
        c0 = 3 * c0 + 1
    # imprime os num intermediarios
    print(int(c0))
    count += 1

# imprime as etapas
print("etapas = ", count)
