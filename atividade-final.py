import unicodedata

# --------------------------------------
# 1. Função auxiliar para remover acentos
# --------------------------------------
def normalize_string(s: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    ).lower()


# -------------------------------------------------------
# 2. Função de Hash personalizada para nomes (strings)
# -------------------------------------------------------
def custom_hash(name: str, table_size: int) -> int:
    """
    Hash baseado em:
    - Normalização (remove acentos e coloca minúsculo)
    - Rolling hash polinomial
    - Usa módulo grande e só no final reduz para o tamanho da tabela

    Essa abordagem reduz padrões e melhora a dispersão,
    diminuindo colisões mesmo com tabela pequena (ex: 15 posições).
    """
    name = normalize_string(name)

    hash_value = 0
    base = 131               # base boa para hashing de strings
    mod  = 2**61 - 1         # primo grande (Mersenne-like)

    for char in name:
        hash_value = (hash_value * base + ord(char)) % mod

    # Só aqui reduzimos para o tamanho da tabela
    return hash_value % table_size


# -------------------------------------------------------
# 3. Estrutura da Hash Table (usando Chaining)
# -------------------------------------------------------
class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def insert(self, key: str) -> int:
        index = custom_hash(key, self.size)

        # colisão = slot já ocupado (independente de ser igual ou não)
        if self.table[index]:
            self.collisions += 1

        self.table[index].append(key)
        return index

    def print_table(self):
        for i, slot in enumerate(self.table):
            print(f"{i:02d}: {slot}")


# -------------------------------------------------------
# 4. Testes com +20 nomes
# -------------------------------------------------------
nomes_teste = [
    "João", "João Silva", "Ana Clara", "Ana Cláudia", "Andressa",
    "André", "Roberta", "Roberto", "Carla", "Karl", "Marcos",
    "Marcus", "Pablo", "Pabllo", "Marcia", "Márcio", "Julia",
    "Júlio", "Carlos", "Karla"
]

# -------------------------------------------------------
# 5. Tamanho da tabela = 15 posições
# -------------------------------------------------------
tamanho_tabela = 16
tabela = HashTable(tamanho_tabela)

print("=== Índices Gerados ===")
resultados = []
for nome in nomes_teste:
    indice = tabela.insert(nome)
    resultados.append((nome, indice))
    print(f"{nome:15} → índice {indice}")

print("\n=== Tabela Hash (Chaining) ===")
tabela.print_table()

print(f"\nTotal de colisões: {tabela.collisions}")
print(
    f"Load factor: {len(nomes_teste)}/{tamanho_tabela} "
    f"= {len(nomes_teste)/tamanho_tabela:.2f}"
)
