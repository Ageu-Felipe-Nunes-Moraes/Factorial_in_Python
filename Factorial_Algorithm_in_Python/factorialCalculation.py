
class FactorialCalculate:

    def __init__(self):
        print("========================")
        print("====CALCULA FATORIAL====")
        print("========================")
        self.factorial = 0 # Will receive a number given by the user
        self.result = 1 # Counter that will store the result
    
    def get_value(self): # To get the value given by the user

        self.factorial = int(input("Digite um valor para saber o fatorial do mesmo: "))
        self.result = 1

    def checks_conditions(self): # Checks the necessary conditions to have a factorial
        if self.factorial < 0: # if a negative value is entered it will show this message
            print("Valor negativo, portanto resultado inválido.")
        else: # Otherwise, the code calls the logic implementation and calls the result
            # In a range of 1 to value entered +1 it will multiply with the "Result" variable 
            # EXEMPLE: 5! = 1*1 = 1*2 = 2*3 = 6*4 = 24 * 5 = 120
            for i in range(1, self.factorial +1):
                self.result *= i
            self.print_result() 
            

    def print_result(self): # Delivers results
        print(f"O fatorial do seu número é: {self.result}")

calculator = FactorialCalculate() # Object 1
calculator.get_value() # // to Get user value
calculator.checks_conditions() # Checks if the entered value is valid


# Simple form of calculating factorial
#def factorial_calculater(number):
#    factorial = 1
#    if number >= 0:
#        for i in range(1, number+1):
#            factorial *= i
#        print(f"O fatorial é: {factorial}")
#    else:
#        print("Valor inválido")

#number = int(input("Digite um número: "))
#factorial_calculater(number)
