print("*********************************************************")
print(" * * * * * * * Segundo ejemplo de tarea * * * * * * * * * ")
print("*********************************************************\n")

cantidad = int(input("cantidad a invertir: "));
interes = int(input("cantidad de interes que deseas que se le cobre al year: "));
anosInversion = int(input("duracion de la inversion en years: "));
intIver = interes*anosInversion;
ganancias = cantidad + intIver;

print("*********************************************************")
print(" * * * * * * * cantidad invertida: ",cantidad, "              * * * * * * * * * ")
print(" * * * * * * * interes recibido por años: ",interes, "        * * * * * * * * * ")
print(" * * * * * * * Ganancias totales: ",intIver, "                * * * * * * * * * ")
print(" * * * * * * * Monto total: ",ganancias, "                    * * * * * * * * * ")
print("*********************************************************\n")
