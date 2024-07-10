def listar_tarefas(lista=None):
    if lista is None:
        lista = []
    if len(lista) == 0:
        print('Lista vazia.')
        return
    
    print('\nTAREFAS: ')
    for tarefa in lista:
        print(tarefa)


def adicionar_tarefa(tarefa, lista=None):
    if lista is None:
        lista = []
    lista.append(tarefa)


def desfazer_tarefa(lista_tarefa=None, lista_historico=None):
    if lista_historico is None:
        lista_historico = []
    if lista_tarefa is None:
        lista_tarefa = []
    
    if len(lista_tarefa) == 0:
        print('Nada a desfazer')
        return True
    
    lista_historico.append(lista_de_tarefas.pop())



def refazer_tarefa(lista_tarefa=None, lista_historico=None):
    if lista_historico is None:
        lista_historico = []
    if lista_tarefa is None:
        lista_tarefa = []

    if len(lista_historico) == 0:
        print('Nada a refazer.')
        return True
    
    lista_tarefa.append(lista_historico.pop())


lista_de_tarefas = []
lista_historico_de_tarefas = []

while True:

    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ').lower()

    if tarefa == 'listar':
        listar_tarefas(lista_de_tarefas)

    elif tarefa == 'desfazer':
        desfazer_tarefa(lista_de_tarefas, lista_historico_de_tarefas)

    elif tarefa == 'refazer':
        refazer_tarefa(lista_de_tarefas, lista_historico_de_tarefas)

    else:
        adicionar_tarefa(tarefa.capitalize(), lista_de_tarefas)
        listar_tarefas(lista_de_tarefas)

    print()


