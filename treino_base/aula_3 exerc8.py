#Escreva um programa que calcule a quantidade de latas de tinta
#necessárias e o custo para pintar tanques cilíndricos de
#combustível, em que são fornecidos a altura e o raio do
#cilindro. Sabendo que:
#▶ O preço da lata de tinta é de acordo com a quantidade:
#⋆ Na compra de 1 lata o valor unitário é de R$ 50,00
#⋆ Na compra de 2 latas o valor unitário é de R$ 48,00
#⋆ Na compra de 3 latas o valor unitário é de R$ 46,00
#⋆ Na compra de mais que 3 latas o valor unitário é de R$ 45,00
#▶ Uma lata de tinta tem 5 litros
#▶ Um litro cobre 3mš
#▶ A área do cilindro é a área da base somada com a área da lateral
#▶ A área da base é π × r
#2 (r = raio, π = 3.1415)
#▶ A área da lateral é altura multiplicada pelo perímetro
#▶ O perímetro é 2 × π × r

if latas == 1:
    preco_unitario = 50.00
elif latas == 2:
    preco_unitario = 48.00
elif latas == 3:
    preco_unitario = 46.00
else:
    preco_unitario = 45.00

custo_total = latas * preco_unitario

# Mostrando o resultado final formatado
print(f"Latas necessárias: {latas}")
print(f"Custo total: R$ {custo_total:.2f}")




















