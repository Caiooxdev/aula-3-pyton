#Escreva um programa que pergunte o ano atual e o ano de
#nascimento do usuário.
#Calcule a idade dele.
#Se a idade for maior ou igual a 18 anos, mostre uma mensagem
#izendo que ele pode tirar CNH.
#Observação: Resolva usando apenas Estruturas de Decisão
#Simples.

ano_atual = int(input("digite o ano atual: "))
ano_nasc = int(input("digite seu ano de nascimento: "))

idade = ano_atual - ano_nasc

if idade >= 18:
   print(f"sua iadde é: {idade} anos, pode tirar a CNH")


