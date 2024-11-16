opcao = 0
listaCompra = ['Banana', 'Pão', 'Laranja']

while opcao != 4:

    print('=== Lista de Compras ===')
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Exibir lista de compras')
    print('4. Sair')

    try:
        opcao = int(input("Digite uma opcao: "))

        if opcao == 1:           
            continua = 'SIM'

            while continua == 'SIM':
                nomeProdutoAdc = input('Digite o nome do produto: ')
                listaCompra.append(nomeProdutoAdc)
                
                continua = input("Deseja inserir mais um produto: (SIM / NAO)")
        elif opcao == 2:
            continua = 'SIM' 

            while continua == 'SIM':
                nomeProdutoRemover = input('Digite o produto que deseja remover: ')
                if nomeProdutoRemover in listaCompra:
                    listaCompra.remove(nomeProdutoRemover)
                else:
                    print("Esse produto nao existe na lista ou ja foi removido!")
                
                continua = input("Deseja remover mais um produto: (SIM / NAO)")
        elif opcao == 3:
            print('==== Lista de Compras ====')
            cont = 1
            for i in listaCompra:
                
                print(f'{cont}. {i} ')
                cont += 1


    except ValueError:
        print("Opção digitada é invalida!")
        


    

    

print(listaCompra)