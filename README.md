# Portfólio de Programação Matemática

Repositório destinado ao armazenamento das atividades desenvolvidas na disciplina de **Estruturas Matemáticas para Computação** (2026/2).

---

## 👤 Identificação do Aluno

* **Nome:** Mariana Queiroz Lopes
* **Matrícula:** 2622130019
* **Disciplina:** Estruturas Matemáticas para Computação
* **Curso:** Ciência da Computação
* **Turno:** Matutino

---

## 📁 Estrutura do Repositório

```text
portfolio-matematica-discreta-2026-2/
│
├── README.md
│
└── P1/
    ├── atividade_01_conjuntos/
    │   ├── conjuntos.py
    │   └── documento_atividade_01.pdf
    │
    └── atividade_02_divisibilidade/
        ├── divisibilidade.py
        └── documento_atividade_02.pdf


🚀 Atividades Desenvolvidas📌 Atividade 1 – Teoria dos ConjuntosDiretório: P1/atividade_01_conjuntos/Código-fonte: conjuntos.pyRelatório em PDF: documento_atividade_01.pdf🔹 DescriçãoAplicação interativa em Python para realização de operações fundamentais sobre Teoria dos Conjuntos a partir de elementos numéricos inseridos pelo usuário no terminal.🔹 Operações Implementadas (Manualmente)União ($A \cup B$) e Interseção ($A \cap B$)Diferença ($A - B$ e $B - A$)Cardinalidade dos conjuntos e de seus conjuntos das partes ($\vert{}A\vert{}$, $\vert{}B\vert{}$, $\vert{}\mathcal{P}(A)\vert{}$, $\vert{}\mathcal{P}(B)\vert{}$)Conjunto das Partes ($\mathcal{P}(A)$ e $\mathcal{P}(B)$) de forma iterativaExemplo de Partição VálidaProduto Cartesiano ($A \times B$)Verificação Manual de Inclusão ($A \subseteq B$ e $B \subseteq A$) sem uso de métodos embutidos como issubset()🔹 Como Executarpython P1/atividade_01_conjuntos/conjuntos.py
Entrada: Digite os elementos do Conjunto A separados por espaço (ex: 1 2 3) e em seguida os elementos do Conjunto B (ex: 2 3 4).📌 Atividade 2 – Divisibilidade, MDC e MMCDiretório: P1/atividade_02_divisibilidade/Código-fonte: divisibilidade.pyRelatório em PDF: documento_atividade_02.pdf🔹 DescriçãoPrograma para análise de propriedades de divisibilidade e cálculo de Máximo Divisor Comum (MDC) e Mínimo Múltiplo Comum (MMC) entre dois números inteiros.🔹 Operações Implementadas (Manualmente)Divisão Inteira (DIV / //) e Resto (MOD / %) garantindo a condição $0 \le r < \vert{}b\vert{}$Algoritmo de Euclides: Implementação iterativa com laço while para determinação do MDC com exibição detalhada de cada etapa da divisão no terminal, sem o uso de math.gcd()Cálculo do MMC fundamentado no produto dos números e seu MDC:
$$\text{MMC}(a, b) = \frac{\vert{}a \times b\vert{}}{\text{MDC}(a, b)}$$🔹 Como Executarpython P1/atividade_02_divisibilidade/divisibilidade.py
Entrada: Informe dois números inteiros (dividendo e divisor, garantindo divisor $b \neq 0$). Exemplo: 48 e 18.🛠️ Requisitos e TecnologiasLinguagem: Python 3.xRegra de Implementação: Algoritmos desenvolvidos com lógica própria (laços for/while e condicionais if/else), respeitando a restrição do uso de funções prontas de alto nível para operações matemáticas centrais.
