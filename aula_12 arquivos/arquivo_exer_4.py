
contatos = []


def carregarcontatos():
    return
def salvarcontatos():
     return



def novo_contato():
    nome = input("digite o nome: ")
    sobrenome = input("digite o sobrenome: ")
    telefone = input("digite o telefone: ")
    email = input("digite o email: ")

    novo = {'nome': nome, 'sobrenome': sobrenome, 'telefone': telefone, 'email': email}

    
    contatos.append(novo)1

def exibecontatos(contato):
    print(f"nome: {contato['nome']}, sobrenome: {contato['sobrenome']}, telefone: {contato['telefone']}, email: {contato['email']}")
    print()

def buscar_contato():
    nome = input("digite o nome a ser buscado: ")
    for i in range(len(contatos)):
        if contatos[i]['nome'] == nome:
            print("contato encontrado: ", contatos[i])
            exibecontatos(contatos[i])


def exibemenu():
    print("1 - novo contato")
    print("2 - buscar contato")
    print("3 - atualizar contato")
    print("4 - apagar contato")
    print("0 - sair")


def processamenu(menu):
    if menu == 1:
        print("novo contato")
        return True
    elif menu == 2:
        print("buscar contato")
        return True
    elif menu == 3:
        print("atualizar contato")
        return True
    elif menu == 4:
        print("apagar contato")
        return True
    elif menu == 0:
        print("saindo...")
        return False
    return False
    
       

while True:
    exibemenu()
    menu = int(input("digite a opção desejada: "))
    if (not processamenu(menu)):
        break
    salvarcontatos()