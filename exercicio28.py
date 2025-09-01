# Exemplo de Classes com modelo de dados 

class Carrinho:
    """Exemplo completo de Modelo de Dados"""
    
    def __init__(self, cliente):
        """Construtor - inicializa o objeto"""
        self.cliente = cliente
        self.itens = []
        self.total = 0
    
    def __str__(self):
        """Representação amigável para print()"""
        return f"Carrinho de {self.cliente} com {len(self.itens)} itens"
    
    def __repr__(self):
        """Representação técnica para desenvolvedores"""
        return f"Carrinho(cliente='{self.cliente}', itens={len(self.itens)})"
    
    def __len__(self):
        """Permite usar len(carrinho)"""
        return len(self.itens)
    
    def __getitem__(self, indice):
        """Permite acessar carrinho[0], carrinho[1], etc."""
        return self.itens[indice]
    
    def __setitem__(self, indice, valor):
        """Permite modificar carrinho[0] = novo_item"""
        self.itens[indice] = valor
        self._atualizar_total()
    
    def __add__(self, item):
        """Permite usar carrinho + item"""
        novo_carrinho = Carrinho(self.cliente)
        novo_carrinho.itens = self.itens.copy()
        novo_carrinho.itens.append(item)
        novo_carrinho._atualizar_total()
        return novo_carrinho
    
    def __eq__(self, outro):
        """Permite comparar carrinho1 == carrinho2"""
        return (self.cliente == outro.cliente and 
                self.itens == outro.itens)
    
    def __iter__(self):
        """Permite usar for item in carrinho"""
        return iter(self.itens)
    
    def _atualizar_total(self):
        """Método auxiliar para calcular total"""
        self.total = sum(item.get('preco', 0) for item in self.itens)
    
    def adicionar(self, nome, preco):
        """Método normal para adicionar itens"""
        item = {'nome': nome, 'preco': preco}
        self.itens.append(item)
        self._atualizar_total()

# Testando o Modelo de Dados
print("=== TESTANDO MODELO DE DADOS ===")

# __init__ é chamado
carrinho = Carrinho("João")

# Adicionando itens
carrinho.adicionar("Notebook", 2500)
carrinho.adicionar("Mouse", 50)

# __str__ é chamado pelo print()
print(f"Carrinho: {carrinho}")

# __repr__ é chamado quando você digita só o nome
print(f"Repr: {repr(carrinho)}")

# __len__ é chamado pelo len()
print(f"Quantidade de itens: {len(carrinho)}")

# __getitem__ é chamado pelos colchetes
print(f"Primeiro item: {carrinho[0]}")
print(f"Segundo item: {carrinho[1]}")

# __iter__ é chamado pelo for
print("Itens no carrinho:")
for item in carrinho:
    print(f"  - {item['nome']}: R\$ {item['preco']}")

# __add__ é chamado pelo operador +
novo_item = {'nome': 'Teclado', 'preco': 150}
carrinho_novo = carrinho + novo_item
print(f"Novo carrinho: {len(carrinho_novo)} itens")

# __eq__ é chamado pelo operador ==
carrinho2 = Carrinho("João")
carrinho2.adicionar("Notebook", 2500)
carrinho2.adicionar("Mouse", 50)
print(f"Carrinhos são iguais? {carrinho == carrinho2}")