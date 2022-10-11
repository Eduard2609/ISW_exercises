# take an integer n and print on different colums in decimial, octal, hexadecimal and binary
def print_formatted(number):

   # print("Decimal Octal Hexadecimal Binary")
    w = len("{0:b}".format(number))
    for i in range(1, number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print_formatted(n)
