from math import ceil

altura = float(input("Altura: "))
raio = float(input("Raio: "))

area_base = 3.1415 * (raio ** 2)
perimetro = 2 * 3.1415 * raio
area_lateral = altura * perimetro
area_total = area_base + area_lateral

litros = area_total / 3
latas = ceil(litros / 5)

if latas == 1:
    preco_unit = 50.00
elif latas == 2:
    preco_unit = 48.00
elif latas == 3:
    preco_unit = 46.00
else:
    preco_unit = 45.00

custo_total = latas * preco_unit

print("Área a ser pintada:", round(area_total, 2))
print("Qtde de litros necessários:", round(litros, 2))
print("Qtde de latas de tinta:", latas)
print("Preço unitário da lata: R$ %.2f" % preco_unit)
print("Custo total: R$ %.2f" % custo_total)