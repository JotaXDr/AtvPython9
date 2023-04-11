frase = input("Insira uma frase: ")
caractere_brancos = 0
for letra in frase:
    if letra == " ":
        caractere_brancos += 1
print(f"A frase digitada possui {caractere_brancos} caracteres em branco.")