import os

def check_if_is_a_list(lista):
    if lista is None:
        lista = []
    return lista
    

def check_if_list_is_empty(lista):
    lista = [] if lista is None else lista
    if len(lista) == 0:
        return True
    return False


def add_task(tarefa, lista=None):
    lista = check_if_is_a_list(lista)
    lista.append(tarefa)


def undo_task(lista_tarefa, lista_hist):
    lista_tarefa = check_if_is_a_list(lista_tarefa)
    lista_hist = check_if_is_a_list(lista_hist)

    if check_if_list_is_empty(lista_tarefa):
        print('Nada a desfazer.\n')

    else:
        lista_hist.append(lista_tarefa.pop())


def redo_task(lista_tarefa, lista_hist):
    lista_tarefa = check_if_is_a_list(lista_tarefa)
    lista_hist = check_if_is_a_list(lista_hist)

    if check_if_list_is_empty(lista_hist):
        print('Nada a refazer.\n')
    
    else:
        lista_tarefa.append(lista_hist.pop())


def show_list(lista):
    check_if_is_a_list(lista)
    if check_if_list_is_empty(lista):
        print('Nada a mostrar\n')
    
    else:
        for tarefa in lista:
            print(tarefa)


def limpar_terminal():
    os.system('clear')


lista_de_tarefas = []
lista_de_historico = []

while True:

    print('Comandos: listar, desfazer, refazer')
    input_usuario = input('Digite uma tarefa ou comando:')
    input_usuario_lower = input_usuario.lower()

    if input_usuario_lower == 'clear':
        limpar_terminal()


    elif input_usuario == 'desfazer':
        undo_task(lista_de_tarefas, lista_de_historico)
        print()

    elif input_usuario_lower == 'refazer':
        redo_task(lista_de_tarefas, lista_de_historico)
        print()

    elif input_usuario_lower == 'listar':
        print('\nTarefas')
        show_list(lista_de_tarefas)
    
    else:
        print('Tarefas')
        add_task(input_usuario_lower.capitalize(), lista_de_tarefas)
        show_list(lista_de_tarefas)
        print()
