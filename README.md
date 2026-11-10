# 🧮 Portfólio de Programação Matemática

Repositório destinado ao armazenamento e documentação das atividades desenvolvidas na disciplina de **Estruturas Matemáticas para Computação**.

---

## 👤 Identificação do Aluno

- **Nome:** Mariana Queiroz Lopes
- **Matrícula:** 2622130019
- **Disciplina:** Estruturas Matemáticas para Computação
- **Curso:** Ciência da Computação
- **Turno:** Matutino

---

## 🚀 Guia Rápido de Utilização

### 📂 Parte 1 (P1)

- **Atividade 1 – Teoria dos Conjuntos**
  - **Arquivo:** `P1/atividade_01_conjuntos/conjuntos.py`
  - **Como utilizar:** O programa solicita os elementos dos conjuntos A e B.
  - **Exemplo de entrada:**
    ```text
    A = 1 2 3 4
    B = 3 4 5 6
    ```
  - **O programa apresenta:** União, interseção, diferenças, cardinalidades, conjunto das partes, partição, produto cartesiano e inclusão.

- **Atividade 2 – Divisibilidade**
  - **Arquivo:** `P1/atividade_02_divisibilidade/divisibilidade.py`
  - **Como utilizar:** O programa solicita dois números inteiros (dividendo e divisor).
  - **Exemplo de entrada:**
    ```text
    A = 48
    B = 18
    ```
  - **O programa apresenta:** Divisão inteira (DIV), resto da divisão (MOD), passo a passo do Algoritmo de Euclides, Máximo Divisor Comum (MDC) e Mínimo Múltiplo Comum (MMC).

---

### 📂 Parte 2 (P2)

- **Atividade 1 – Congruência Modular e Teorema Chinês do Resto**
  - **Arquivo:** `P2/atividade_01_congruencia_tcr/atividade1.py`
  - **Como utilizar:** Executar o script para abrir o menu interativo e escolher entre testar a congruência simples ou resolver um sistema do TCR.
  - **Exemplo de entrada (Parte A - Congruência):**
    ```text
    a = 23, b = 8, n = 5
    ```
  - **Exemplo de entrada (Parte B - TCR):** Sistema de 3 congruências com restos $a = [2, 3, 2]$ e módulos $n = [3, 5, 7]$.
  - **O programa apresenta:** Verificação de divisibilidade e congruência modular, checagem de coprimalidade dos módulos, cálculo dos termos parciais $N_i$ e inversos modulares, somatória da solução $x_0$ e validação final do sistema.

- **Atividade 2 – Criptografia RSA**
  - **Arquivo:** `P2/atividade_02_rsa/atividade2.py`
  - **Como utilizar:** O programa guia o usuário em cada etapa da geração de parâmetros e cifragem de uma mensagem numérica.
  - **Exemplo de entrada:**
    ```text
    p = 61, q = 53
    e = 17
    M = 65
    ```
  - **O programa apresenta:** Teste autoral de primalidade para $p$ e $q$, cálculo de $n$ e da função Totiente de Euler $\phi(n)$, validação do expoente público $e$ via MDC, determinação da chave privada $d$ via Algoritmo de Euclides Estendido, cifragem/decifragem com exponenciação modular por reduções sucessivas e análise dos Teoremas de Euler e Fermat.

---

## 📁 Estrutura do Repositório

```text
portfolio-matematica-discreta-2026-2/
│
├── README.md
│
├── P1/
│   ├── atividade_01_conjuntos/
│   │   ├── conjuntos.py
│   │   └── documento_atividade_01.pdf
│   │
│   └── atividade_02_divisibilidade/
│       ├── divisibilidade.py
│       └── documento_atividade_02.pdf
│
└── P2/
    ├── atividade_01_congruencia_tcr/
    │   ├── atividade1.py
    │   └── documento_atividade_01P2.pdf
    │
    └── atividade_02_rsa/
        ├── atividade2.py
        └── documento_atividade_02P2.pdf
