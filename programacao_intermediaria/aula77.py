
questions_list = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',
    },
]

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
    
