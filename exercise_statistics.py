def statistics():
    num1 = 8
    num2 = 15
    num3 = 23
    num4 = 12

    promedio = (num1 + num2 + num3 + num4) / 4
    maximo = max(num1, num2, num3, num4)
    minimo = min(num1, num2, num3, num4)
    rango = maximo - minimo

    print(promedio)
    print(maximo)
    print(minimo)
    print(rango)