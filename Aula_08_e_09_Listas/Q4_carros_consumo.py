# LABORATÓRIO 8 E 9 - LISTAS | QUESTÃO 4
# PERGUNTA ORIGINAL (texto enviado):
# Faça um programa que leia uma a um modelos de cinco carros (exemplos:
# FUSCA, GOL, VECTRA etc) e os guarde em uma mesma lista. Leia (um a um)
# uma outra lista com o consumo desses carros, isto é, quantos quilômetros
# cada um desses carros faz com um litro de combustível. Calcule e mostre:
# - O modelo do carro mais econômico;
# - Quantos litros de combustível cada um dos carros cadastrados consome
#   para percorrer uma distância de 1000 quilômetros.
# EXEMPLO: modelos FUSCA, GOL, VECTRA, ESCORT, PEUGEOT;
# consumos 5, 7, 6, 11, 2 km/l. Mais econômico: ESCORT.
# Litros para 1000 km, arredondados: 200, 143, 167, 91, 500.
# O QUE TREINA: duas listas relacionadas pelo índice, maior valor,
# divisão e repetição com for.

modelos = []
consumos = []

for i in range(5):
    modelo = input()
    modelos.append(modelo)

for i in range(5):
    consumo = float(input())
    consumos.append(consumo)

indice_melhor = consumos.index(max(consumos))
print(modelos[indice_melhor])

for consumo in consumos:
    litros = 1000 / consumo
    print(f"{litros:.0f}")

# EXPLICAÇÃO:
# append adiciona um item à lista.
# max(consumos) encontra o maior km/l (o mais econômico).
# index(...) encontra a posição desse carro, igual nas duas listas.
# 1000 / consumo calcula os litros necessários para percorrer 1000 km.
# :.0f exibe sem casas decimais, como no exemplo fornecido.
# ATENÇÃO: a tabela do Moodle mostra os valores digitados no resultado;
# este código exibe apenas os resultados calculados, sem repetir entradas.
