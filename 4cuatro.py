def calcular_ahorros(cantidad_inicial, tasa_interes, num_anos):
    for i in range(num_anos):
        cantidad_inicial += cantidad_inicial * tasa_interes
        cantidad_inicial = round(cantidad_inicial, 2)
        print(f"Ahorros después del año {i + 1}: ${cantidad_inicial}")

cantidad = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: $"))
interes = 0.04
anos = 3

calcular_ahorros(cantidad, interes, anos)