
# ==========================================================
# PORTFOLIO DE PROGRAMACAO MATEMATICA - PARTE 2
# Atividade 1 - Congruencia Modular e Teorema Chines do Resto
# Disciplina: Estruturas Matematicas para Computacao
# Linguagem: Python
# ==========================================================

print("\n" + "=" * 55)
print("PORTFOLIO DE PROGRAMACAO MATEMATICA")
print("=" * 55)

print("\nAluno:Mariana Queiroz Lopes")
print("Matricula: 2622130019")
print("Disciplina: Estruturas Matematicas para Computacao")
print("Turno: matutino")


# ----------------------------------------------------------
# FUNCAO 1 - CALCULO DO MDC PELO ALGORITMO DE EUCLIDES
# ----------------------------------------------------------

def calcular_mdc(a, b):

    a = abs(a)
    b = abs(b)

    print("\nPassos do Algoritmo de Euclides:")

    while b != 0:

        quociente = a // b
        resto = a % b

        print(a, "=", b, "x", quociente, "+", resto)

        a = b
        b = resto

    print("MDC =", a)

    return a


# ----------------------------------------------------------
# FUNCAO 2 - CALCULO DO INVERSO MULTIPLICATIVO
# PELO ALGORITMO DE EUCLIDES ESTENDIDO
# ----------------------------------------------------------

def calcular_inverso(numero, modulo):

    # Variaveis utilizadas pelo algoritmo
    resto_anterior = numero
    resto_atual = modulo

    coef_numero_anterior = 1
    coef_numero_atual = 0

    coef_modulo_anterior = 0
    coef_modulo_atual = 1

    print("\nAplicando o Algoritmo de Euclides Estendido:")

    while resto_atual != 0:

        quociente = resto_anterior // resto_atual
        novo_resto = resto_anterior % resto_atual

        print(
            resto_anterior, "=",
            resto_atual, "x", quociente, "+", novo_resto
        )

        # Atualizacao dos restos
        resto_anterior, resto_atual = (
            resto_atual,
            novo_resto
        )

        # Atualizacao dos coeficientes
        coef_numero_anterior, coef_numero_atual = (
            coef_numero_atual,
            coef_numero_anterior - quociente * coef_numero_atual
        )

        coef_modulo_anterior, coef_modulo_atual = (
            coef_modulo_atual,
            coef_modulo_anterior - quociente * coef_modulo_atual
        )

    # O ultimo resto nao nulo e o MDC
    mdc = resto_anterior

    print("MDC =", mdc)

    if mdc != 1:

        print("O inverso multiplicativo nao existe.")
        return None

    # O coeficiente de numero e o inverso antes da reducao
    inverso_original = coef_numero_anterior

    # Reduz o inverso ao intervalo de 0 ate modulo - 1
    inverso = inverso_original % modulo

    print(
        "Identidade de Bezout:",
        mdc, "=",
        coef_numero_anterior, "x", numero, "+",
        coef_modulo_anterior, "x", modulo
    )

    print(
        "Inverso encontrado:",
        inverso_original, "mod", modulo, "=", inverso
    )

    print(
        "Verificacao:",
        numero, "x", inverso, "mod", modulo, "=",
        (numero * inverso) % modulo
    )

    return inverso


# ----------------------------------------------------------
# PARTE A - VERIFICACAO DE CONGRUENCIA MODULAR
# ----------------------------------------------------------
print("\n" + "=" * 55)
print("PARTE A - VERIFICACAO DE CONGRUENCIA MODULAR")
print("=" * 55)

a = int(input("\nDigite o valor de a: "))
b = int(input("Digite o valor de b: "))
n = int(input("Digite o modulo n: "))

# Verifica se o modulo e positivo
while n <= 0:

    print("Erro: o modulo precisa ser positivo.")
    n = int(input("Digite novamente o modulo n: "))

# Calcula a diferenca
diferenca = a - b

# Calcula o quociente e o resto
quociente = diferenca // n
resto = diferenca % n

print("\n--- CALCULOS ---")

print("a =", a)
print("b =", b)
print("n =", n)

print("\nDiferenca:")
print("a - b =", a, "-", b, "=", diferenca)

print("\nDivisao pelo modulo:")
print(
    diferenca, "=", n, "x", quociente, "+", resto
)

print("Resto da divisao =", resto)

# Verifica a congruencia
if resto == 0:

    print("\nCONCLUSAO:")
    print(
        a, "e", b,
        "sao congruentes modulo", n
    )

    print(a, "equivale a", b, "(mod", n, ")")

else:

    print("\nCONCLUSAO:")
    print(
        a, "e", b,
        "NAO sao congruentes modulo", n
    )

    print("O resto encontrado e diferente de zero.")


# ----------------------------------------------------------
# PARTE B - TEOREMA CHINES DO RESTO
# ----------------------------------------------------------

print("\n" + "=" * 55)
print("PARTE B - TEOREMA CHINES DO RESTO")
print("=" * 55)

# Solicita a quantidade de congruencias
quantidade = int(
    input("\nDigite a quantidade de congruencias (3 ou 4): ")
)

while quantidade != 3 and quantidade != 4:

    print("Quantidade invalida. Escolha 3 ou 4.")
    quantidade = int(
        input("Digite novamente a quantidade: ")
    )

# Listas para armazenar os restos e os modulos
restos = []
modulos = []

# Solicita os valores de cada congruencia
print("\nDigite os valores de cada congruencia:")

for i in range(quantidade):

    print("\nCongruencia", i + 1)

    ai = int(input("Digite o resto: "))
    ni = int(input("Digite o modulo: "))

    restos.append(ai)
    modulos.append(ni)


# ----------------------------------------------------------
# VERIFICACAO DOS MODULOS
# ----------------------------------------------------------

print("\n--- VERIFICACAO DAS CONDICOES ---")

modulos_positivos = True

for i in range(quantidade):

    print(
        "Modulo n", i + 1, "=", modulos[i]
    )

    if modulos[i] <= 0:

        print("Erro: todos os modulos precisam ser positivos.")
        modulos_positivos = False


# Verifica se os modulos sao dois a dois coprimos
modulos_coprimos = True

if modulos_positivos:

    print("\nVerificando se os modulos sao dois a dois coprimos:")

    for i in range(quantidade):

        for j in range(i + 1, quantidade):

            print(
                "\nVerificando MDC(",
                modulos[i], ",", modulos[j], ")"
            )

            mdc = calcular_mdc(modulos[i], modulos[j])

            if mdc == 1:

                print("Os modulos sao coprimos.")

            else:

                print("Os modulos NAO sao coprimos.")
                modulos_coprimos = False


# ----------------------------------------------------------
# APLICACAO DO TEOREMA CHINES DO RESTO
# ----------------------------------------------------------

if modulos_positivos and modulos_coprimos:

    print("\n" + "=" * 55)
    print("APLICANDO O TEOREMA CHINES DO RESTO")
    print("=" * 55)

    # Passo 1 - Calcula o produto de todos os modulos
    N = 1

    for i in range(quantidade):

        N = N * modulos[i]

    print("\nProduto dos modulos:")

    print("N =", end=" ")

    for i in range(quantidade):

        print(modulos[i], end="")

        if i < quantidade - 1:
            print(" x ", end="")

    print(" =", N)

    # Listas para armazenar os resultados
    valores_Ni = []
    inversos = []

    # Passo 2 - Calcula cada Ni e seu inverso
    for i in range(quantidade):

        print("\n" + "-" * 45)

        print("Congruencia", i + 1)

        # Calcula Ni
        Ni = N // modulos[i]

        valores_Ni.append(Ni)

        print("\nCalculo de N", i + 1)
        print("N", i + 1, "=", N, "/", modulos[i])
        print("N", i + 1, "=", Ni)

        # Calcula o inverso de Ni modulo ni
        print(
            "\nCalculando o inverso de",
            Ni, "modulo", modulos[i]
        )

        inverso = calcular_inverso(Ni, modulos[i])

        inversos.append(inverso)

    # Passo 3 - Calcula a soma utilizada no TCR
    print("\n" + "=" * 55)
    print("CALCULO DA SOLUCAO")
    print("=" * 55)

    soma = 0

    for i in range(quantidade):

        parcela = (
            restos[i] * valores_Ni[i] * inversos[i]
        )

        print("\nParcela", i + 1, ":")

        print(
            restos[i], "x",
            valores_Ni[i], "x",
            inversos[i], "=",
            parcela
        )

        soma = soma + parcela

    print("\nSoma das parcelas =", soma)

    # Passo 4 - Reduz o resultado modulo N
    x0 = soma % N

    print("\nReducao modulo N:")
    print(x0, "=", soma, "mod", N)

    print("\nSOLUCAO PARTICULAR:")
    print("x0 =", x0)

    # Passo 5 - Apresenta a solucao geral
    print("\nSOLUCAO GERAL:")
    print("x =", x0, "+ t x", N)
    print("Onde t pertence aos numeros inteiros (Z).")

    # Passo 6 - Verifica se x0 satisfaz todas as congruencias
    print("\n" + "=" * 55)
    print("VERIFICACAO DA SOLUCAO")
    print("=" * 55)

    solucao_valida = True

    for i in range(quantidade):

        resto_verificacao = x0 % modulos[i]

        print("\nCongruencia", i + 1)

        print(
            x0, "mod", modulos[i],
            "=", resto_verificacao
        )

        print("Resto esperado =", restos[i] % modulos[i])

        if resto_verificacao == restos[i] % modulos[i]:

            print("Congruencia satisfeita.")

        else:

            print("Congruencia NAO satisfeita.")
            solucao_valida = False

    if solucao_valida:

        print("\nRESULTADO FINAL:")
        print("A solucao encontrada satisfaz todas as congruencias.")

        print("Solucao particular: x =", x0)
        print("Solucao geral: x =", x0, "+", N, "t")

    else:

        print("\nERRO: a solucao nao satisfez todas as congruencias.")

else:

    print("\n" + "=" * 55)
    print("SISTEMA FORA DAS CONDICOES DA ATIVIDADE")
    print("=" * 55)

    print(
        "Nao foi possivel aplicar o Teorema Chines do Resto."
    )

    print(
        "Os modulos precisam ser positivos e dois a dois coprimos."
    )

print("\n" + "=" * 55)
print("FIM DA ATIVIDADE 1")
print("=" * 55)
