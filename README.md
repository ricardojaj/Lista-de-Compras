# Lista de Compras

Este projeto é uma aplicação simples de **Lista de Compras** desenvolvida em Python. O objetivo é permitir ao usuário adicionar, remover e exibir itens de uma lista de compras, além de poder salvar e abrir essa lista em um arquivo `.txt`.

## Funcionalidades

- **Adicionar item**: O usuário pode adicionar produtos à lista de compras.
- **Remover item**: O usuário pode remover produtos da lista de compras.
- **Exibir lista de compras**: Exibe todos os produtos atualmente na lista.
- **Abrir lista em arquivo `.txt`**: A lista é salva em um arquivo `.txt` e pode ser aberta para visualização.

## Tecnologias utilizadas

- Python (versão 3.12.2)

## Como usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/ricardojaj/Lista-de-Compras.git
   ```

2. **Execute o script Python:**

   ```bash
   python lista_compras.py
   ```

3. **Interaja com o menu:**
   O programa exibirá um menu com as seguintes opções:

   1. Adicionar item
   2. Remover item
   3. Exibir lista de compras
   4. Salvar e abrir lista em arquivo `.txt`
   5. Sair

   Você pode inserir as opções digitando o número correspondente e seguir as instruções na tela.

## Explicação do Código

### Estrutura Principal

1. **Lista de Compras:**

   - A lista de compras é armazenada em uma lista Python, chamada `listaCompra`.

2. **Menu Interativo:**

   - O programa exibe um menu com opções para o usuário escolher. O menu é implementado usando um loop `while` que continuará até que o usuário escolha a opção de sair (opção 5).

3. **Adicionar Itens:**

   - Quando a opção 1 é selecionada, o programa solicita ao usuário o nome de um produto e o adiciona à lista. O usuário pode continuar adicionando produtos até escolher a opção "NAO".

4. **Remover Itens:**

   - Quando a opção 2 é selecionada, o programa pede o nome de um produto a ser removido. Se o produto estiver na lista, ele é removido. Caso contrário, o programa informa que o produto não foi encontrado.

5. **Exibir Lista:**

   - Quando a opção 3 é escolhida, o programa exibe todos os produtos na lista com a numeração correspondente.

6. **Salvar e Abrir Arquivo:**
   - Quando a opção 4 é selecionada, o programa salva a lista de compras em um arquivo `lista_compras.txt`, e também exibe o conteúdo desse arquivo.
