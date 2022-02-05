from models import *

class CategoriaDAO:

    # Método para escrever categorias em um arquivo
    @classmethod
    def salvar(cls, categoria):
        with open('categorias.txt', 'a') as arq:
            arq.writelines(f'{categoria.categoria}'.capitalize())
            arq.writelines('\n')

    # Método para ler o arquivo categorias
    @classmethod
    def ler(cls):
        with open('categorias.txt', 'r') as arq:
            cls.categoria=arq.readlines()
        
        # Retira o \n da lista de categorias
        cls.categoria=list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        # Retorna as categorias como instâncias do objeto Categoria modelado 
        cat=[]
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat

class ProdutosDAO:

    # Método para escrever produtos no arquivo
    @classmethod
    def salvar(cls, nome, preco, categoria):
        with open('produtos.txt', 'a') as arq:
            arq.writelines(f'{nome} ')
            arq.writelines(f'{preco} ')
            arq.writelines(f'{categoria} ')
            arq.writelines('\n')

    # Método para ler o arquivo de produtos
    @classmethod
    def ler(cls):
        with open('produtos.txt', 'r') as arq:
            a=[]
            # Lê as linhas do arquivo (cada linha é um produto). Cada elemento da lista retornada é uma string
            res=arq.readlines()
            # A cada elemento da lista, esse é splitado de modo que cada elemento vire uma lista, com cada atributo do produto sendo um elemento
            for i in range(0,len(res)):
                a.append(res[i].split())
            print(a)
            print(res)
                   
class EstoqueDAO:
    # Método para escrever produtos e suas quantidades no arquivo
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(f'{produto.nome} ')
            arq.writelines(f'{produto.preco} ')
            arq.writelines(f'{produto.categoria} ')
            arq.writelines(f'{quantidade} ')
            arq.writelines('\n')

    # Método para ler o arquivo de estoque
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            a=[]
            res=arq.readlines()
            for i in range(0,len(res)):
                a.append(res[i].split())

            # Retorna o estoque como instâncias do objeto Estoque modelado, que possui instância do objeto Produtos 
            est=[]
            for i in a:
                est.append(Estoque(Produtos(i[0],i[1],i[2]), i[3]))
            return est

class VendaDAO:

    # Método de classe para salvar venda
    @classmethod
    def salvar(cls,venda:Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(f'{venda.itens_vendidos.nome} ')
            arq.writelines(f'{venda.itens_vendidos.categoria} ')
            arq.writelines(f'{venda.itens_vendidos.preco} ')
            arq.writelines(f'{venda.vendedor} ')
            arq.writelines(f'{venda.comprador} ')
            arq.writelines(f'{venda.quantidade_vendida} ')
            arq.writelines(f'{venda.data} ')
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            res=arq.readlines()
            a=[]
            for i in range(0,len(res)):
                a.append(res[i].split())

            est=[]
            for i in a:
                est.append(Venda(Produtos(i[0],i[2], i[1]), i[3], i[4], i[5], i[6]))
            return est

class FornecedorDAO:

    @classmethod
    def salvar(cls,fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(f'{fornecedor.nome} ')
            arq.writelines(f'{fornecedor.telefone} ')
            arq.writelines(f'{fornecedor.cnpj} ')
            arq.writelines(f'{fornecedor.categoria.categoria} ')
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            res=arq.readlines()
            a=[]
            for i in range(0,len(res)):
                a.append(res[i].split())

            est=[]
            for i in a:
                est.append(Fornecedor(i[0], i[1], i[2], Categoria(i[3])))
            return est

class ClienteDAO:

    @classmethod
    def salvar(cls,cliente: Cliente):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(f'{cliente.nome} ')
            arq.writelines(f'{cliente.telefone} ')
            arq.writelines(f'{cliente.cpf} ')
            arq.writelines(f'{cliente.email} ')
            arq.writelines(f'{cliente.endereco} ')
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            res=arq.readlines()
            a=[]
            for i in range(0,len(res)):
                a.append(res[i].split())
            
            est=[]
            for i in a:
                est.append(Cliente(i[0], i[1], i[2], i[3], i[4]))
            return est

class FuncionarioDAO:

    @classmethod
    def salvar(cls,funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(f'{funcionario.nome} ')
            arq.writelines(f'{funcionario.clt} ')
            arq.writelines(f'{funcionario.cpf} ')
            arq.writelines(f'{funcionario.email} ')
            arq.writelines(f'{funcionario.telefone} ')
            arq.writelines(f'{funcionario.endereco} ')
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            res=arq.readlines()
            a=[]
            for i in range(0,len(res)):
                a.append(res[i].split())
            
            est=[]
            for i in a:
                est.append(Funcionario(i[1], i[0], i[2], i[3], i[4], i[5]))
            return est