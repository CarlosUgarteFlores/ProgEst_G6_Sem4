#Leer n cantidad de notas decir si es aprendizaje inicial, fundamental,
#satisfactorio y avanzado, mostrar todas las notas

#AI=60 , AF=70 AS=80 AA=90

def evalGrade(grade):
    if grade >= 90:
        return "Aprendizaje Avanzado"
    elif grade >= 80:
        return "Aprendizaje Satisfactorio"
    elif grade >= 70:
        return "Aprendizaje fundamental"
    else:
        return "Aprendizaje Inicial"


def regisGrade():
    number =  int (input("Cantidad de notas a ingresar: "))
    grades = []

    for i in range(number):
        grade = float(input(f"Ingrese la nota {i + 1}:  "))
        grades.append(grade)

    print ("Resultados")

    for i, grade in enumerate(grades, 1):
        level = evalGrade(grade)
        formatted_grade = int(grade) if grade.is_integer() else grade
        print(f"Nota {i}: {formatted_grade}: {level}")
regisGrade()