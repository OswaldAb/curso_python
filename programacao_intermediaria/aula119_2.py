import os
import json

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

def ler(tarefas, caminho_arquivo):
    try:
        dados = []
        with open(caminho_arquivo, 'r', encoding='utf8') as file:
            dados = json.load(file)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as file:
        dados = json.dump(tarefas, file, indent=2, ensure_ascii=False)
    
    return dados


CAMINHO_ARQUIVO = 'aula119.json'
task = ler([], CAMINHO_ARQUIVO)
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
    salvar(task, CAMINHO_ARQUIVO)