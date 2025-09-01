# Exemplo de classe com modelo de dados

class Biblioteca:
    def __init__(self, nome):
        print(f"📚 Criando biblioteca: {nome}")
        self.nome = nome
        self.livros = {
            'python': 'Aprenda Python',
            'java': 'Java para Iniciantes',
            'javascript': 'JS Moderno'
        }
        self.emprestimos = []
    
    def __getitem__(self, codigo):
        """Permite buscar livro com biblioteca['python']"""
        if codigo in self.livros:
            return self.livros[codigo]
        return "Livro não encontrado"
    
    def emprestar(self, codigo):
        if codigo in self.livros:
            self.emprestimos.append(codigo)
            return f"Livro '{self.livros[codigo]}' emprestado!"
        return "Livro não disponível"

# Testando tudo junto
print("=== EXEMPLO COMPLETO ===")

# __init__ é chamado aqui
bib = Biblioteca("Biblioteca Central")

# Vendo __dict__
print(f"\nAtributos da biblioteca: {bib.__dict__}")

# Usando __getitem__
print(f"\nLivro de Python: {bib['python']}")
print(f"Livro de Java: {bib['java']}")
print(f"Livro inexistente: {bib['php']}")

# Emprestando um livro
print(f"\n{bib.emprestar('python')}")

# Vendo __dict__ após empréstimo
print(f"\nAtributos após empréstimo: {bib.__dict__}")

