
# ---------------------------------------------------------
# ATIVIDADE 02 - CRIPTOGRAFIA RSA
# Disciplina: Estruturas Matemáticas para Computação
# ---------------------------------------------------------
print("\n" + "=" * 55)
print("PORTFOLIO DE PROGRAMACAO MATEMATICA")
print("=" * 55)

print("\nAluno:Mariana Queiroz Lopes")
print("Matricula: 2622130019")
print("Disciplina: Estruturas Matematicas para Computacao")
print("Turno: matutino")


# ---------------------------------------------------------
# FUNÇÃO 1 - VERIFICAR SE UM NÚMERO É PRIMO
# ---------------------------------------------------------

def verificar_primo(numero):

    if numero <= 1:
        return False

    divisor = 2

    while divisor < numero:

        if numero % divisor == 0:
            return False

        divisor += 1

    return True


# ---------------------------------------------------------
# FUNÇÃO 2 - CALCULAR O MDC PELO ALGORITMO DE EUCLIDES
# ---------------------------------------------------------

def calcular_mdc(a, b):

    print("\nCálculo do MDC:")

    while b != 0:

        resto = a % b

        print(f"{a} = {b} * {a // b} + {resto}")

        a = b
        b = resto

    print(f"MDC = {a}")

    return a


# ---------------------------------------------------------
# FUNÇÃO 3 - ENCONTRAR O INVERSO MULTIPLICATIVO
# ALGORITMO DE EUCLIDES ESTENDIDO
# ---------------------------------------------------------

def calcular_inverso(e, phi):

    print("\nCálculo do inverso multiplicativo:")

    a = phi
    b = e

    x_anterior = 1
    x_atual = 0

    y_anterior = 0
    y_atual = 1

    while b != 0:

        quociente = a // b
        resto = a % b

        print(f"{a} = {b} * {quociente} + {resto}")

        a, b = b, resto

        x_anterior, x_atual = (
            x_atual,
            x_anterior - quociente * x_atual
        )

        y_anterior, y_atual = (
            y_atual,
            y_anterior - quociente * y_atual
        )

    if a != 1:
        return None

    inverso = y_anterior % phi

    return inverso


# ---------------------------------------------------------
# FUNÇÃO 4 - EXPONENCIAÇÃO MODULAR
# CALCULA BASE^EXPOENTE MOD MODULO
# UTILIZANDO REDUÇÕES SUCESSIVAS
# ---------------------------------------------------------

def exponenciacao_modular(base, expoente, modulo):

    print(f"\nCalculando {base}^{expoente} mod {modulo}")

    resultado = 1
    base = base % modulo

    etapa = 1

    while expoente > 0:

        print(f"\nEtapa {etapa}:")
        print(f"Expoente atual: {expoente}")
        print(f"Base atual: {base}")
        print(f"Resultado atual: {resultado}")

        if expoente % 2 == 1:

            resultado = (resultado * base) % modulo

            print(
                f"Expoente ímpar: resultado = "
                f"({resultado}) mod {modulo}"
            )

        base = (base * base) % modulo
        expoente = expoente // 2

        print(f"Nova base: {base}")
        print(f"Novo expoente: {expoente}")

        etapa += 1

    print(f"\nResultado final: {resultado}")

    return resultado


# =========================================================
# PARTE A - PRIMALIDADE E PARÂMETROS RSA
# =========================================================

print("=" * 50)
print("ATIVIDADE 02 - CRIPTOGRAFIA RSA")
print("=" * 50)

print("\nPARTE A - PRIMALIDADE E PARÂMETROS RSA")

while True:

    p = int(input("\nDigite o primeiro número primo (p): "))
    q = int(input("Digite o segundo número primo (q): "))

    if p <= 1 or q <= 1:

        print("Os números devem ser maiores que 1.")

    elif p == q:

        print("Os números devem ser distintos.")

    elif not verificar_primo(p):

        print(f"{p} não é primo. Tente novamente.")

    elif not verificar_primo(q):

        print(f"{q} não é primo. Tente novamente.")

    else:

        print("\nOs dois números são primos e distintos!")
        break


# Cálculo do módulo RSA

n = p * q

print(f"\nn = p * q")
print(f"n = {p} * {q}")
print(f"n = {n}")


# Cálculo da função totiente de Euler

phi = (p - 1) * (q - 1)

print(f"\nphi(n) = (p - 1) * (q - 1)")
print(f"phi(n) = ({p} - 1) * ({q} - 1)")
print(f"phi(n) = {phi}")


# Escolha do expoente público

while True:

    e = int(input(f"\nDigite o expoente público (e), entre 1 e {phi}: "))

    if e <= 1 or e >= phi:

        print("O expoente deve ser maior que 1 e menor que phi(n).")

    else:

        mdc = calcular_mdc(e, phi)

        if mdc == 1:

            print("\nO expoente público é válido!")
            break

        else:

            print("O MDC deve ser igual a 1. Escolha outro expoente.")


print("\nPARÂMETROS RSA:")
print(f"p = {p}")
print(f"q = {q}")
print(f"n = {n}")
print(f"phi(n) = {phi}")
print(f"e = {e}")


# =========================================================
# PARTE B - CONSTRUÇÃO DAS CHAVES
# =========================================================

print("\n" + "=" * 50)
print("PARTE B - CONSTRUÇÃO DAS CHAVES")
print("=" * 50)

# Encontrando o expoente privado

d = calcular_inverso(e, phi)

print(f"\nExpoente privado d = {d}")


# Verificação do inverso multiplicativo

verificacao = (e * d) % phi

print(f"\nVerificação: e * d mod phi(n)")
print(f"{e} * {d} mod {phi} = {verificacao}")

if verificacao == 1:

    print("O inverso multiplicativo foi encontrado corretamente!")

else:

    print("Erro no cálculo do inverso multiplicativo.")


# Apresentação das chaves

print("\nCHAVES RSA:")

print(f"Chave pública: ({e}, {n})")
print(f"Chave privada: ({d}, {n})")


# =========================================================
# PARTE C - CIFRAGEM E DECIFRAGEM
# =========================================================

print("\n" + "=" * 50)
print("PARTE C - CIFRAGEM E DECIFRAGEM")
print("=" * 50)

while True:

    M = int(input(f"\nDigite um número inteiro M entre 0 e {n - 1}: "))

    if M < 0 or M >= n:

        print("Valor inválido! M deve satisfazer 0 <= M < n.")

    else:

        break


# Cifragem: C = M^e mod n

print("\n--- CIFRAGEM ---")

C = exponenciacao_modular(M, e, n)

print(f"\nNúmero original: {M}")
print(f"Número cifrado: {C}")


# Decifragem: M' = C^d mod n

print("\n--- DECIFRAGEM ---")

M_final = exponenciacao_modular(C, d, n)

print(f"\nNúmero cifrado: {C}")
print(f"Número decifrado: {M_final}")


# Verificação

print("\n--- VERIFICAÇÃO ---")

if M_final == M:

    print("O número decifrado é igual ao número original.")
    print("A criptografia RSA funcionou corretamente!")

else:

    print("O número decifrado é diferente do original.")
    print("Não foi possível confirmar a decifragem.")


# =========================================================
# PARTE D - TEOREMAS DE EULER E FERMAT
# =========================================================

print("\n" + "=" * 50)
print("PARTE D - TEOREMAS DE EULER E FERMAT")
print("=" * 50)


# ---------------------------------------------------------
# TEOREMA DE EULER
# ---------------------------------------------------------

print("\n--- TEOREMA DE EULER ---")

mdc_euler = calcular_mdc(M, n)

if mdc_euler == 1:

    print(f"\nM = {M}")
    print(f"n = {n}")
    print(f"phi(n) = {phi}")

    print("\nComo MDC(M, n) = 1, o Teorema de Euler pode ser aplicado.")

    print(f"Teorema: {M}^{phi} mod {n} = 1")

    resultado_euler = exponenciacao_modular(M, phi, n)

    if resultado_euler == 1:

        print("\nO Teorema de Euler foi verificado corretamente!")

    else:

        print("\nO resultado não foi igual a 1.")

else:

    print("\nO Teorema de Euler não pode ser aplicado diretamente.")
    print("A base M não é coprima com o módulo n.")
    print("Nesse caso, utiliza-se a exponenciação modular por reduções sucessivas.")


# ---------------------------------------------------------
# PEQUENO TEOREMA DE FERMAT
# ---------------------------------------------------------

print("\n--- PEQUENO TEOREMA DE FERMAT ---")

print(f"\nSerá utilizado o número primo p = {p}.")

while True:

    a = int(input(f"Digite uma base a que não seja divisível por {p}: "))

    if a % p == 0:

        print(f"A base não pode ser divisível por {p}.")

    else:

        break


print(f"\nBase escolhida: a = {a}")
print(f"Módulo primo: p = {p}")
print(f"Expoente: p - 1 = {p - 1}")

print("\nComo p é primo e a não é divisível por p,")
print("as condições do Pequeno Teorema de Fermat são atendidas.")

print(f"\nTeorema: {a}^{p - 1} mod {p} = 1")

resultado_fermat = exponenciacao_modular(a, p - 1, p)

if resultado_fermat == 1:

    print("\nO Pequeno Teorema de Fermat foi verificado corretamente!")

else:

    print("\nO resultado não foi igual a 1.")


# ---------------------------------------------------------
# CONCLUSÃO
# ---------------------------------------------------------

print("\n" + "=" * 50)
print("CONCLUSÃO DA ATIVIDADE")
print("=" * 50)

print("O programa realizou:")
print("1. Verificação de números primos.")
print("2. Cálculo dos parâmetros RSA.")
print("3. Cálculo do inverso multiplicativo.")
print("4. Construção das chaves pública e privada.")
print("5. Cifragem e decifragem de um número.")
print("6. Demonstração do Teorema de Euler.")
print("7. Demonstração do Pequeno Teorema de Fermat.")

print("\nFim do programa!")
