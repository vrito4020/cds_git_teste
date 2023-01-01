import teste2

def get_operation():
    op = input('operacao:')
    return op

def gather_data():
    n1 = input('Primeiro valor:')
    n2 = input('Segundo valor:')
    op = get_operation()
    return n1, n2, op

def maine(n1, n2):
    print(n1*n2)
    return None

if __name__ == '__main__':
    gather_data()
    maine()