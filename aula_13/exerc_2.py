palavra = input("Digite a palavra: ")

i = 0 
j = len(palavra) - 1
palindromo = True
while i <= j:
    if palavra[i] != palavra[j]:
        palindromo = False
        break
    i += 1
    j -= 1
if palindromo:
    print("É palindromo!")

else:
    print("Não é palindromo")
