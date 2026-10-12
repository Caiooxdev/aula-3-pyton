#Faça um programa que solicita do usuário uma quantidade de
#dias, horas, minutos e segundos. Calcule e imprima o total
#convertido em somente segundos.
#Saída esperada:



dias = int(input("digite a quantidaded de dias: "))
horas = float(input("digite a quantidade de horas: "))
minutos = float(input("digite a quantidade de minutos: "))
segundos = float(input("digite a quantidade de segundos: "))
total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print("tempo total de segundos é:", total_segundos)



















