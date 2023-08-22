def ordenar ():
    lista_numeros = []
    numero1 = int(input("Ingresa un numero: "))
    lista_numeros.append(numero1)

    numero2 = int(input("Ingresa un numero: "))
    lista_numeros.append(numero2)

    numero3 = int(input("Ingresa un numero: "))
    lista_numeros.append(numero3)

    numero4 = int(input("Ingresa un numero: "))
    lista_numeros.append(numero4)

    lista_numeros_ordenados = sorted(lista_numeros)

    print(lista_numeros_ordenados)


ordenar()