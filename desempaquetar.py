#Desempaqueta y combina las siguientes lista en una sola ordenada.
lista1 = [8, 3, 7]
lista2 = [2, 5, 9]
lista3 = [4, 6, 1]
lista_combinada = sorted([*lista1, *lista2, *lista3])
print(lista_combinada)
