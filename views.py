import os, controller, time

def criar_arquivos(*nomes):
    for i in nomes:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')

def limpar():
    os.system('cls') or None

def cabecalho(num):
    if num==1:
        res='CATEGORIAS'
    elif num==2:
        res='ESTOQUE'
    elif num==3:
        res='FORNECEDORES'
    elif num==4:
        res='CLIENTES'
    elif num==5:
        res='FUNCIONÁRIOS'
    elif num==6:
        res='VENDAS'

    print('-'*20)
    print(f'OPÇÕES PARA {res}')
    print('-'*20)

criar_arquivos('categorias.txt', 'clientes.txt', 'estoque.txt', 'fornecedores.txt', 'funcionarios.txt', 'vendas.txt')

if __name__ == "__main__": # Se eu executar este arquivo através dele mesmo
    while True:
        print('-'*18)
        print('GESTÃO PARA MERCEARIA')
        print('-'*18)
        local=int(input('Digite 1 para acessar [Categorias]\n'
        'Digite 2 para acessar [Estoque]\n'
        'Digite 3 para acessar [Fornecedores]\n'
        'Digite 4 para acessar [Clientes]\n'
        'Digite 5 para acessar [Funcionários]\n'
        'Digite 6 para acessar [Vendas]\n'
        'Digite 7 para ver os produtos mais vendidos\n'
        'Digite 8 para sair\n'
        'Qual a sua opção:? '))
        limpar()
        if local==1:
            cat=controller.CategoriaController()
            while True:
                cabecalho(local)
                decisao=int(input('Digite 1 para cadastrar uma categoria\n'
                'Digite 2 para remover uma categoria\n'
                'Digite 3 para alterar uma categoria\n'
                'Digite 4 para mostrar as categorias cadastradas\n'
                'Digite 5 para sair\n'
                'Qual a sua opção? '))
                limpar()
                if decisao==1:
                    categoria=input('Digite a categoria que deseja cadastrar: ').replace(' ', '')
                    cat.cadastro_categoria(categoria)
                    print()
                elif decisao==2:
                    cat.mostrar_categoria()
                    print()
                    categoria=input('Digite a categoria que deseja remover: ').replace(' ', '')
                    cat.remover_categoria(categoria)
                    print()
                elif decisao==3:
                    cat.mostrar_categoria()
                    print()
                    categoria = input('Digite a categoria que deseja alterar: ').replace(' ', '')
                    novacat= input('Digite a categoria para a qual deseja alterar: ').replace(' ', '')
                    cat.alterar_categoria(categoria, novacat)
                    print()
                elif decisao==4:
                    cat.mostrar_categoria()
                    print()
                elif decisao==5:
                    break
                else:
                    print('Digite um valor válido')
                    print()
        elif local==2:
            est=controller.EstoqueController()
            while True:
                cabecalho(local)
                decisao=int(input('Digite 1 para cadastrar um produto\n'
                'Digite 2 para remover um produto\n'
                'Digite 3 para alterar um produto\n'
                'Digite 4 para mostrar os produtos do estoque\n'
                'Digite 5 para sair\n'
                'Qual a sua opção? '))
                limpar()
                if decisao==1:
                    nome=input('Digite o nome do produto que deseja cadastrar: ').replace(' ', '')
                    preco=float(input('Digite o preço do produto que deseja cadastrar: R$'))
                    categoria=input('Digite a categoria do produto que deseja cadastrar: ').replace(' ', '')
                    quantidade=int(input('Digite a quantidade do produto que deseja cadastrar: '))
                    est.cadastrar_produto(nome, preco, categoria, quantidade)
                    print()
                elif decisao==2:
                    est.mostrar_estoque()
                    nome=input('Digite o nome do produto que deseja remover: ').replace(' ', '')
                    est.remover_produto(nome)
                    print()
                elif decisao==3:
                    est.mostrar_estoque()
                    nome=input('Digite o nome do produto que deseja alterar: ').replace(' ', '')
                    novo_nome=input('Digite o nome para o qual deseja alterar o produto: ').replace(' ', '')
                    novo_preco=float(input('Digite o novo preço para o produto: R$'))
                    nova_cat=input('Digite a nova categoria do produto: ').replace(' ', '')
                    nova_q=int(input('Digite a nova quantidade do produto: '))
                    est.alterar_produto(nome, novo_nome, novo_preco, nova_cat, nova_q) 
                    print()   
                elif decisao==4:
                    est.mostrar_estoque()
                    print()
                elif decisao==5:
                    break
                else:
                    print('Digite um valor válido!')
                    print()
        elif local==3:
            f=controller.FornecedorController()
            while True:
                cabecalho(local)
                decisao=int(input('Digite 1 para cadastrar um fornecedor\n'
                'Digite 2 para remover um fornecedor\n'
                'Digite 3 para alterar um fornecedor\n'
                'Digite 4 para mostrar os fornecedores cadastrados\n'
                'Digite 5 para sair\n'
                'Qual a sua opção? '))
                limpar()
                if decisao==1:
                    nome=input('Digite o nome do fornecedor que deseja cadastrar: ').replace(' ', '')
                    categoria=input('Digite a categoria de produtos que ele fornece: ').replace(' ', '')
                    telefone=input('Digite o telefone do fornecedor (somente números): ').replace(' ', '')
                    cnpj=input('Digite o CNPJ do fornecedor (somente números): ').replace(' ', '')
                    f.cadastrar_fornecedor(nome, telefone, cnpj, categoria)
                    print()
                elif decisao==2:
                    f.mostrar_fornecedores()
                    nome=input('Digite o nome do fornecedor que deseja remover: ')
                    f.remover_fornecedor(nome)
                    print()
                elif decisao==3:
                    f.mostrar_fornecedores()
                    nome=input('Digite o nome do fornecedor que deseja alterar: ').replace(' ', '')
                    novo_nome=input('Digite o nome para o qual deseja alterar o fornecedor: ').replace(' ', '')
                    novo_tel=input('Digite o novo telefone do fornecedor (somente números): ').replace(' ', '')
                    novo_cnpj=input('Digite o novo CNPJ do fornecedor (somente números): ').replace(' ', '')
                    nova_cat=input('Digite a nova categoria de produtos que ele fornece: ').replace(' ', '')
                    f.alterar_fornecedor(nome, novo_nome, novo_cnpj, novo_tel, nova_cat)
                    print()
                elif decisao==4:
                    f.mostrar_fornecedores()
                    print()
                elif decisao==5:
                    break
                else:
                    print('Digite um valor válido!')
                    print()
        elif local==4:
            cl=controller.ClienteController()
            while True:
                cabecalho(local)
                decisao=int(input('Digite 1 para cadastrar um cliente\n'
                'Digite 2 para remover um cliente\n'
                'Digite 3 para alterar um cliente\n'
                'Digite 4 para mostrar os clientes cadastrados\n'
                'Digite 5 para sair\n'
                'Qual a sua opção? '))
                limpar()
                if decisao==1:
                    nome=input('Digite o nome do cliente que deseja cadastrar: ').replace(' ', '')
                    telefone=input('Digite o telefone do cliente (somente números): ').replace(' ', '')
                    cpf=input('Digite o CPF do cliente: ').replace(' ', '')
                    email=input('Digte o email do cliente: ').replace(' ', '')
                    endereco=input('Digite o endereço do cliente: ').replace(' ', '')
                    cl.cadastrar_cliente(nome, telefone,cpf, email, endereco)
                    print()
                elif decisao==2:
                    cl.mostrar_clientes()
                    nome=input('Digite o nome do cliente que deseja remover: ')
                    cl.remover_cliente(nome)
                    print()
                elif decisao==3:
                    cl.mostrar_clientes()
                    nome=input('Digite o nome do cliente que deseja alterar: ').replace(' ', '')
                    novo_nome=input('Digite o novo nome desse cliente: ').replace(' ', '')
                    novo_tel=input('Digite o novo telefone desse cliente (somente números): ').replace(' ', '')
                    novo_cpf=input('Digite o novo CPF desse cliente: ').replace(' ', '')
                    novo_email=input('Digite o novo email desse cliente: ').replace(' ', '')
                    novo_end=input('Digite o novo endereço desse cliente: ').replace(' ', '')
                    cl.alterar_cliente(nome, novo_nome, novo_cpf, novo_tel, novo_email, novo_end)
                    print()
                elif decisao==4:
                    cl.mostrar_clientes()
                    print()
                elif decisao==5:
                    break
                else:
                    print('Digite um valor válido!')
                    print()
        elif local==5:
            func=controller.FuncionarioController()
            while True:
                cabecalho(local)
                decisao=int(input('Digite 1 para cadastrar um funcionário\n'
                'Digite 2 para remover um funcionário\n'
                'Digite 3 para alterar um funcionário\n'
                'Digite 4 para mostrar os funcionários cadastrados\n'
                'Digite 5 para sair\n'
                'Qual a sua opção? '))
                limpar()
                if decisao==1:
                    nome=input('Digite o nome do funcionário que deseja cadastrar: ').replace(' ', '')
                    clt=input('Digite o CLT do funcionário que deseja cadastrar (somente números): ').replace(' ', '')
                    telefone=input('Digite o telefone do funcionário que deseja cadastrar (somente números): ').replace(' ', '')
                    cpf=input('Digite o CPF do funcionário que deseja cadastrar (somente números): ').replace(' ', '')
                    email=input('Digite o email do funcionário que deseja cadastrar: ').replace(' ', '')
                    endereco=input('Digite o endereço do funcionário que deseja cadastrar: ').replace(' ', '')
                    func.cadastrar_funcionario(clt, nome, telefone, cpf, email, endereco)
                    print()
                elif decisao==2:
                    func.mostrar_funcionarios()
                    nome=input('Digite o nome do funcionário que deseja remover: ').replace(' ', '')
                    func.remover_funcionario(nome)
                    print()
                elif decisao==3:
                    func.mostrar_funcionarios()
                    nome=input('Digite o nome do funcionário que deseja alterar: ').replace(' ', '')
                    novo_nome=input('Digite o novo nome do funcionário: ').replace(' ', '')
                    novo_clt=input('Digite o novo CLT do funcionário (somente números): ').replace(' ', '')
                    novo_cpf=input('Digite o novo CPF do funcionário (somente números): ').replace(' ', '')
                    novo_telefone=input('Digite o novo telefone do funcionário (somente números): ').replace(' ', '')
                    novo_email=input('Digite o novo email do funcionário: ').replace(' ', '')
                    novo_endereco=input('Digite o novo endereço do funcionário: ').replace(' ', '')
                    func.alterar_funcionario(nome, novo_clt, novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco)
                    print()
                elif decisao==4:
                    func.mostrar_funcionarios()
                    print()
                elif decisao==5:
                    break
                else:
                    print('Digite um valor válido!')
                    print()
        elif local==6:
            ve=controller.VendaController()
            while True:
                cabecalho(local)
                decisao=int(input('Digite 1 para cadastrar uma venda\n'
                'Digite 2 para mostrar vendas\n'
                'Digite 3 para sair\n'
                'Qual a sua opção? '))
                limpar()
                if decisao==1:
                    nome=input('Digite o nome do produto que deseja vender: ').replace(' ', '')
                    vendedor=input('Digite o nome do vendedor que realizou a venda: ').replace(' ', '')
                    comprador=input('Digite o nome do cliente que comprou: ').replace(' ', '')
                    quant=int(input('Digite a quantidade vendida: '))
                    ve.cadastrar_venda(nome, vendedor, comprador, quant)
                    print()
                elif decisao==2:
                    inicio=input('Digite a data de início do período de vendas que deseja ver [dd/mm/aa]: ')
                    fim=input('Digite a data de fim do período do vendas que deseja ver [dd/mm/aa]: ')
                    ve.mostrar_vendas(inicio, fim)
                    print()
                elif decisao==3:
                    break
                else:
                    print('Digite um valor válido!')
                    print()
        elif local==7:
            r=controller.VendaController()
            r.relatorio_produtos()
        elif local==8:
            break
        else:
            print('Digite um número válido!')
print('OBRIGADO POR USAR O PROGRAMA!')
time.sleep(1.6)
limpar()