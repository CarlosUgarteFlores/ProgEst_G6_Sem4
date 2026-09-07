#Leer la edad de una persona y decir si es menor o mayor

Age = 0
def readAge():
    print("Dime tu edad: ")
    global Age
    Age = int(input())

def evalAge(Age):
    return Age >=18

def show():
    print("Mayor de edad " if evalAge(Age) else "Menor de edad")

readAge()
show()
