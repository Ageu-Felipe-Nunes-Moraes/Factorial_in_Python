
def calcula_fatorial(numero):
    fatorial = 1
    if numero >= 0:
        for i in range(1, numero+1):
            fatorial *= i
        print(f"O fatorial é: {fatorial}")
    else:
        print("Valor inválido")

n = int(input("Digite um número: "))
calcula_fatorial(n)

