import os
def list_talks(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')

def undo_task(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para defazer')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def redo_task(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para resfazer')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def add_task(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()

    if not tarefa:
        print('Você não digitu uma tarefa')
        return
    tarefas.append(tarefa)

def clear():
    os.system('clear')


task = []
task_redo = []

while True:

    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ').lower()

    comandos = {
        'listar': lambda: list_talks(task),        
        'desfazer': lambda: undo_task(task, task_redo),        
        'refazer': lambda: redo_task(task, task_redo),        
        # 'clear': clear(),     
        'adicionar': lambda: add_task(tarefa, task),        
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None \
    else comandos['adicionar']
    comando()

    # if tarefa == 'listar':
    #     list_talks(task)
    #     continue

    # elif tarefa == 'desfazer':
    #     undo_task(task, task_redo)
    #     continue

    # elif tarefa == 'refazer':
    #     redo_task(task, task_redo)
    #     continue

    # else:
    #    add_task(tarefa, task)

