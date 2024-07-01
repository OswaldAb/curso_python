import emoji
questions = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opcoes': ['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opcoes': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opcoes': ['4','5','2','1'],
        'Resposta': '5',
    },
]

qtd_hits = 0

for question in questions:
    print(f'Pergunta: {question['Pergunta']}')
    print()

    options = question['Opcoes']
    for i, option in enumerate(options):
        print(f'{i}) {option}')
    print()

    user_response = input('Escolha uma opção: ')

    got_it_right = False
    user_response_int = None
    qtd_options = len(options)
    
    try:
        user_response_int = int(user_response)  

    except ValueError:
        user_response_int = None

    if user_response_int is not None:
        if 0 <= user_response_int <= qtd_options:
            if options[user_response_int] == question['Resposta']:
                got_it_right = True
    
    print()
    if got_it_right:
        qtd_hits += 1
        print(emoji.emojize('Acertou :thumbs_up:'))
    
    else:
        print(emoji.emojize('Errou :cross_mark:'))
    print()

print('Você acertou', qtd_hits,\
       'de', len(questions), 'perguntas')



   
'''
for question_dict in questions_list:

    question_key, options_key, answer_key = question_dict

    print(f'{question_key}: {question_dict[question_key]}\n')
    print(f'{options_key}:')

    options_list = question_dict[options_key]

    for option in enumerate(options_list):
        alternative, answer = option
        print(f'{alternative}) {answer}')

    user_response = input('Escolha uma opção: ')

    got_it_right = options_list[int(user_response)] == question_dict[answer_key]

    if got_it_right:
        print('Acertou')
    else:
        print('Errou')
'''