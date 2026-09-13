#Atividade 01 Conjuntos.
#------------------------------------------------------
print("-" * 30)
print("Nome: Mariana Queiroz Lopes ")
print("Matrícula: 2622130019 ")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno: Matutino ")
print("-" * 30)
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
interseção = set()
for elemt in A:
    if elemt in B:
        interseção.add(elemt)

print(f"A Interseção B = {intersecao}")
#----------------------------------------------------

