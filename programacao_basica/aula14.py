
a = 'A'
b = 'B'
c = 1.1

string = 'a={} b={} c={:.2f}' # as {} também podem receber os indices ex {0} {1}

formato = string.format(a, b, c)

print(formato)