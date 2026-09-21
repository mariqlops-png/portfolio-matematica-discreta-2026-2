# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 1 - Teoria dos Conjuntos
# ==================================================
# Cabeçalho
#------------------------------------------------------

print("--------------------------------------------------")
print("Nome: Mariana Queiroz Lopes")
print("Matrícula: 2622130019")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno: Matutino")
print("--------------------------------------------------")

#------------------------------------------------------
# Entrada dos elementos do conjunto
#------------------------------------------------------

A = set(input("\nDigite os números de A (separados por espaço): ").split())
B = set(input("Digite os números de B (separados por espaço): ").split())

print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")

#------------------------------------------------------
# União
#------------------------------------------------------

uniao = set()

for elemento in A:
    uniao.add(elemento)

for elemento in B:
    if elemento not in uniao:
        uniao.add(elemento)

print(f"\nUnião de A e B (A ∪ B): {uniao}")

#------------------------------------------------------
# Interseção
#------------------------------------------------------

intersecao = set()

for elemento in A:
    if elemento in B:
        intersecao.add(elemento)

if intersecao == set():
    print("\nInterseção de A e B (A ∩ B): ∅")
else:
    print(f"\nInterseção de A e B (A ∩ B): {intersecao}")

#------------------------------------------------------
# Diferença
#------------------------------------------------------

difeAB = set()

for elemento in A:
    if elemento not in B:
        difeAB.add(elemento)

difeBA = set()

for elemento in B:
    if elemento not in A:
        difeBA.add(elemento)

if difeAB == set():
    print("\nDiferença de A e B (A - B): ∅")
else:
    print(f"\nDiferença de A e B (A - B): {difeAB}")

if difeBA == set():
    print("\nDiferença de B e A (B - A): ∅")
else:
    print(f"\nDiferença de B e A (B - A): {difeBA}")

#------------------------------------------------------
# Cardinalidades
#------------------------------------------------------

cardA = len(A)
cardB = len(B)
carduniao = len(uniao)
cardintersecao = len(intersecao)

print(f"\nCardinalidade de A: {cardA}")
print(f"Cardinalidade de B: {cardB}")
print(f"Cardinalidade de A união B: {carduniao}")
print(f"Cardinalidade de A interseção B: {cardintersecao}")

#------------------------------------------------------
# Conjunto das partes de A
#------------------------------------------------------

partesA = [set()]

for elemento in A:
    novas_partes = []

    for parte in partesA:
        nova_parte = set(parte)
        nova_parte.add(elemento)
        novas_partes.append(nova_parte)

    partesA = partesA + novas_partes

print("\nConjunto das partes de A P(A):")

for parte in partesA:
    if parte == set():
        print("∅")
    else:
        print(parte)

cardPartesA = len(partesA)

print(f"Cardinalidade de P(A): {cardPartesA}")

#------------------------------------------------------
# Conjunto das partes de B
#------------------------------------------------------

partesB = [set()]

for elemento in B:
    novas_partes = []

    for parte in partesB:
        nova_parte = set(parte)
        nova_parte.add(elemento)
        novas_partes.append(nova_parte)

    partesB = partesB + novas_partes

print("\nConjunto das partes de B P(B):")

for parte in partesB:
    if parte == set():
        print("∅")
    else:
        print(parte)

cardPartesB = len(partesB)

print(f"Cardinalidade de P(B): {cardPartesB}")

#------------------------------------------------------
# Inclusão
#------------------------------------------------------

AemB = True

for elemento in A:
    if elemento not in B:
        AemB = False

BemA = True

for elemento in B:
    if elemento not in A:
        BemA = False

print(f"\nA está contido em B (A ⊆ B): {AemB}")
print(f"B está contido em A (B ⊆ A): {BemA}")

#------------------------------------------------------
# Produto cartesiano AxB
#------------------------------------------------------

produto = []

for elementoA in A:
    for elementoB in B:
        produto.append((elementoA, elementoB))

print(f"\nProduto cartesiano A x B: {produto}")

#------------------------------------------------------
# Partição exemplo
#------------------------------------------------------

listaA = list(A)
metade = len(listaA) // 2

parte1 = set(listaA[:metade])
parte2 = set(listaA[metade:])

print(f"\nExemplo de partição de A: {parte1} e {parte2}")

#------------------------------------------------------

print("\nFim")
