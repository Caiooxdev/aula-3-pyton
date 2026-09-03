dias = int(input("digite a quantidade de dias: "))
horas = int(input("digite a quantidade de horas: "))
minutos = int(input("digite a quantidade de minutos: "))
segundos = int(input("digite a quantidade de segundos: "))

total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print("tempo total foi de", total, "segundos")