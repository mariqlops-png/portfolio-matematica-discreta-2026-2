#Atividade 01 Conjuntos.
#------------------------------------------------------
#Cabeçalho
#------------------------------------------------------
print("-" * 20)
print("Nome: Mariana Queiroz Lopes ")
print("Matrícula: 2622130019 ")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno: Matutino ")
print("-" * 20)
#-----------------------------------------------------
#Entradas dos elementos dos conjuntos
#-----------------------------------------------------

entrada_a = input("\n Digite os números do conjunto A separados por espaço: ")
entrada_b = input("Digite os números do conjunto B separados por espaço: ")

conjunto_a_texto = entrada_a.split()
conjunto_b_texto = entrada_b.split()

conjunto_a = []
for item in conjunto_a_texto:
    numero = int(item)
    conjunto_a.append(numero)

conjunto_b = []
for item in conjunto_b_texto:
    numero = int(item)
    conjunto_b.append(numero)

A = set(conjunto_a)
B = set(conjunto_b)

print(f"\nConjunto A = {A}")
print(f"Conjunto B = {B}")

#---------------------------------------------------
#União
#---------------------------------------------------

uniao = set()
for elemt in A:
    uniao.add(elemt)
for elemt in B:
    uniao.add(elemt)

print(f"\nA união B: {uniao}")

#---------------------------------------------------
#interseção
#---------------------------------------------------

intersecao = set()
for elemt in A:
    if elemt in B:
        intersecao.add(elemt)

print(f"A Interseção B = {intersecao}")

#----------------------------------------------------
#Diferença
#----------------------------------------------------

diferenca_ab = set()
for elemt in A:
    if elemt not in B:
        diferenca_ab.add(elemt)

diferenca_ba = set()
for elemt in B:
    if elemt not in A:
        diferenca_ba.add(elemt)
        
if diferenca_ab:
    print(f"A - B = {diferenca_ab}")
else:
    print("A - B = vazio")

if diferenca_ba:
    print(f"B - A = {diferenca_ba}")
else:
    print("B - A = vazio")

#----------------------------------------------------
#Cardinalidades
#----------------------------------------------------

print(f"\nCardinalidade de A: {len(A)}")
print(f"Cardinalidade de B: {len(B)}")
print(f"Cardinalidade da união de A e B: {len(uniao)}")
print(f"Cardinalidade da interseção de A e B: {len(intersecao)}")

#----------------------------------------------------
#conjunto das partes
#----------------------------------------------------

def conjunto_das_partes(conjunto):
    elementos = list(conjunto)
    partes = [[]]

    for elemento in elementos:
        novos_subconjuntos = []

        for subconjunto in partes:
            copia = subconjunto.copy()   
            copia.append(elemento)        
            novos_subconjuntos.append(copia)

        for novo in novos_subconjuntos:
            partes.append(novo)

    return partes

partes_a = conjunto_das_partes(A)
partes_b = conjunto_das_partes(B)

print("\nConjunto das partes de A:")
for subconjunto in partes_a:
    print(" ", subconjunto)

print("\nConjunto das partes de B:")
for subconjunto in partes_b:
    print(" ", subconjunto)

# --------------------------------------------------
# cardinalidades conjunto das partes
# --------------------------------------------------

print(f"\n Cardinalidade dos subconjuntos de A: {len(partes_a)}")
print(f"Cardinalidade dos subconjuntos de B: {len(partes_b)}")

#----------------------------------------------------
#Produto cartesiano AxB 
#---------------------------------------------------

produto_AXB = []

for a in A:
    for b in B:
        par = (a,b)
        produto_AXB.append(par)

print(f"\nProduto cartesiano AXB: {produto_AXB}")


#---------------------------------------------------
#Inclusão
#-------------------------------------------------

a_contido_b = True
for elemento in A:
    if elemento not in B:
        a_contido_b = False


b_contido_a = True
for elemento in B:
    if elemento not in A:
        b_contido_a = False

print(f"\nA está contido em B? {a_contido_b}")
print(f"B está contido em A? {b_contido_a}")


# --------------------------------------------------
# Partição
# --------------------------------------------------

lista_a_ordenada = sorted(A)
metade = len(lista_a_ordenada) // 2

parte1 = set(lista_a_ordenada[:metade])
parte2 = set(lista_a_ordenada[metade:])

print("\nExemplo de partição de A:")
print(f"Parte 1 = {parte1}")
print(f"Parte 2 = {parte2}")
#---------------------------------------------------

print("\nFim")




