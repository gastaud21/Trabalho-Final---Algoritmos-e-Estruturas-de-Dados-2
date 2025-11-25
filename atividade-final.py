import unicodedata

# --------------------------------------
# 1. Função auxiliar para remover acentos
# --------------------------------------
def normalize_string(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn').lower()

# -------------------------------------------------------
# 2. Função de Hash personalizada para nomes (strings)
# -------------------------------------------------------
def custom_hash(name, table_size):
    """
    Hash baseado em:
    - Normalização (remove acentos e coloca minúsculo)
    - Combinação de pesos usando polinomial rolling hash
    - Base 131 (boa para strings)
    """
    name = normalize_string(name)

    hash_value = 0
    base = 131  # constante amplamente usada em hashing de strings

    for char in name:
        hash_value = (hash_value * base + ord(char)) % table_size

    return hash_value


# -------------------------------------------------------
# 3. Estrutura da Hash Table (usando Chaining)
# -------------------------------------------------------
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def insert(self, key):
        index = custom_hash(key, self.size)

        # colisão = slot já ocupado e chave diferente
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
    "Júlio", "Carlos", "Karla", "Ana", "Ane", "Anelise"
]

# -------------------------------------------------------
# 5. Definindo tamanho da tabela
# -------------------------------------------------------
"""
Escolha do tamanho:
- Usamos número primo para melhorar dispersão.
- Temos 23 nomes → ideal manter load factor < 0.75
- Tamanho escolhido: 31 (primo)
→ load factor ≈ 23/31 = 0.74 (ótimo)
"""

tamanho_tabela = 31
tabela = HashTable(tamanho_tabela)

# Inserindo e exibindo hash gerado
print("=== Índices Gerados ===")
resultados = []
for nome in nomes_teste:
    indice = tabela.insert(nome)
    resultados.append((nome, indice))
    print(f"{nome:15} → índice {indice}")

# Mostrar tabela final
print("\n=== Tabela Hash (Chaining) ===")
tabela.print_table()

# Colisões
print(f"\nTotal de colisões: {tabela.collisions}")
print(f"Load factor: {len(nomes_teste)}/{tamanho_tabela} = {len(nomes_teste)/tamanho_tabela:.2f}")
