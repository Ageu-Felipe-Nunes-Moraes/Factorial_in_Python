
class CalculaFatorial:

    def __init__(self):
        print("========================")
        print("====CALCULA FATORIAL====")
        print("========================")
        self.fatorial = 0 # Vai receber o número dado pelo usuário
        self.resultado = 1 # Variável contadora que armazenará o resultado
    
    def get_valor(self): # Captura o valor dado pelo usuário

        self.fatorial = int(input("Digite um valor para saber o fatorial do mesmo: "))
        self.resultado = 1

    def verifica_condicoes(self): # Verifica a condição necessária para ser considerado fatorial
        if self.fatorial < 0: # Se um valor negativo for inserido, vai aparecer essa mensagem
            print("Valor negativo, portanto resultado inválido.")
        else: # Se não, o código chama a implementação da lógica e chama o resultado
            # Dentro de um range entre 1 ao valor inserido +1 ele será múltiplicado com a variável "Resultado"
            # EXEMPLO: 5! = 1*1 = 1*2 = 2*3 = 6*4 = 24 * 5 = 120
            for i in range(1, self.fatorial +1):
                self.resultado *= i
            self.imprime_resultado() 
            

    def imprime_resultado(self): # Entrega o resultado
        print(f"O fatorial do seu número é: {self.resultado}")

calculadora = CalculaFatorial() # Objeto 1
calculadora.get_valor() # // Capturando valor do usuário
calculadora.verifica_condicoes() # Verificando se o valor inserido é válido


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
