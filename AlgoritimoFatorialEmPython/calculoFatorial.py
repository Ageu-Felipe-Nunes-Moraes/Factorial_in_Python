
class CalculaFatorial:

    def __init__(self):
        print("========================")
        print("====CALCULA FATORIAL====")
        print("========================")
        self.fatorial = 0
        self.resultado = 1
    
    def get_valor(self):

        self.fatorial = int(input("Digite um valor para saber o fatorial do mesmo: "))
        self.resultado = 1

    def verifica_condicoes(self):
        if self.fatorial < 0:
            print("Valor negativo, portanto resultado inválido.")
        else:
            for i in range(1, self.fatorial +1):
                self.resultado *= i
            self.imprime_resultado()
            

    def imprime_resultado(self):
        print(f"O fatorial do seu número é: {self.resultado}")

calculadora = CalculaFatorial()
calculadora.get_valor()
calculadora.verifica_condicoes()


#Forma simplificada de calcular fatorial
#def calcula_fatorial(numero):
#    fatorial = 1
#    if numero >= 0:
#        for i in range(1, numero+1):
#            fatorial *= i
#        print(f"O fatorial é: {fatorial}")
#    else:
#        print("Valor inválido")

#n = int(input("Digite um número: "))
#calcula_fatorial(n)
