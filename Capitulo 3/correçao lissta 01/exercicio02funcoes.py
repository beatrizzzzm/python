def do_twice(f, nome):
    f() + nome
    f() + nome

def print_spam(nome):
    print('spam' + nome)

do_twice(print_spam, nome)
