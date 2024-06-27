import os
lista_de_compra = list()

while True:

    
    print('\nSelecione uma opção')
    opcao = input(f'[i]nserir [a]pagar [l]istar: ').lower()

    if bool(opcao) == False:
        print('Você não digitou nada')

    if opcao not in 'ial':
        print('Opção invalida!')
        continue

    # Inserir itns na lista
    if opcao == 'i':
        item = input('item: ')

        if bool(item) != False:
            lista_de_compra.append(item )
        
        else:
            print('Você não digitou nada!\n')
    
    # Apagar os itens da lista

    elif opcao == 'a':
        os.system('clear')
        converteu = None 
        indice_int = 0

        if len(lista_de_compra) == 0:
            print('Nada para apagar!')
            continue

        indice = input('\nInsira o indice do item a ser excluido: ')
       
        if bool(indice) == False:
            print('Você não digitou nada!')
        
        try:
            indice_int = int(indice)
            converteu = True
        except ValueError:
            converteu = None

        if converteu is None:
            print('Digite apenas números inteiros para os indices!')
            continue
     
        try:
            item_excluido = lista_de_compra.pop(indice_int)
            print(f'Item {item_excluido} foi excluido!')

        except IndexError:
            print('Indice inexistente!')
            continue

    # Listar os itns da lista
    elif opcao == 'l':
        os.system('clear')
        if len(lista_de_compra) == 0:
            print('Nada para listar.')
        
        else:
            for indice, item in enumerate(lista_de_compra):
                print(indice, item)

    else:
        print('Opção invalida')