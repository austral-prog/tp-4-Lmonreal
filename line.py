def line():
    coeficiente_a = float(input("Ingrese el coeficiente A: "))
    coeficiente_b = float(input("Ingrese el coeficiente B: "))
    coeficiente_x1 = float(input("Ingrese el coeficiente X1: "))
    coeficiente_x2 = float(input("Ingrese el coeficiente X2: "))

    print(f"El coeficiente A de su ecuación de la recta es: {coeficiente_a}")
    print(f"El coeficiente B de su ecuación de la recta es: {coeficiente_b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coeficiente_x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coeficiente_x2}\n")

    print("Para la siguiente ecuación:")
    print(f"\tY = {coeficiente_a}X + {coeficiente_b}\n")

    print("Dados los siguientes puntos:")
    
    p1_y = coeficiente_a * coeficiente_x1 + coeficiente_b
    p2_y = coeficiente_a * coeficiente_x2 + coeficiente_b

    print(f"\tP1 ({coeficiente_x1}, {p1_y})")
    print(f"\tP2 ({coeficiente_x2}, {p2_y})\n")
    distance = (((p2_y - p1_y)**2) + ((coeficiente_x2 - coeficiente_x1)**2))**(1/2)

    print(f"La distancia entre ellos es: {distance}")