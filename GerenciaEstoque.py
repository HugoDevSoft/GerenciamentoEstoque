# Criando funções para Estruturas de Dados 
produtos = []
categorias = ["Eletrônicos", "Eletrica"]  # Categorias pré-definidas
movimentacoes = []

# Funções para Cadastrar e Consulta um produto
def cadastrar_produto(nome, categoria, quantidade_de_inicial):
    if categoria not in categorias:
        print(f"Erro: Categoria '{categoria}' não encontrada. Escolha uma das categorias existentes.")
        return
    # Objetos do tipo set representado por (pruduto) habilitam operações de conjuntos , como união, interseção, diferença e muitas outras 
    # onde foi passado na (((((CW2 Estruturas de dados em Python – parte II que ajudou de mais nisso ))))) .
    produto = {
        "id": len(produtos),
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade_de_inicial
    }
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso.")

def consultar_produto(nome):
    for produto in produtos:
        if produto["nome"] == nome:
            print(f"Produto encontrado: {produto}")
            return produto
    print(f"Produto '{nome}' não encontrado.")
    return None

# Funções que vai guarda toda movimentação do Estoque como entrada e saida de produto
def movimento_do_estoque(nome, tipo, quantidade):
    produto = consultar_produto(nome)
    if not produto:
        return
    if tipo == "entrada":
        produto["quantidade"] += quantidade
        print(f"Entrada de {quantidade} unidades do produto '{nome}'.")
    elif tipo == "saida":
        if produto["quantidade"] >= quantidade:
            produto["quantidade"] -= quantidade
            print(f"Saída de {quantidade} unidades no produto '{nome}'.")
        else:
            print(f"Erro: Estoque insuficiente para a saída de {quantidade} unidades do produto '{nome}'.")
            return
    else:
        print("Tipo de movimentação inválido.")
        return
    # Registro da movimentação
    movimentacoes.append({
        "produto": nome,
        "tipo": tipo,
        "quantidade": quantidade
    })

# Funções de Relatórios e Consultas
def gerar_relatorio_movimentacoes():
    print("Relatorio de Movimentações:")
    for mov in movimentacoes:
        print(f"Produto: {mov['produto']}, Tipo: {mov['tipo']}, Quantidade: {mov['quantidade']}")

def gerar_relatorio_estoque():
    print("Relatório de Estoque:")
    for produto in produtos:
        print(f"Produto: {produto['nome']}, Categoria: {produto['categoria']}, Quantidade em estoque: {produto['quantidade']}")

""" Aqui eu estou simulando 2 CADASTRO DE PRODUTOS ("Smartphone" "Tomada / 220v") E fazendo a movimentações
 com eles dando ENTRADA E SAIDA para ter um resultado quando for 
 gerar os relarorios"""
 
cadastrar_produto("Smartphone", "Eletrônicos", 10)
cadastrar_produto("Tomada / 220v", "Eletrica", 20)

movimento_do_estoque("Smartphone", "entrada", 5)
movimento_do_estoque("Tomada / 220v", "saida", 10)

gerar_relatorio_movimentacoes()
gerar_relatorio_estoque()

