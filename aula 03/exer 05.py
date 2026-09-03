ano_atual = int(input("Digite o ano atual: "))
ano_nasc = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nasc

if idade >= 18:
    print("Você pode tirar CNH")