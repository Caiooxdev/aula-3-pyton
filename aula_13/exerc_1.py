palavra = input("Digite uma palara: ")
nova_palavra = ""
for char in palavra:
    print(char, end=" ")
    if char == 'a' or char == 'e' or char == 'i' or char == 'O' or char == 'u':
        nova_palavra += (chr(ord(char)))
    else:
        nova_palavra += (char)

print(nova_palavra)

