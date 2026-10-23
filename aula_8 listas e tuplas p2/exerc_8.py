l = []

while True:
    palavra = input("digite uma palavra: ")
    if palavra == "":
        break
    if not palavra in l:
        l.append(palavra)

print("palavra digitadas: ")
for palavra in l:
    print(palavra)

    
