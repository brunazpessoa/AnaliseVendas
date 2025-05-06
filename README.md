# 📊 Sistema de Análise de Dados de Vendas — eMACK

Este projeto realiza uma análise de dados de vendas da empresa eMACK, um dos maiores varejistas online do Brasil. Com base em um dataset contendo mais de 500 produtos vendidos ao longo de 2023, o sistema implementa algoritmos simples (sem bibliotecas externas) para explorar e extrair insights relevantes.

---

## 🗃️ Descrição do Dataset

O arquivo utilizado contém os seguintes campos para cada produto:

- `id`: Identificador único do produto
- `title`: Nome ou título do produto
- `price`: Preço atual do produto
- `listPrice`: Preço original do produto antes de descontos
- `categoryName`: Categoria do produto
- `isBestSeller`: Indica se o produto é um best-seller
- `boughtInLastMonth`: Quantidade vendida no último mês

---

## 🧠 Funcionalidades

### 1. Carregamento dos Dados
- Leitura do dataset em memória usando estruturas básicas como listas e dicionários.
- Sem o uso de bibliotecas como `pandas` ou similares.

### 2. Análises Disponíveis

#### a) Contagem de Produtos por Categoria
- Exibe quantos produtos existem em cada categoria.

#### b) Percentual de Produtos por Categoria
- Calcula a representatividade percentual de cada categoria no total de produtos.

#### c) Proporção de Best-Sellers por Categoria
- Mostra a porcentagem de produtos marcados como *best-sellers* dentro de cada categoria.

#### d) Top 10 Produtos Mais Caros e Mais Baratos
- Lista os 10 produtos com os preços mais altos e mais baixos, considerando todos do dataset.

#### e) Listagem por Categoria
- Permite que o usuário escolha uma categoria e visualize todos os produtos correspondentes.

#### f) Relatório HTML
- Geração de um relatório em HTML com os Top 10 *best-sellers* de cada categoria.
- Cada item exibe o título do produto e a quantidade vendida no último mês.

---

## 🛠 Requisitos

- Python 3.x
- Nenhuma biblioteca externa necessária (sem `pandas`, `matplotlib`, etc.)

---
