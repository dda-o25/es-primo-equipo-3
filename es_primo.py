"""
Enrique Aranda Gutiérrez
Carlos Ariel González Ramírez
Eric Fernando Panas López Dellamary
Juan Pablo Zepeda Orozco

07/10/2025

Dado un número, el programa determina si es primo o no.
"""
# Entradas
numero = int(input("Ingresa un número: "))

# Proceso
if numero > 1:
    primo = "sí"
    x = 2
    while x < numero:
        if numero % x == 0:
            primo = "no"
            break
        x += 1

# Salidas
print(f'El número {numero} {primo} es primo')