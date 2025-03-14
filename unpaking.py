
lista = {1,2,3,4,5,6}
#Impresion de una lista normal
print(lista)

#Impresion de una lista mediante el uso desempaquetado
print(*lista)
print(*lista,sep="-")

#Juntar mas listas en una sola
lista2 = [6,7,8]
lista3 = [*lista , *lista2, 9,10]
print(lista3)

#Unir diccionarios 
diccionario1 = {"dato1": 10, "dato2": 20}
diccionario2 = {"dato3": 30, "dato4": 40}
diccionario3 = {**diccionario1, **diccionario2}
print(diccionario3)

#Duplica el mismo contenido
lista4 = [10,12,100,20]
lista5 = [*lista4]
lista5 = lista5
lista5.append(200)

#Distintos valores y espacios de memoria
print(f"Lista 5: {id(lista5)} contenido: {lista4}")
print(f"Lista 4: {id(lista4)} contenido: {lista5}")
string="texto"
print(string[2]*4)

def multiple(*datos):
    print(datos)
multiple(*lista5)