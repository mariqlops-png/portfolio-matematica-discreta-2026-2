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
#Entrada dos elementos do conjunto
#-----------------------------------------------------

A = set(input("\nDigite os números de A (separados por espaço): ").split())
B = set(input("Digite os números de B (separados por espaço): ").split())

print(f"Conjunto A:{A}")
print(f"Conjunto B:{B}")

#---------------------------------------------------
#União
#---------------------------------------------------

uniao = A | B
print(f"\nUnião de A e B (A ∪ B): {uniao}")

#---------------------------------------------------
#interseção
#---------------------------------------------------

intersecao = A & B
print(f"Interseção de A e B (A ∩ B): {intersecao}")

#----------------------------------------------------
#Diferença
#----------------------------------------------------

difeAB = A - B
difeBA = B - A

print(f"\nDiferença entre A e B (A-B): {difeAB}")
print(f"Diferença entre B e A (B-A): {difeBA}")

#----------------------------------------------------
#Cardinalidades
#----------------------------------------------------
cardA = len(A)
cardB = len(B)
carduniao = len(uniao)
cardintersecao = len(intersecao)

print(f"\nCardinalidade de A: {cardA}")
print(f"Cardinalidade de B: {cardB}")
print(f"Cardinalidade de B: {carduniao}")
print(f"Cardinalidade de A interseção B: {cardintersecao}")

#----------------------------------------------------
#Conjunto das partes de A
#----------------------------------------------------

partesA = [set()]

for elemento in A:
    novas_partes = []

    for parte in partesA:
        nova_parte = parte | {elemento}
        novas_partes.append(nova_parte)

    partesA = partesA + novas_partes

print(f"\nConjunto das partes de A: {partesA}")

cardPartesA = len(partesA)

print(f"Cardinalidade do conjunto das partes de A: {cardPartesA}")

#----------------------------------------------------
#Conjunto das partes de B
#----------------------------------------------------

partesB = [set()]

for elemento in B:
    novas_partes = []

    for parte in partesB:
        nova_parte = parte | {elemento}
        novas_partes.append(nova_parte)

    partesB = partesB + novas_partes

print(f"\nConjunto das partes de B: {partesB}")

cardPartesB = len(partesB)

print(f"Cardinalidade do conjunto das partes de B: {cardPartesB}")

#----------------------------------------------------
#Produto cartesiano AxB 
#---------------------------------------------------

# --------------------------------------------------
# Partição
# --------------------------------------------------

#---------------------------------------------------

print("\nFim")
