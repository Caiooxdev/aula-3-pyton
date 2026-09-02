from math import ceil

Altura = float(input("Digite a altura da parede: "))
raio = float(input("Digite a largura da parede: "))

raio_base = raio*raio*3.1415
perimetro = 2*raio*3.1415
area_lateral = altura * perimetro
area_cilindro = rea_base + area_lateral


litros = area_cilindro / 3
qtd_latas  = ceil(litros / 5)

if qtd_latas == 1:
    print(f"quantidade de latas:  {qtd_latas} | custo total: R$ {qtd_latas * 50:.2f}")