#Bruna Zakaib Pessoa; RA: 10417079; Turma 01J.
lista_registros = []
chaves = ["id", "title", "price", "listPrice", "categoryName", "isBestSeller", "boughtInLastMonth"]
#função que carrega o arquivo, lê linha por linha, 
#separa os dados como elementos de uma lista pela vírgula
#coloca a chave na posição "i" para o dado naquela mesma posição
#torna cada linha do arquivo em um dicionario e cada dicionario será armazenado numa lista
def carregar(endereco_arquivo):
    with open(endereco_arquivo, "r") as arquivo:
        for linha in arquivo:
            dicionario = {}
            # remove o caractere de quebra de linha '\n' da linha lida
            linha = linha.strip()
            dados = linha.split(',')
            for i in range(len(chaves)):
                dicionario[chaves[i]] = dados[i]
            lista_registros.append(dicionario)  
    return lista_registros

#inserindo o arquivo emack.csv na função:
nome_arquivo = "emack.csv"
carregar(nome_arquivo)

#para corrigir erro de leitura do arquivo:
for registro in lista_registros:
    if registro["categoryName"] == "EletrÃ´nicos":
        registro["categoryName"] = "Eletrônicos"
        
#para acontagem de produtos por categoria, a função entra em um loop 
#para ler linha por linha e identificar qual a categoria e somá-la de acordo com a sua variável
def cont_prod_cat():
    livros = 0
    casa = 0 
    moda = 0
    eletro = 0
    esporte = 0
    for registro in lista_registros:
        categoria = registro["categoryName"].lower()
        if categoria == "livros":
            livros += 1
        elif categoria == "casa":
            casa += 1
        elif categoria == "moda":
            moda += 1
        elif categoria == "esportes":
            esporte += 1
        elif categoria == "eletrônicos":  
            eletro += 1
        else:
            continue
    resultado_contagem = [livros, casa, moda, eletro, esporte]
    return resultado_contagem

resultado_contagem = cont_prod_cat()

#função que calcula o percentual dos produtos por categoria:
def perc_prod_cat():
    percentuais = []
    total_produtos = sum(resultado_contagem)
    
    #calculando a porcentagem e adicionando os resultados à lista 'percentuais'
    for quantidade in resultado_contagem:
        percentual = (quantidade / total_produtos) * 100
        percentuais.append(percentual)
    
    #gerando a mensagem para o usuário:
    categorias = ["Livros", "Casa", "Moda", "Eletrônicos", "Esportes"]
    for i in range(len(categorias)):
        categoria = categorias[i]
        percentual = percentuais[i]
        print(f"{categoria}: {percentual:.2f}%")


#para avaliar a proporção de best-sellers por categoria, é necessária uma função auxiliar
#que irá fazer a contagem de best-sellers por categoria
def aux_cont_bestsel():
    bestseller_cat = [0, 0, 0, 0, 0]  # Lista para armazenar a quantidade de best-sellers por categoria
    for registro in lista_registros:
        categoria = registro["categoryName"].lower()
        if registro["isBestSeller"].lower() == "true":
            if categoria == "livros":
                bestseller_cat[0] += 1
            elif categoria == "casa":
                bestseller_cat[1] += 1
            elif categoria == "moda":
                bestseller_cat[2] += 1
            elif categoria == "eletrônicos":
                bestseller_cat[3] += 1
            elif categoria == "esportes":
                bestseller_cat[4] += 1
    return bestseller_cat

lista_aux = aux_cont_bestsel()

#na função principal para o cálculo da proporção, 
#é necessário dividir a qtd de bets-sellers pelo total de produtos por categoria:
def proporcao_bestsell():
    resolucao = []
    for i in range(len(resultado_contagem)):
        proporcao = (lista_aux[i]/resultado_contagem[i])
        resolucao.append(proporcao)
    return resolucao

resolucao = proporcao_bestsell()
def identificar_10_produtos_mais_caros_e_baratos():
    # Lista para armazenar todos os preços
    precos = []

    # Itera sobre os registros para extrair os preços
    for registro in lista_registros:
        # Verifica se o valor do preço pode ser convertido em float
        try:
            preco = float(registro["price"])
            precos.append(preco)
        except ValueError:
            # Ignora registros sem preço válido
            continue
    
    #classifica os preços em ordem decrescente
    precos.sort(reverse=True)
    
    #seleciona os 10 produtos mais caros
    produtos_mais_caros = precos[:10]
    #seleciona os 10 produtos mais baratos
    produtos_mais_baratos = precos[-10:]
    
    #lista para armazenar os nomes dos produtos mais caros
    nomes_produtos_mais_caros = []
    #lista para armazenar os nomes dos produtos mais baratos
    nomes_produtos_mais_baratos = []

    #itera sobre os registros para identificar os produtos mais caros e mais baratos
    for registro in lista_registros:
        try:
            preco = float(registro["price"])
            precos.append(preco)
        except ValueError:
            # Ignora registros sem preço válido
            continue
        if preco in produtos_mais_caros:
            nomes_produtos_mais_caros.append(f"{registro['title']}: R${preco:.2f}")
        elif preco in produtos_mais_baratos:
            nomes_produtos_mais_baratos.append(f"{registro['title']}: R${preco:.2f}")
    
    return nomes_produtos_mais_caros, nomes_produtos_mais_baratos

#chama a função para identificar os 10 produtos mais caros e os 10 mais baratos
produtos_mais_caros, produtos_mais_baratos = identificar_10_produtos_mais_caros_e_baratos()

#função para listar os produtos por categoria escolhida pelo usuário
def listar_prod_cat(categoria_usuario):
    lista_prod_cat = []
    categoria_usuario = categoria_usuario.lower()
    for registro in lista_registros:
        categoria_registro = registro["categoryName"].lower()  # Convertendo a categoria do registro para minúsculas
        if categoria_usuario == categoria_registro:
            lista_prod_cat.append(registro)      
    return lista_prod_cat

def carregar_dados():
    dataset = []                    #lista que irá receber todos os dados do arquivo
    file = open('emack.csv', 'r')
    linhas = file.readlines()
    cabecalho = linhas[0].strip().split(',')
    for linha in linhas[1:]:
        valores = linha.strip().split(',')
        produto = {}
        for i in range(len(cabecalho)):
            produto[cabecalho[i]] = valores[i]  #dicionário com a chave id e conteúdo c os outros valores
        dataset.append(produto)
    print (dataset)
    return dataset

def listarCategorias(dados):
    categorias = []
    for produto in dados:
        if produto["categoryName"] not in categorias:
            categorias.append(produto["categoryName"])
    return categorias

def listarProdutosCategoria(dados, categoria):
    produtos = []
    for produto in dados:
        if produto["categoryName"] == categoria:
            produtos.append(produto)
    return produtos

def ultVendaMes(produto):
    return int(produto["boughtInLastMonth"])

def gerarHtml_BestSellers(dados):
    relatorio = "<html><head><title>Relatório Top 10 Best Sellers por Categoria</title></head><body>"
    categorias = listarCategorias(dados)
    for categoria in categorias:
        relatorio += f"<h1>{categoria}</h1>"
        produtos = listarProdutosCategoria(dados, categoria)
        produtos_ordenados = sorted(produtos, key=ultVendaMes)
        relatorio += "<ol>"
        for produto in produtos_ordenados[:10]:
            relatorio += f"<li>{produto['title']} - Quantidade Vendida: {produto['boughtInLastMonth']}</li>"
        relatorio += "</ol>"
    relatorio += "</body></html>"
    with open("relatorio_top_10_best_sellers.html", "w") as file:
        file.write(relatorio)


#main:
while True:
    print("Menu:")
    print("1) Contagem de produtos por categoria")
    print("2) Percentual de produtos por categoria")
    print("3) Proporção de best-sellers por categoria")
    print("4) Os 10 produtos mais caros e mais baratos no geral")
    print("5) Listar os produtos por categoria escolhida")
    print("6) Relatório que demonstra os Top 10 best-sellers por categoria")
    print("7) Sair")
    entrada_usuario = int(input("Digite a opção escolhida: "))
    if entrada_usuario > 7 and entrada_usuario < 1:
        print("Número inválido!")
    else:
        if entrada_usuario == 1:
            cont_prod_cat()
            print("Livros:", resultado_contagem[0])
            print("Casa:", resultado_contagem[1])
            print("Moda:", resultado_contagem[2])
            print("Eletrônicos:", resultado_contagem[3])
            print("Esportes:", resultado_contagem[4])

        elif entrada_usuario == 2:
            perc_prod_cat()

        elif entrada_usuario == 3:
            proporcao_bestsell()
            print(f"Livros: {resolucao[0]:.2f}")
            print(f"Casa: {resolucao[1]:.2f}")
            print(f"Moda: {resolucao[2]:.2f}")
            print(f"Eletrônicos: {resolucao[3]:.2f}")
            print(f"Esportes: {resolucao[4]:.2f}")

        elif entrada_usuario == 4:
            identificar_10_produtos_mais_caros_e_baratos()
            print("Os 10 produtos mais caros são:")
            for produto in produtos_mais_caros:
                print(produto)

            print("\nOs 10 produtos mais baratos são:")
            for produto in produtos_mais_baratos:
                print(produto)
        
        elif entrada_usuario == 5:
            categoria_usuario = input("Escolha a categoria: ")
            lista = listar_prod_cat(categoria_usuario)
            print(lista)
        
        elif entrada_usuario == 6:
            dados = carregar_dados()
            gerarHtml_BestSellers(dados)
            print("Relatório gerado")
            
        elif entrada_usuario == 7:
            break
        
