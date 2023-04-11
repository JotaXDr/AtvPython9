palavra = input("Informe uma palavra: ")
new_palavra = ""
for letra in palavra:
    new_codigo_ascii = ord(letra) + 1
    new_letra = chr(novo_codigo_ascii)
    new_palavra += nova_letra
print(nova_palavra)