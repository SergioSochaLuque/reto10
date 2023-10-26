#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales
def promedioz(reales) -> float:
    sumas = 0
    for numero in reales:
        sumas += numero
    promedio = sumas / len(reales)
    return promedio

if __name__ == "__main__": #definir la función main con las variables que utilicé
    reales = [12, -14, 8, 14, 19, 32, 15, 0.75]

    promedio = promedioz(reales)

    print(f"El promedio de la lista es {promedio}")