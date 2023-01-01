def gather_data():
    n1 = int(input('Primeiro valor:'))
    n2 = int(input('Segundo valor:'))
    return n1, n2

def print_message(n1,n2):
    print(f'Os valores {n1} e {n2} somados dao {n1+n2}')
    return None

def main():
    n1,n2 = gather_data()

    print_message(n1, n2)

    return None


if __name__ == '__main__':
    main()