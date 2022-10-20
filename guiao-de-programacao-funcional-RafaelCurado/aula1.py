#Exercicio 1.1
def comprimento(lista):
	if lista==[]:
		return 0
	return 1+comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
	if lista==[]:
		return 0
	return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
	if lista==[]:
		return 0
	return (lista[0]==elem) or existe(lista[1:],elem)

#Exercicio 1.4
def concat(l1, l2):
	if l2==[]:
		return l1
	return concat(l1+l2[:1], l2[1:])
	
#Exercicio 1.5
def inverte(lista):
	if lista==[]:
		return []
	inv = inverte(lista[1:])
	inv[len(inv):] = [lista[0]]
	return inv

#Exercicio 1.6
def capicua(lista):
	if lista == []:
		return True
	if lista[0] != lista[-1]: return False
	return capicua(lista[1:-1])
	

#Exercicio 1.7
def concat_listas(lista):
	if lista == []:
		return []
	return lista[0] + concat_listas(lista[1:])

#Exercicio 1.8
def substitui(lista, original, novo):
	if lista == []:
		return []
	if lista[0] == original:
		return [novo] + substitui(lista[1:], original, novo)
	else:
		return lista[:1] + substitui(lista[1:], original, novo)

#Exercicio 1.9
def fusao_ordenada(lista1, lista2):
	if lista1 == []:
		return lista2
	if lista2 == []:
		return lista1

	if lista1[0] < lista2[0]:
		return lista1[:1] + fusao_ordenada(lista1[1:], lista2)
	else:
		return lista2[:1] + fusao_ordenada(lista1, lista2[1:]) 

#Exercicio 1.10
def lista_subconjuntos(lista):
	if lista == []:
		return [[]]

	a = lista_subconjuntos(lista[1:])	
	return a + [[lista[0]] + b for b in a]

#Exercicio 2.1
def separar(lista):
	if lista == []:
		return [],[]
	a, b = lista[0]
	c, d = separar(lista[1:])
	return [a] + c, [b] + d

#Exercicio 2.2
def remove_e_conta(lista, elem):
	if lista == []:
		return [], 0

	a, b = remove_e_conta(lista[1:], elem)
	
	if lista[0] == elem:
		return a, b+1
	else:
		return [lista[0]]+a, b
	

#Exercicio 3.1
def cabeca(lista):
	if lista == []:
		return None
	return lista[0]

#Exercicio 3.2
def cauda(lista):
	if lista == []:
		return None
	return lista[-1]

#Exercicio 3.3
def juntar(l1, l2):
	if len(l1) != len(l2):
		return None
	if l2 == []:
		return l2

	a, b = l1[0], l2[0]

	return [(a,b)] + juntar(l1[1:], l2[1:])

	
#Exercicio 3.4
def menor(lista):
	if lista == []:
		return None
	
	men = lista[0]

	if lista[1] < men:
		return lista[1] + menor(lista[1:])
	else:
		return men + menor(lista)

#Exercicio 3.6
def max_min(lista):
	pass
