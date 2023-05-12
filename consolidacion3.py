# declaracion
lista = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
magos = []
cientificos = []
otros = []
# transforma a grandioso
def grandioso(gran):
    for y in range(len(gran)):
        if gran[y] == 'Harry Houdini' or gran[y]  == 'David Blaine' or gran[y]  == 'Teller':
            gran[y] = ("El Gran "+ gran[y])
    return gran        
# imprime
def imprimir_nombres(y):
    for x in range(len(y)):
        #print(x,len(y))
        if x!=(len(y)-1):
            print(y[x], end=", ")
        else:
            print(y[x]+ ".\n")
# separa la lista en grupos
for x in range(len(lista)):
    if lista[x] == 'Harry Houdini' or lista[x] == 'David Blaine' or lista[x] == 'Teller':
        magos.append(lista[x])
    elif lista[x] == 'Newton' or lista[x] == 'Hawking' or lista[x] == 'Einstein':
        cientificos.append(lista[x])
    else:
        otros.append(lista[x])
# impresion de resultados
print ("\n")
print ("--- LISTA COMPLETA ORIGINAL ---")
print ("-------------------------------")
imprimir_nombres(lista)
print ("--- LISTA MAGOS ORIGINAL ---")
print ("--------------------------------")
imprimir_nombres(magos)
print ("--- LISTA MAGOS MODIFICADO ---")
print ("------------------------------")
magos = grandioso(magos)
imprimir_nombres(magos)
print ("--- LISTA CIENTIFICOS ---")
print ("-------------------------")
imprimir_nombres(cientificos)
print ("--- LISTA OTROS ---")
print ("-------------------")
imprimir_nombres(otros)
print ("--- LISTA COMPLETA MODIFICADA---")
print ("--------------------------------")
lista = grandioso(lista)
imprimir_nombres(lista)