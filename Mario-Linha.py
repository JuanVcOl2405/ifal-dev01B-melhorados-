def main():
    linha(comprimento())

def linha(comprido):
    print("-\n"*comprido)

def comprimento():
    while True:
        comprido = input("Qual o comprimento da linha: ")

        if comprido > 0:
            return comprido | comprido
main()