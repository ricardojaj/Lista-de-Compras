opcao = 0
listaCompra = ['Banana', 'Biscoito', 'Laranja', 'Arroz']

while opcao != 5:

    print('=== Lista de Compras ===')
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Exibir lista de compras')
    print('4. Salvar e abrir lista em arquivo txt')
    print('5. Sair')

    try:
        opcao = int(input("Digite uma opcao: "))

        if opcao == 1:           
            continua = 'SIM'

            while continua == 'SIM':
                nomeProdutoAdc = input('Digite o nome do produto: ')
                listaCompra.append(nomeProdutoAdc)
                
                continua = input("Deseja inserir mais um produto: (SIM / NAO)").upper()
        elif opcao == 2:
            continua = 'SIM' 

            while continua == 'SIM':
                nomeProdutoRemover = input('Digite o produto que deseja remover: ')
                if nomeProdutoRemover in listaCompra:
                    listaCompra.remove(nomeProdutoRemover)
                else:
                    print("Esse produto nao existe na lista ou ja foi removido!")
                
                continua = input("Deseja remover mais um produto: (SIM / NAO)").upper
        elif opcao == 3:
            if listaCompra:
                print('==== Lista de Compras ====')
                cont = 1
                for i in listaCompra:
                    print(f'{cont}. {i} ')
                    cont += 1
            else:
                print("A lista esta vazia!")
        elif opcao == 4:
            if listaCompra:
                with open("lista_compras.txt", "w") as arquivo:
                    cont = 1
                    for i in listaCompra:      
                        arquivo.write(f'{cont}. {i}' + "\n")
                        cont += 1

                with open("lista_compras.txt", "r") as arquivo:
                    conteudo = arquivo.readlines()
                print("Lista salva no arquivo 'lista_compras.txt'.")
            else:
                print("A lista esta vazia e nao pode ser salva!")
        elif opcao == 5:
            print("Programa encerrado. Até logo!")
        
        else:
            print("Opção inválida! Escolha entre 1 e 5.")
    except ValueError:
        print("Opção digitada é invalida!")
        
