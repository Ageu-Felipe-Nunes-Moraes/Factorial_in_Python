
class CalculaFatorial:

    def __init__(self):
        print("========================")
        print("====CALCULA FATORIAL====")
        print("========================")
        self.fatorial = 0
        self.resultado = 1
    
    def getValor(self):

        self.fatorial = int(input("Digite um valor para saber o fatorial do mesmo: "))
        self.resultado = 1

    def verificaCondicoes(self):
        if self.fatorial < 0:
            print("Valor negativo, portanto resultado inválido.")
        else:
            for i in range(1, self.fatorial +1):
                self.resultado *= i
            self.imprimeResultado()
            

    def imprimeResultado(self):
        print(f"O fatorial do seu número é: {self.resultado}")

calculadora = CalculaFatorial()
calculadora.getValor()
calculadora.verificaCondicoes()


#Forma simplificada de calcular fatorial
"""def calcula_fatorial(numero):
    fatorial = 1
    if numero >= 0:
        for i in range(1, numero+1):
            fatorial *= i
        print(f"O fatorial é: {fatorial}")
    else:
        print("Valor inválido")

n = int(input("Digite um número: "))
calcula_fatorial(n)"""

