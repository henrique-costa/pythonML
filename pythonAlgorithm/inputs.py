caractere = input("Digite uma letra: ")
print(f"Letra digitada foi: {caractere}")
valor_decimal = ord(caractere)
print(f"Seu valor em decimal é: {valor_decimal}")
print(f"Seu valor em hexadecimal é: {hex(valor_decimal)}")
print(f"Seu valor em binário é: {bin(valor_decimal)}")

# Figura 2 (a): Código com parâmetros sep e end
texto = "Alterando o valor de sep"
print(texto)
print('Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', sep=' --- ')

# Pula uma linha
print()

texto = "Alterando o valor de sep e end"
print(texto)
print('Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', sep=' --- ', end='...\n')