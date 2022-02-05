from turtle import ycor
from models import *
from dao import *
from datetime import datetime

class CategoriaController:

    # Método para cadastrar categorias
    def cadastro_categoria(self, categoria):
        existe=False
        x=CategoriaDAO.ler()
        # Verificação se a categoria pedida já existe no arquivo
        for i in x:
            if i==categoria:
                existe=True
        if existe==False:
            # Se não existe, salva a categoria
            CategoriaDAO.salvar(Categoria(categoria))
            print('Categoria salva com sucesso')
        else:
            print('A categoria digitada já existe')

    # Método para remover categorias
    def remover_categoria(self,categoria_rem):
        x=CategoriaDAO.ler()
        # Filtra se um elemento da lista de categorias corresponde ? categoria que se deseja remover
        cat=list(filter(lambda x: x.categoria == categoria_rem, x))
        if len(cat)<=0: # Se n?o retornar nenhum elemento correspondente
            print('Essa categoria não existe')
        else:
            # Percorre a lista de categorias e remove a que se deseja (remove da mem?ria RAM, ou seja, da vari?vel x criada)
            for i in range(len(x)):
                if x[i].categoria==categoria_rem:
                    del x[i]
                    break
            print('Categoria removida com sucesso')

            with open('categorias.txt', 'w') as arq:
                # Reescreve no arquivo as categorias armazenadas na vari?vel x
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')  

        estoque = EstoqueDAO.ler()
        fornecedores=FornecedorDAO.ler()

        estoque=list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, Categoria('Sem Categoria'.replace(' ', ''))), x.quantidade) if x.produto.categoria==categoria_rem else x, estoque))
        fornecedores=list(map(lambda x: Fornecedor(x.nome, x.telefone, x.cnpj, Categoria('Sem Categoria'.replace(' ', ''))) if x.categoria.categoria==categoria_rem else x, fornecedores))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(f'{i.produto.nome} ')
                arq.writelines(f'{i.produto.preco} ')
                arq.writelines(f'{i.produto.categoria} ')
                arq.writelines(f'{i.quantidade} ')
                arq.writelines('\n')
        
        with open('fornecedores.txt', 'w') as arq:
            for i in fornecedores:
                arq.writelines(f'{i.nome} ')
                arq.writelines(f'{i.telefone} ')
                arq.writelines(f'{i.cnpj} ')
                arq.writelines(f'{i.categoria.categoria} ')
                arq.writelines('\n')

    # Método para alterar categorias
    def alterar_categoria(self,categoria_alt,nova_categoria):
        x=CategoriaDAO.ler()
        # Filtra se um elemento da lista de categorias corresponde ? categoria que se deseja alterar
        cat=list(filter(lambda x: x.categoria == categoria_alt, x))
        if len(cat)<=0: # Se n?o retornar nenhum elemento correspondente
            print('Essa categoria não existe')
        else:
            # Filtra se um elemento da lista de categorias corresponde ? categoria para a qual se deseja alterar
            cat1=list(filter(lambda x: x.categoria == nova_categoria, x))
            if len(cat1)==0: # Se n?o retornar nenhum elemento correspondente
                # Altera na lista a categoria
                x=list(map(lambda x: x.categoria.replace(categoria_alt, nova_categoria), x))
                print('Categoria alterada com sucesso')

                with open('categorias.txt', 'w') as arq:
                    # Reescreve no arquivo as categorias armazenadas na vari?vel x, essa j? alterada
                    for i in x:
                        arq.writelines(i)
                        arq.writelines('\n')
            else: # Se a categoria para a qual se deseja alterar j? existe na lista
                print('A categoria para a qual deseja alterar já existe')
            
            estoque = EstoqueDAO.ler()
            fornecedores=FornecedorDAO.ler()

            estoque=list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, Categoria(nova_categoria)), x.quantidade) if x.produto.categoria==categoria_alt else x, estoque))
            fornecedores=list(map(lambda x: Fornecedor(x.nome, x.telefone, x.cnpj, Categoria(nova_categoria)) if x.categoria.categoria==categoria_alt else x, fornecedores))

            with open('estoque.txt', 'w') as arq:
                for i in estoque:
                    arq.writelines(f'{i.produto.nome} ')
                    arq.writelines(f'{i.produto.preco} ')
                    arq.writelines(f'{i.produto.categoria} ')
                    arq.writelines(f'{i.quantidade} ')
                    arq.writelines('\n')
            
            with open('fornecedores.txt', 'w') as arq:
                for i in fornecedores:
                    arq.writelines(f'{i.nome} ')
                    arq.writelines(f'{i.telefone} ')
                    arq.writelines(f'{i.cnpj} ')
                    arq.writelines(f'{i.categoria.categoria} ')
                    arq.writelines('\n')

    # M?todo para mostrar as categorias
    def mostrar_categoria(self):
        categorias=CategoriaDAO.ler()
        if len(categorias)==0: # Se o arquivo de categorias estiver vazio
            print('Não há categorias cadastradas')
        else:
            print('-'*20)
            print('LISTA DE CATEGORIAS')
            print('-'*20)
            for i in categorias:
                print(f'- {i.categoria.capitalize()}')

class EstoqueController:

    # Método para cadastrar produtos no estoque
    def cadastrar_produto(self, nome, preco, categoria, quantidade):
        x=EstoqueDAO.ler() 
        y=CategoriaDAO.ler()

        cat=list(filter(lambda x: x.categoria == categoria, y)) # Filtra se a categoria do produto a ser cadastrado já existe na lista de categorias
        pr = list(filter(lambda x: x.produto.nome == nome, x)) # Filtra se o nome do produto a ser cadastrado já existe no estoque

        if len(cat)>0: # Se a categoria pedida no cadastro á? existir
            if len(pr)==0: # Se já não houver produto no estoque com o nome pedido
                produto=Produtos(nome, preco, categoria)
                EstoqueDAO.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('O produto já existe no estoque')
        else:
            print('Categoria inexistente')

    # Método para remover produto no estoque
    def remover_produto(self, nome):
        x=EstoqueDAO.ler()

        ex=list(filter(lambda x: x.produto.nome==nome, x))

        if len(ex)>0:
            for i in range(len(x)):
                if x[i].produto.nome==nome:
                    del x[i]
                    print('Produto removido com sucesso')
                    break
        else:
            print('O produto não existe')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(f'{i.produto.nome} ')
                arq.writelines(f'{i.produto.preco} ')
                arq.writelines(f'{i.produto.categoria} ')
                arq.writelines(f'{i.quantidade} ')
                arq.writelines('\n')

    # Método para alterar produto no estoque
    def alterar_produto(self, nome_alt, nome_novo, preco_novo, categoria_nova, quantidade_nova):
        x=EstoqueDAO.ler()
        y=CategoriaDAO.ler()

        cat=list(filter(lambda x: x.categoria==categoria_nova, y)) # Filtra se a categoria para a qual se deseja alterar existe na lista de categorias

        if len(cat)>0: # Se existe a categoria
            est=list(filter(lambda x: x.produto.nome==nome_alt,x)) # Filtra se o nome do produto que se deseja alterar existe no estoque 

            if len(est)>0: # Se existe o produto

                ex=list(filter(lambda x: x.produto.nome==nome_novo, x)) # Filtra se o nome do produto para o qual se deseja alterar j? existe no estoque

                if len(ex)==0: # Se o nome novo ainda n?o existe
                    # Altera a lista x, instanciando os novos atributos caso o nome do elemento da lista corresponda ao nome do produto que se deseja alterar
                    x=list(map(lambda x: Estoque(Produtos(nome_novo, preco_novo, categoria_nova), quantidade_nova) if (x.produto.nome==nome_alt) else(x), x))
                    print('Produto alterado com sucesso')
                else:
                    print('O nome para o qual se deseja alterar o produto já existe')
            else:
                print('O produto que se deseja alterar não existe')

            with open('estoque.txt', 'w') as arq:
                # Reescreve a lista de produtos no estoque armazenados na vari?vel x já alterada
                for i in x:
                    arq.writelines(f'{i.produto.nome} ')
                    arq.writelines(f'{i.produto.preco} ')
                    arq.writelines(f'{i.produto.categoria} ')
                    arq.writelines(f'{i.quantidade} ')
                    arq.writelines('\n')
        else:
            print('A categoria para a qual se deseja alterar não existe')

    # Método para mostrar Estoque
    def mostrar_estoque(self):
        est=EstoqueDAO.ler()
        if len(est)==0: #Se o estoque tiver vazio
            print('O estoque está vazio')
        else:
            print('-'*20)
            print('ESTOQUE')
            print('-'*20)
            for i in est:
                print(f'Produto: {i.produto.nome}; Preço: R${i.produto.preco}; Categoria: {i.produto.categoria}; Quantidade: {i.quantidade} unidades ou kg ')

class VendaController:
    
    # Método para cadastrar venda
    def cadastrar_venda(self,nome_produto, vendedor, comprador, quantidade_vendida):
        x=EstoqueDAO.ler()
        ex=list(filter(lambda x: x.produto.nome==nome_produto, x)) # Filtra se o produto a ser vendido existe no estoque

        temp=[]
        existe=False
        if len(ex)>0: #S e existe o produto
            for i in x: # Para cada produto na lista de produtos do estoque
                if (i.produto.nome==nome_produto) and (int(i.quantidade)>=int(quantidade_vendida)): # Se o produto iterado for o que será vendido e tem quantidade suficiente
                    i.quantidade = int(i.quantidade)-int(quantidade_vendida) # Subtrai a quantidade vendida
                    vendido=Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidade_vendida) # Instancia a venda
                    valor_compra = int(quantidade_vendida)*float(i.produto.preco) # Calcula o valor de compra
                    existe=True
                    VendaDAO.salvar(vendido) # Salva a venda
                    print('Produto salvo com sucesso!')
                elif (i.produto.nome==nome_produto) and not(int(i.quantidade)>=int(quantidade_vendida)): # Se o produto iterado for o que será vendido e não tem quantidade suficiente
                    print(f'O produto {i.produto.nome} não possui quantidade disponível')
                
                temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade]) # Acrescenta na lista temporária os produtos
                arq = open('estoque.txt', 'w')
                arq.write('') # Limpa o arquivo estoque

                for i in temp:
                    # Reescreve o arquivo estoque com o produto vendido com quantidade alterada 
                    with open('estoque.txt', 'a') as arq: 
                        arq.writelines(f'{i[0].nome} ')
                        arq.writelines(f'{i[0].preco} ')
                        arq.writelines(f'{i[0].categoria} ')
                        arq.writelines(f'{i[1]} ')
                        arq.writelines('\n')
                
            if existe:
                return valor_compra
        else:
            print('Não existe esse produto no estoque')

    # Método para mostrar um relatório de produtos em ordem decrescente em quantidade
    def relatorio_produtos(self):
        x=VendaDAO.ler()
        produto=[]

        # Percorre a lista em x
        if len(x)==0:
            print('Não há vendas realizadas')
        else:
            for i in x:
                nome=i.itens_vendidos.nome 
                quantidade=int(i.quantidade_vendida)
                tamanho = list(filter(lambda x: x['produto']==nome, produto)) # Filtra, na lista cadastrada (produto) se já existe o nome passado
                if len(tamanho)>0: # Se existe
                    # Soma a quantidade do produto encontrado com a quantidade dada atualmente se o produto tiver nome já existente na lista
                    produto = list(map(lambda x: {'produto': nome, 'quantidade': x['quantidade']+quantidade} if x['produto']==nome else(x), produto))
                else: # Se não existe  
                    # Adiciona o produto e sua respectiva quantidade  
                    produto.append({'produto': nome, 'quantidade': quantidade})

            # Sorteia o dicionário (a lista de dicionários) por meio da chave quantidade em ordem decrescente
            ordenado=sorted(produto, key=lambda k: k['quantidade'], reverse=True)

            print('-'*18)
            print('RELATÓRIO DE VENDAS')
            print('-'*18)
            for i in ordenado:
                nome_produto=i['produto']
                quantidade_produto=i['quantidade']
                print(f'- Produto: {nome_produto} ; Quantidade: {quantidade_produto}')

    def mostrar_vendas(self, data_inicio, data_final):
        x=VendaDAO.ler()
        dataInicio = datetime.strptime(data_inicio, '%d/%m/%y')
        dataTermino = datetime.strptime(data_final, '%d/%m/%y')

        vendas_selecionadas = list(filter(lambda x: dataInicio<= datetime.strptime(x.data, '%d/%m/%y') <=dataTermino, x))
        total_vendas=0
        if len(x)==0:
            print('Não há vendas cadastradas')
        elif len(vendas_selecionadas)==0:
            print('Não foram realizadas vendas nesse período')
        else:
            for i in vendas_selecionadas:
                print('-'*15)
                print(f'Nome: {i.itens_vendidos.nome}\n'
                f'Categoria: {i.itens_vendidos.categoria}\n'
                f'Preço: R${i.itens_vendidos.preco}\n'
                f'Vendedor: {i.vendedor}\n'
                f'Comprador: {i.comprador}\n'
                f'Quantidade vendida: {i.quantidade_vendida}\n'
                f'Data: {i.data}')
                total_vendas+=float(i.itens_vendidos.preco)*int(i.quantidade_vendida)
            print('-'*15)
            print(f'Total de vendas: R${total_vendas}')

class FornecedorController:

    def cadastrar_fornecedor(self,  nome, telefone, cnpj, categoria):
        x=FornecedorDAO.ler()
        y=CategoriaDAO.ler()

        lista_cnpj=list(filter(lambda x: x.cnpj==cnpj, x))
        lista_telefone=list(filter(lambda x: x.telefone==telefone, x))
        catex=list(filter(lambda x: x.categoria==categoria, y))

        if len(lista_cnpj)>0:
            print('Este CNPJ já existe')
        elif len(lista_telefone)>0:
            print('Este telefone já existe')
        elif len(catex)==0:
            print('Essa categoria de produto não existe na lista de categorias cadastradas')
        else:
            if len(cnpj)==14 and 10<=len(telefone)<=11:
                FornecedorDAO.salvar(Fornecedor(nome, telefone, cnpj, Categoria(categoria)))
                print('Fornecedor cadastrado com sucesso')
            else:
                print('Digite um telefone ou um CNPJ válido(s)')
        
    def alterar_fornecedor(self, nome_alt, nome_novo, cnpj_novo, telefone_novo, categoria_nova):
        x=FornecedorDAO.ler()

        ex = list(filter(lambda x: x.nome==nome_alt, x)) 

        if len(ex)>0: 
            est = list(filter(lambda x: x.cnpj==cnpj_novo, x)) 
            if len(est)>0: 
                y=list(filter(lambda x: (x.nome==nome_novo and x.cnpj==cnpj_novo), x))
                if len(y)==1:
                    x = list(map(lambda x: Fornecedor(nome_novo, telefone_novo, cnpj_novo, Categoria(categoria_nova)) if x.nome==nome_alt else x, x))
                    print('Fornecedor alterado com sucesso')
                else:
                    print('Este CNPJ já existe')
            else:
                x = list(map(lambda x: Fornecedor(nome_novo, telefone_novo, cnpj_novo, Categoria(categoria_nova)) if x.nome==nome_alt else x, x))
                print('Fornecedor alterado com sucesso')
        else:
            print('Este fornecedor não está cadastrado')

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(f'{i.nome} ')
                arq.writelines(f'{i.telefone} ')
                arq.writelines(f'{i.cnpj} ')
                arq.writelines(f'{i.categoria.categoria} ')
                arq.writelines('\n')

    def remover_fornecedor(self, nome):
        x=FornecedorDAO.ler()

        ex=list(filter(lambda x: x.nome==nome, x))

        if len(ex)>0:
            for i in range(len(x)):
                if x[i].nome==nome:
                    del x[i]
                    print('Fornecedor deletado com sucesso')
                    break
        else:
            print('Este fornecedor já não existe')

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(f'{i.nome} ')
                arq.writelines(f'{i.telefone} ')
                arq.writelines(f'{i.cnpj} ')
                arq.writelines(f'{i.categoria.categoria} ')
                arq.writelines('\n')

    def mostrar_fornecedores(self):
        x=FornecedorDAO.ler()

        if len(x)==0:
            print('Não há fornecedores cadastrados')
        else:
            print('-'*18)
            print('LISTA DE FORNECEDORES')
            print('-'*18)

            for i in x:
                print(f'- Fornecedor: {i.nome.capitalize()} | Telefone: {i.telefone} | CNPJ: {i.cnpj} | Categoria: {i.categoria.categoria}')

class ClienteController:

    def cadastrar_cliente(self, nome, telefone, cpf, email, endereco):
        x=ClienteDAO.ler()

        lista_cpf=list(filter(lambda x: x.cpf==cpf, x))
        
        if len(lista_cpf)>0:
            print('Este CPF já existe')
        else:
            if len(cpf)==11 and 10<=len(telefone)<=11:
                ClienteDAO.salvar(Cliente(nome,telefone,cpf,email,endereco))
                print('Cliente cadastrado com sucesso')
            else:
                print('Digite um telefone ou um CPF válido(s)')
        
    def alterar_cliente(self, nome_alt, nome_novo, cpf_novo, telefone_novo, email_novo, endereco_novo):
        x=ClienteDAO.ler()

        ex = list(filter(lambda x: x.nome==nome_alt, x))

        if len(ex)>0:
            est = list(filter(lambda x: x.cpf==cpf_novo, x))
            if len(est)>0:
                print('Este CPF já existe')
            else:
                x = list(map(lambda x: Cliente(nome_novo, telefone_novo, cpf_novo, email_novo, endereco_novo) if x.nome==nome_alt else x, x))
                print('Cliente alterado com sucesso')
        else:
            print('Este cliente não está cadastrado')

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(f'{i.nome} ')
                arq.writelines(f'{i.telefone} ')
                arq.writelines(f'{i.cpf} ')
                arq.writelines(f'{i.email} ')
                arq.writelines(f'{i.endereco} ')
                arq.writelines('\n')

    def remover_cliente(self, nome):
        x=ClienteDAO.ler()

        ex=list(filter(lambda x: x.nome==nome, x))

        if len(ex)>0:
            for i in range(len(x)):
                if x[i].nome==nome:
                    del x[i]
                    print('Cliente deletado com sucesso')
                    break
        else:
            print('Este cliente já não existe')

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(f'{i.nome} ')
                arq.writelines(f'{i.telefone} ')
                arq.writelines(f'{i.cpf} ')
                arq.writelines(f'{i.email} ')
                arq.writelines(f'{i.endereco} ')
                arq.writelines('\n')

    def mostrar_clientes(self):
        x=ClienteDAO.ler()

        if len(x)==0:
            print('Não há clientes cadastrados')
        else:
            print('-'*18)
            print('LISTA DE CLIENTES')
            print('-'*18)

            for i in x:
                print(f'- Cliente: {i.nome.capitalize()} | Telefone: {i.telefone} | CPF: {i.cpf} | Email: {i.email} | Endereço: {i.endereco}')

class FuncionarioController:

    def cadastrar_funcionario(self, clt, nome, telefone, cpf, email, endereco):
        x=FuncionarioDAO.ler()

        lista_cpf=list(filter(lambda x: x.cpf==cpf, x))
        lista_clt=list(filter(lambda x: x.clt==clt, x))

        if len(lista_cpf)>0:
            print('Este CPF já existe')
        elif len(lista_clt)>0:
            print('Esse CLT já existe')
        else:
            if len(cpf)==11 and 10<=len(telefone)<=11:
                FuncionarioDAO.salvar(Funcionario(clt,nome,telefone,cpf,email,endereco))
                print('Funcionário cadastrado com sucesso')
            else:
                print('Digite um telefone ou um CPF válido(s)')
        
    def alterar_funcionario(self, nome_alt, clt_novo, nome_novo, cpf_novo, telefone_novo, email_novo, endereco_novo):
        x=FuncionarioDAO.ler()

        ex = list(filter(lambda x: x.nome==nome_alt, x))

        if len(ex)>0:
            est = list(filter(lambda x: x.cpf==cpf_novo, x))
            if len(est)>0:
                print('Este CPF já existe')
            else:
                x = list(map(lambda x: Funcionario(clt_novo, nome_novo, telefone_novo, cpf_novo, email_novo, endereco_novo) if x.nome==nome_alt else x, x))
                print('Funcionário alterado com sucesso')
        else:
            print('Este funcionário não está cadastrado')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(f'{i.nome} ')
                arq.writelines(f'{i.clt} ')
                arq.writelines(f'{i.cpf} ')
                arq.writelines(f'{i.email} ')
                arq.writelines(f'{i.telefone} ')
                arq.writelines(f'{i.endereco} ')
                arq.writelines('\n')

    def remover_funcionario(self, nome):
        x=FuncionarioDAO.ler()

        ex=list(filter(lambda x: x.nome==nome, x))

        if len(ex)>0:
            for i in range(len(x)):
                if x[i].nome==nome:
                    del x[i]
                    print('Funcionário deletado com sucesso')
                    break
        else:
            print('Este funcionário já não existe')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(f'{i.nome} ')
                arq.writelines(f'{i.clt} ')
                arq.writelines(f'{i.cpf} ')
                arq.writelines(f'{i.email} ')
                arq.writelines(f'{i.telefone} ')
                arq.writelines(f'{i.endereco} ')
                arq.writelines('\n')

    def mostrar_funcionarios(self):
        x=FuncionarioDAO.ler()

        if len(x)==0:
            print('Não há funcionários cadastrados')
        else:
            print('-'*18)
            print('LISTA DE FUNCIONÁRIOS')
            print('-'*18)

            for i in x:
                print(f'- Funcionário: {i.nome} | CLT: {i.clt} | CPF: {i.cpf} | Telefone: {i.telefone} | Email: {i.email} | Endereço: {i.endereco}')
