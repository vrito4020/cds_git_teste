def gather_data():
    n1 = input('Primeiro valor:')
    n2 = input('Segundo valor:')
    op = input('operacao:')
    return n1, n2, op

def maine(n1, n2, op):
    print(eval(n1+op+n2))
    return None

if __name__ == '__main__':
    maine()