def suma(num1, num2):
    return num1 + num2

def multiplicacion(num1, num2):
    return num1 * num2

def resta(num1, num2):
    return num1 - num2

def division(num1,num2):

    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return "Operacion erronea"

while True:
    try:
        
        op1= int(input("Ingrese el primer numero:"))

        op2= int(input("Ingrese el segundo numero: "))
        break

    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo")


operacion = input('Ingrese la operacion a realizar (suma, resta, multiplicacion,division)')

if operacion =="suma":
    print(suma(op1,op2))
elif operacion =="resta":
    print(resta(op1,op2))
elif operacion == "multiplicacion":
    print(multiplicacion(op1,op2))
elif operacion == "division":
    print(division(op1,op2))
else:
    print("Operacion no comtemplada") 