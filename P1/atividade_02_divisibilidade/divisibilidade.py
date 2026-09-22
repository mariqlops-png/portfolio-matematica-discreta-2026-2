# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 2 - Divisibilidade, MDC e MMC
# ==================================================

# ------------------------------------------------------
# Cabeçalho
# ------------------------------------------------------
print("\nCABEÇALHO")
print("--------------------------------------------------")
print("Nome: Mariana Queiroz Lopes")
print("Matrícula: 2622130019")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno: Matutino")
print("--------------------------------------------------")

# ------------------------------------------------------
# Entrada dos números
# ------------------------------------------------------
print("\nENTRADA DOS NÚMEROS")

num_a = int(input("\nDigite um número inteiro e positivo (dividendo): "))
num_b = int(input("Digite mais um número inteiro e positivo (divisor): "))

print(f"\nDividendo: {num_a}")
print(f"Divisor: {num_b}")

# Guarda os valores originais para o cálculo posterior do MMC
numero_a_original = num_a
numero_b_original = num_b

print("\n--------------------------------------------------")

# ------------------------------------------------------
# DIV e MOD
# ------------------------------------------------------
print("\nDIV E MOD")

div = num_a // num_b
mod = num_a % num_b

print(f"\nDIV (quociente da divisão) = {div}")
print(f"MOD (resto da divisão) = {mod}")

print("\n--------------------------------------------------")

# ------------------------------------------------------
# Algoritmo de Euclides e MDC
# ------------------------------------------------------
print("\nPASSO A PASSO - ALGORITMO DE EUCLIDES E MDC (máximo divisor comum)")

while num_b != 0:
    resto = num_a % num_b
    quociente = num_a // num_b

    print(f"\n{num_a} = {num_b} × {quociente} + {resto}")

    num_a = num_b
    num_b = resto

mdc = num_a
print(f"\nMDC (máximo divisor comum) = {mdc}")

print(f"\nMDC É definido pelo ultímo resto não nulo do algoritimo de euclides.")

print("\n--------------------------------------------------")

# ------------------------------------------------------
# MMC (mínimo múltiplo comum)
# ------------------------------------------------------
print("\nMMC (mínimo múltiplo comum)")

mmc = (numero_a_original * numero_b_original) // mdc

print("\nO MMC é definido pelo produto de a e b divídido pelo MDC(a,b)")

print(f"\nMMC (mínimo múltiplo comum) = {mmc}")

print("\n--------------------------------------------------")

# ------------------------------------------------------

print("\nFim")
