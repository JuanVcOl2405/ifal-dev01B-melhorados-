def main():
    tamanho = int(input("Qual o tamnho do bloco: "))
    quadrado(tamanho)

def quadrado(tamanho):
    quadrado = ("+" * tamanho)
    print (f"{quadrado}\n" * tamanho)

main()