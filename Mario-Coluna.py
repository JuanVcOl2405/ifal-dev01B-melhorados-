def main():
    coluna(quantas())

def coluna(colunas):
    print("#\n"* colunas)

def quantas():
    while True:
        colunas = int(input("Quantas colunas: "))

        if colunas > 0:
            return colunas
main()