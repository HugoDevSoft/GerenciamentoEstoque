from datetime import datetime

class Produto:
    def __init__(self, id, nome, quantidade_estoque=0):
        self.id = id
        self.nome = nome
        self.quantidade_estoque = quantidade_estoque

class Movimentacao:
    def __init__(self, produto, tipo, quantidade):
        self.produto = produto
        self.tipo = tipo  # 'entrada' ou 'saida'
        self.quantidade = quantidade
        self.data = datetime.now().strftime('%d/%m/%Y %H:%M')  # Pegando a data e hora atual da movimentação

# Funções para cadastrar produtos e consultar pelo ID do produto.
produtos = []  # Lista para armazenar os produtos

def cadastrar_produto(id, nome, quantidade_inicial=0): #Aqui a função p/ cadastro de produto
    produto = Produto(id, nome, quantidade_inicial)
    produtos.append(produto)
    return produto

def consultar_produto(id): #Aqui a função p/ consultar o produto
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


# Função para registrar entradas e saídas e de bonus coloquei a def p/ atualizar o estoque.

movimentacoes = []  # Lista para armazenar movimentações

def movimento_no_estoque(produto_id, tipo, quantidade):
    produto = consultar_produto(produto_id)
    if produto is None:
        print("Produto não encontrado ou não existe.")
        return

    if tipo == 'saida' and produto.quantidade_estoque < quantidade:
        print("Estoque insuficiente para saída ou seja acabou tudo na liquidação.")
        return

    produto.quantidade_estoque += quantidade if tipo == 'entrada' else -quantidade
    movimentacoes.append(Movimentacao(produto, tipo, quantidade))  # Registra a movimentação toda que acontece no estoque tanto a entrada e a saida.



# Funções para ver o estoque atual e o histórico de movimentações.

def relatorio_estoque():
    for produto in produtos:
        print(f"{produto.nome}: {produto.quantidade_estoque} unidades deste produto")

def historico_movimentacoes(produto_id):
    produto = consultar_produto(produto_id)
    if produto:
        for mov in movimentacoes:
            if mov.produto.id == produto_id:
                print(f"{mov.data} - {mov.tipo} - {mov.quantidade} unidades deste produto")


# Exemplo de Uso onde eu simulo que estou cadastrando um novo produto colocando o 
# Cadastro de produto novo
cadastrar_produto(1, "Água Mineral", 100)
cadastrar_produto(2, "Suco", 50)

# Movimentações onde eu simulo que dei entrada 20 agua e saida de 10 agua e tambem a entrada de 10 Sucos.
movimento_no_estoque(1, 'entrada', 20)
movimento_no_estoque(1, 'saida', 10)
movimento_no_estoque(2, 'entrada', 10)


# aqui eu estou pedindo que o programa imprimir os relatórios
print("Estoque Atual:")
relatorio_estoque()

print("\nHistórico de Movimentações para Água Mineral:")
historico_movimentacoes(1)
historico_movimentacoes(2)

