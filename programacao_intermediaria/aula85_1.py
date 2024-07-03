nomes = ['Luiz', 'Maria', 'Helena', 'Felipe']

novos_nomes = [
    nome[0: -1].lower() + nome[-1].upper() 
    for nome in nomes]

print(novos_nomes)