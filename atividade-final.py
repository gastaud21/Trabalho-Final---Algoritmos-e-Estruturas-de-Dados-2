import unicodedata

def normalize_string(s: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    ).lower()


def custom_hash(name: str, table_size: int) -> int:
    name = normalize_string(name)

    hash_value = 0
    base = 131
    mod  = 2**61 - 1

    for char in name:
        hash_value = (hash_value * base + ord(char)) % mod

    return hash_value % table_size



class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def insert(self, key: str) -> int:
        index = custom_hash(key, self.size)

        if self.table[index]:
            self.collisions += 1

        self.table[index].append(key)
        return index

    def print_table(self):
        for i, slot in enumerate(self.table):
            print(f"{i:02d}: {slot}")


nomes_teste = [
    "João", "João Silva", "Ana Clara", "Ana Cláudia", "Andressa",
    "André", "Roberta", "Roberto", "Carla", "Karl", "Marcos",
    "Marcus", "Pablo", "Pabllo", "Marcia", "Márcio", "Julia",
    "Júlio", "Carlos", "Karla"
]

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
