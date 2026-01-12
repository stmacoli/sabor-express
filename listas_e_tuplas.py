# LISTAS
# As listas são mútaveis, ela podem ter alterações com os metodos de listas: append(), remove(), pop(), e insert().

# append() -> 👉 Adiciona um elemento no final da lista
# remove() -> 👉 Remove o primeiro elemento com o valor informado
# pop()    -> 👉 Remove e retorna um elemento da lista
# insert() -> 👉 Insere um elemento em uma posição específica
#             📌 Diferença importante:
#                - remove() → remove pelo valor 
#                - pop() → remove pelo índice e retorna o valor




# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

print('LISTA DE COMPRAS INCIAL: ')
print(lista_de_compras)
# Adicionando um item à lista
novo_iten = input('Digite o novo item: ')
iten_adicionado = lista_de_compras.append(novo_iten)


# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)

print(novo_iten)


#----------------------------------------------------------------------------------

# TUPLAS
# As Tuplas são imutáveis depois de sua criação. 

# Definindo uma tupla de coordenadas geográficas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])
