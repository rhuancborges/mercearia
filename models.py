from datetime import datetime

# --------------------------------------
'''Aqui, modelamos todos os objetos que precisaremos no projeto.
Utilizamos o método construtor para criar atributos de cada um dos objetos
ao criar suas instâncias'''
# --------------------------------------

class Categoria:
    def __init__(self, categoria):
        self.categoria=categoria
    
class Produtos:

    def __init__(self, nome, preco, categoria: Categoria):
        self.nome=nome
        self.preco=preco
        self.categoria=categoria # a categoria do produto remete ao objeto Categoria

class Estoque:

    def __init__(self, produto: Produtos, quantidade):
        self.produto=produto # o Produto do estoque refere-se ao objeto produtos
        self.quantidade=quantidade

class Venda:

    def __init__(self, itens_vendidos: Produtos, vendedor, comprador, quantidade_vendida, data=datetime.now().strftime('%d/%m/%y')):
        self.itens_vendidos=itens_vendidos # refere aos produtos
        self.vendedor=vendedor
        self.comprador=comprador
        self.quantidade_vendida=quantidade_vendida
        self.data=data # formatação de data atual, biblioteca importada
        
class Fornecedor:

    def __init__(self, nome, telefone, cnpj, categoria: Categoria):
        self.nome=nome
        self.telefone=telefone
        self.cnpj=cnpj
        self.categoria=categoria # refere-se ao objeto Categoria, indicando a categoria de produto fornecido

class Cliente:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome=nome
        self.telefone=telefone
        self.cpf=cpf
        self.email=email
        self.endereco=endereco

class Funcionario(Cliente):

    def __init__(self,clt, nome, telefone, cpf, email, endereco):
        self.clt=clt
        super().__init__(nome, telefone, cpf, email, endereco) # chama as características do objeto ascendente (de quem esse herda)
