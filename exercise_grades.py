def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """

    nota1 = 7
    nota2 = 9
    nota3 = 8

    promedio = (nota1 + nota2 + nota3) / 3

    nota_maxima = max(nota1, nota2, nota3)
    nota_minima = min(nota1, nota2, nota3)

    faltan_para_10 = 10 - promedio

    print("Promedio:", promedio)
    print("Nota máxima:", nota_maxima)
    print("Nota mínima:", nota_minima)
    print("Puntos que faltan para llegar a 10:", faltan_para_10)

