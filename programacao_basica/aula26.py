'''

Formatação básica de string

s - string
d - int
f - float
.<numero de digítos>f
x ou X- Hexadecimal
(caractere) (><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal + - ou  -
Conversion flags - !r !s !a
'''
variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}') # padding esquerdo
print(f'{variavel: <10}.') # padding direito
print(f'{variavel: ^10}.') # padding centro

print(f'{1000.4444444444554415:.1f}')

print(f'O Hexadecimal de {1500} é {1500:08x}') # x ou X