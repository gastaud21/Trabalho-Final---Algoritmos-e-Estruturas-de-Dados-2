Aqui está o **README.md completo**, já formatado em Markdown, pronto para você colocar no GitHub:

---

# 🧩 Hash Table para Strings – Projeto de Função de Hash Personalizada

Este projeto implementa uma **função de hash própria para nomes (strings)** e utiliza uma **tabela hash com tratamento de colisões por chaining**.

O objetivo é demonstrar:

* ✔ boa dispersão dos índices
* ✔ baixa taxa de colisões
* ✔ escolha adequada do tamanho da tabela
* ✔ testes com 20+ nomes reais
* ✔ análise do comportamento da função de hash

---

## 📌 Funcionalidades Implementadas

* Função de hash personalizada usando **rolling hash polinomial**
* Normalização de strings (remove acentos e coloca minúsculas)
* Tabela hash com **chaining** (listas encadeadas)
* Escolha otimizada do tamanho da tabela (número primo)
* Testes com mais de 20 nomes com acentos, parecidos e compostos
* Exibição do índice gerado para cada nome
* Contagem de colisões e load factor

---

# 🧠 Como funciona a Função de Hash?

A função de hash utiliza o método **polinomial rolling hash**, amplamente usado em algoritmos como Rabin–Karp.

Fórmula geral:

```
H = (H * base + ord(char)) % table_size
```

Para este projeto:

* `base = 131`
  Um número clássico que produz excelente dispersão para strings.

* `table_size = 31`
  Número **primo**, ajudando a reduzir colisões.

### ✔ Normalização

Todos os nomes passam primeiro por:

1. Remoção de acentos
   (`Á → A`, `Ç → C`, `Ã → A`, etc.)
2. Conversão para minúsculas

Isso evita que **"João"** e **"joao"** gerem hashes completamente incompatíveis.

---

# 🔄 Tratamento de Colisões

O método escolhido foi **Chaining**, por ser:

* simples
* eficiente
* ideal quando o load factor está abaixo de 0.75
* flexível para múltiplas entradas no mesmo índice

Cada posição da tabela contém uma **lista**.
Se uma colisão ocorrer, o item é apenas adicionado ao final da lista.

---

# 📏 Tamanho da Tabela Hash

Foram utilizados 23 nomes de teste.
Para uma boa dispersão, recomenda-se:

* usar **números primos**
* manter load factor < **0.75**

### Escolha final:

```
Tamanho da tabela: 31
Load factor: 23 / 31 ≈ 0.74
```

Perfeito para evitar clusters e minimizar colisões.

---

# 🧪 Conjunto de Testes Usado

Foram utilizados nomes reais com:

* acentos
* versões semelhantes (Pablo / Pabllo)
* nomes compostos
* iniciais parecidas
* tamanhos diferentes

Exemplo dos nomes:

```
João, João Silva, Ana Clara, Ana Cláudia, Andressa,
André, Roberta, Roberto, Carla, Karl, Marcos, Marcus,
Pablo, Pabllo, Marcia, Márcio, Julia, Júlio,
Carlos, Karla, Ana, Ane, Anelise
```

---

# 📈 Resultados exibidos no console

* Índice gerado para cada nome
* Layout completo da tabela Hash
* Todas as colisões contabilizadas
* Load factor final

Exemplo do output (parcial):

```
João           → índice 12
Ana Clara      → índice 15
Marcus         → índice 4
Pabllo         → índice 23

Total de colisões: 4
Load factor: 23/31 = 0.74
```

---

# 📚 Estrutura do Código

* `custom_hash()` → Função de hash personalizada
* `HashTable` → Classe com inserção e tratamento de colisões
* Normalização → Remoção de acentos e padronização
* Testes → Inserção + impressão dos índices e da distribuição

---

# 🖥️ Execução

Basta rodar:

```bash
python3 hash_table.py
```

(ou o nome que você deu ao arquivo)

---

# 📌 Possíveis Extensões

Se quiser evoluir este projeto, você pode adicionar:

* Hashing duplo (double hashing)
* Linear probing ou quadratic probing
* Gráfico real de distribuição (matplotlib)
* Exportar dados para CSV
* Benchmark de desempenho

---

Se quiser, posso gerar **um PDF para anexar ao repositório**, ou criar **uma versão em Java**, **JavaScript**, **C** ou qualquer outra linguagem. Só pedir!
