## 🧮 Explicação do Código: Hash Table com Normalização

-----

### 1\. Pré-processamento: `normalize_string`

Esta função é crucial para garantir que o hashing trate nomes semelhantes, mas com ou sem acentos, da mesma forma (ex: "João" e "Joao").

  * **`import unicodedata`**: Importa o módulo para trabalhar com a Base de Dados de Caracteres Unicode.
  * **`unicodedata.normalize('NFD', s)`**: Aplica a forma de **Normalização por Decomposição Canônica (NFD)**. Isso separa caracteres acentuados em sua **letra base** e seu **acento** (o marcador diacrítico).
      * *Exemplo:* 'á' se torna 'a' + '́' (o acento agudo).
  * **`unicodedata.category(c) != 'Mn'`**: Filtra os caracteres. `'Mn'` significa "Mark, Nonspacing" (Marca, Sem Espaçamento), que são os acentos.
      * Ao filtrar os 'Mn', a função **remove todos os acentos**.
  * **`.lower()`**: Converte a string resultante para **minúsculas**.
  * **Resultado:** A string é padronizada, tornando o hash **insensível a acentos e case-insensitive** (não diferencia maiúsculas de minúsculas).
      * *Exemplo:* `normalize_string("Márcio")` retorna `"marcio"`.

-----

### 2\. Função de Hashing Personalizada: `custom_hash`

Esta função calcula o valor hash usando o algoritmo **Polynomial Rolling Hash**.

  * **Normalização**: Primeiro, ela normaliza o `name` usando `normalize_string(name)`.
  * **Inicialização**:
      * `hash_value = 0`: O valor hash acumulado.
      * `base = 131`: Uma base prima escolhida para garantir uma boa distribuição.
      * `mod = 2**61 - 1`: Um primo grande (Mersenne-like) para o módulo, usado para evitar *overflow* e manter a distribuição uniforme.
  * **Cálculo do Hash (Loop)**:
    ```python
    hash_value = (hash_value * base + ord(char)) % mod
    ```
      * Para cada caractere (`char`):
        1.  O `hash_value` anterior é multiplicado pela `base`.
        2.  O valor numérico do caractere (`ord(char)`, geralmente o código ASCII/Unicode) é adicionado.
        3.  Tudo é calculado **módulo `mod`**.
  * **Mapeamento para o Tamanho da Tabela**:
    ```python
    return hash_value % table_size
    ```
      * O hash final, que é um número muito grande, é calculado **módulo `table_size`** para produzir um índice válido dentro do array da tabela hash (de `0` a `table_size - 1`).

-----

### 3\. Classe da Tabela Hash: `HashTable`

Esta classe gerencia a estrutura de dados da Tabela Hash.

  * **`__init__(self, size)`**:
      * Cria a lista interna `self.table`, que é uma lista de listas (ou *buckets*). Cada *bucket* é inicializado como uma lista vazia (`[[] for _ in range(size)]`).
      * `self.collisions = 0`: Contador para rastrear o número de colisões.
  * **`insert(self, key)`**:
    1.  **Calcula o Índice**: `index = custom_hash(key, self.size)` usa a chave (`key`) para encontrar a posição correta.
    2.  **Verifica Colisão**: `if self.table[index]: self.collisions += 1`
          * Se o *bucket* no `index` já contiver elementos, significa que ocorreu uma **colisão**.
    3.  **Encadeamento (Chaining)**: `self.table[index].append(key)`
          * Adiciona a nova `key` à lista no índice calculado. Este é o método de **encadeamento**, onde múltiplas chaves que mapeiam para o mesmo índice são armazenadas na mesma lista.

-----

### 4\. Execução e Análise

O código, em seguida, demonstra o uso:

1.  **Inicialização**: Cria a tabela com `tamanho_tabela = 16`.
2.  **Inserção**: Itera sobre `nomes_teste`, inserindo-os e exibindo o índice.
      * *Note as colisões intencionais:* Nomes como "João" e "João Silva" ou "Marcos" e "Marcus" tendem a colidir devido à similaridade de seus hashes.
3.  **Análise Final**:
      * Exibe a estrutura da tabela (índices com suas listas de chaves).
      * Mostra o **Total de colisões**.
      * Calcula o **Load Factor** ($\alpha$), que é a razão entre o número de itens (`len(nomes_teste)`) e o tamanho da tabela (`tamanho_tabela`).
          * Um *load factor* alto ($> 1$) ou muito próximo de $1$ indica que a tabela está ficando cheia e as colisões são mais prováveis, o que pode degradar a performance de busca.