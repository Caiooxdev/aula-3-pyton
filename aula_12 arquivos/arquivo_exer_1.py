pares = open("pares.txt", "w")
impares = open("impares.txt", "w")


for i in range(1000):
    if i % 2 == 0:
        pares.write(str(i)+"\n")
    else:
        impares.write(str(i)+"\n")

pares.close()
impares.close()

print("pares escritos")
print("impares escritos")