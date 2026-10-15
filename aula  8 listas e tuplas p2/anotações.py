# ==========================================
# LISTA
# ==========================================
# Uma lista é um tipo de variável que permite o armazenamento de valores:
# - com tipos homogêneos (do mesmo tipo) ou heterogêneos (tipos diferentes).
# Os valores armazenados em uma lista são acessados por um índice.
# Para indicar que uma variável é uma lista, utilizamos o símbolo de colchetes.
# Sintaxe criando uma lista chamada L (lista vazia):
L = []

# Criando uma lista chamada z com 3 números inteiros
z = [5, 7, 1]
print(z)
# Dizemos que z tem tamanho 3.


# ==========================================
# ACESSO AOS ELEMENTOS
# ==========================================
# Para acessarmos o primeiro número da lista z, utilizamos a notação z[0].
# Ou seja, da lista z queremos pegar o valor armazenado no índice 0.
z = [5, 7, 1]
print(z[0])
print(z[1])
print(z[2])


# ==========================================
# MODIFICANDO ELEMENTOS
# ==========================================
# Podemos modificar o conteúdo armazenado utilizando o nome de
# uma lista com o índice desejado.
# Exemplo: Alterando o valor do primeiro elemento (índice 0) da lista z
z = [5, 7, 1]
z[0] = 32
print(z)


# ==========================================
# ADICIONANDO ELEMENTOS NO FIM DA LISTA
# ==========================================
# Podemos ainda adicionar novos elementos no fim da lista.
# Para isto, utilizamos o método append(item).
z = [32, 7, 1]
print(z)
z.append('oi')
print(z)


# ==========================================
# ADICIONANDO ELEMENTOS EM QUALQUER LUGAR
# ==========================================
# Podemos ainda adicionar elementos em qualquer lugar da lista.
# Para isto, utilizamos o método insert(índice, item).
z = [32, 7, 1]
print(z)
z.insert(1, 'oi')
print(z)


# ==========================================
# REMOVENDO DA LISTA PELO ÍNDICE
# ==========================================
# Podemos remover um elemento da lista.
# Para isto, utilizamos o método pop(índice).
z = ['a', 'b', 'd', 'e']
print(z)
z.pop(1)
print(z)


# ==========================================
# REMOVENDO DA LISTA PELO ELEMENTO
# ==========================================
# Podemos remover um elemento da lista.
# Para isto, utilizamos o método remove(item).
z = ['a', 'b', 'c', 'd', 'e']
print(z)
z.remove('d')
print(z)


# ==========================================
# TAMANHO DA LISTA (LEN)
# ==========================================
# Como temos os métodos para incluir e remover dados das listas,
# nem sempre sabemos qual é o tamanho exato que a lista tem.
# Para descobrirmos o tamanho da lista, utilizamos o método len(lista).
a = [3, 4, 5]
print(len(a))
a.append(9)
a.append(11)
print(len(a))


# ==========================================
# PESQUISANDO NA LISTA
# ==========================================
# Podemos pesquisar se um elemento está na lista.
# Para isso, verificamos do primeiro ao último comparando com o que queremos encontrar.
# Para percorrer listas, utilizamos uma estrutura de repetição: while ou for.
# A estrutura for é otimizada para trabalhar com listas.

# Procurar o elemento “c” na lista z mostrando mensagem se encontrou:
z = ['a', 'b', 'c', 'd', 'e']
for elemento in z:
  if elemento == 'c':
    print('Elemento encontrado!')
    break
else:
  print('Elemento não encontrado!')

# Porém, se a ideia é somente falar se o elemento está ou não na lista, podemos utilizar uma estrutura mais simples com 'in':
z = ['a', 'b', 'c', 'd', 'e']
if 'c' in z:
  print('Encontrado')
else:
  print('Não encontrado!')

# Contudo, nem sempre encontrar o elemento é suficiente.
# Muitas vezes, precisamos saber qual é a sua posição (índice) na lista:
z = ['a', 'b', 'c', 'd', 'e']
for indice in range(len(z)):
  if z[indice] == 'c':
    print('Elemento encontrado no indice %d' % indice)
    break
else:
  print('Elemento não encontrado!')


# ==========================================
# FATIAMENTO (SLICING)
# ==========================================
# No Python, podemos também fatiar as listas.
# Ou seja, pegar somente partes de uma lista.
p = [42, 13, 82, 63, 80, 90]
print(p[0:5])
print(p[:4])
print(p[1:3])
print(p[-1])


# ==========================================
# CÓPIA DE LISTAS
# ==========================================
# A cópia de uma lista para uma nova variável requer alguma atenção!
# Por exemplo, se quisermos copiar a lista z para uma nova variável chamada z1, o mais natural seria o seguinte:
# z1 = z
# Porém, quando fazemos isso no Python, criamos duas variáveis que referenciam a mesma lista!
# É como se déssemos dois nomes para a mesma lista.
# Quando alteramos o elemento da lista z, a alteração ocorre também na lista z1:
z = [4, 5, 3, 6]
z1 = z
print('antes da alteracao na lista z')
print(z)
print(z1)
z[1] = 98
print('depois da alteracao na lista z')
print(z)
print(z1)

# Para criarmos uma cópia independente, utilizamos a sintaxe com fatiamento completo z1 = z[:]:
z = [4, 5, 3, 6]
z1 = z[:]
z[1] = 98
print(z)
print(z1)


# ==========================================
# TUPLAS
# ==========================================
# Tuplas são similares às listas, porém são IMUTÁVEIS!
# Tuplas não permitem adicionar, apagar, inserir ou modificar elementos.
# Tuplas são definidas com parêntesis ( ).

# Exemplo de criação e leitura de uma tupla:
b = (2, 4, 5, 'tupla')
print(b)
print(b[1])

# Tuplas são imutáveis! Se tentar alterar (ex: b[1] = 8), gera um erro (TypeError).