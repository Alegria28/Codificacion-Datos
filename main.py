# cspell: ignore caracter, Pseudoternario, duracion, opcion, graficar, codificacion

# Importamos librería para trabajar con gráficos
import matplotlib.pyplot as plt


# ---- Codificaciones ----#
def codificacionNRZ_L():
    # Creamos vectores para los ejes X/Y en nuestra gráfica
    tiempo = []
    voltaje = []
    # Al iniciar a gráfica, el tiempo es 0
    tiempoActual = 0
    # La duración de cada bit en la gráfica, en este caso 1s
    duracionBit = 1
    # Etiquetas a mostrar nuestra gráfica
    etiquetaTiempo = []
    posicionesTiempo = []
    # Definimos los niveles (del eje Y)
    nivelAlto = 1
    nivelBajo = 0

    # Recorremos nuestra cadena
    for bit in cadena:
        # Agregamos el inicio y fin del intervalo
        tiempo.extend([tiempoActual, tiempoActual + duracionBit])

        # Verificamos que bit es, para ponerlo en la gráfica
        if bit == "1":
            voltaje.extend([nivelAlto, nivelAlto])
        else:
            voltaje.extend([nivelBajo, nivelBajo])

        # Para que este al centro de cada bit
        posicionesTiempo.append(tiempoActual + duracionBit / 2)

        # Para que se vea la cadena con la que estamos trabajando
        etiquetaTiempo.append(str(bit))

        # Tras procesar el bit, aumentamos el tiempo
        tiempoActual += duracionBit

    # Función principal para graficar
    # tiempo es la lista de valores para el eje X
    # voltaje es la lista de valores para el eje Y
    # steps-post indica que los puntos se deben conectar con lineas horizontales y luego verticales
    plt.plot(tiempo, voltaje, drawstyle="steps-post")

    # Etiquetas para los ejes
    plt.xlabel("Secuencia de bits")
    plt.ylabel("Nivel del bit")

    # El eje Y muestra 0 y 1
    plt.yticks([nivelBajo, nivelAlto], ["0", "1"])
    # El eje X muestra los bits
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Titulo del gráfico
    plt.title("Codificación NRZ-L")

    # Agregamos un grid al gráfico
    plt.grid(True)

    # Mostramos el gráfico
    plt.show()

def codificacionNRZ_I():
    # Creamos vectores para los ejes X/Y en nuestra gráfica
    tiempo = []
    voltaje = []
    # Al iniciar a gráfica, el tiempo es 0
    tiempoActual = 0
    # La duración de cada bit en la gráfica, en este caso 1s
    duracionBit = 1
    # Etiquetas a mostrar nuestra gráfica
    etiquetaTiempo = []
    posicionesTiempo = []
    # Definimos los niveles (del eje Y)
    nivelAlto = 1
    nivelBajo = 0
    estado = False

    # Recorremos nuestra cadena
    for bit in cadena:
        # Agregamos el inicio y fin del intervalo
        tiempo.extend([tiempoActual, tiempoActual + duracionBit])

        # Si el bit es un 1, entonces cambiamos de estado (arriba --> abajo o abajo--> arriba)
        if bit == "1":
            estado = not estado

        if (bit == "0"or bit == '1') and estado == True:
            voltaje.extend([nivelAlto, nivelAlto])
        elif (bit == "0" or bit == '1') and estado == False:
            voltaje.extend([nivelBajo, nivelBajo])

        # Para que este al centro de cada bit
        posicionesTiempo.append(tiempoActual + duracionBit / 2)

        # Para que se vea la cadena con la que estamos trabajando
        etiquetaTiempo.append(str(bit))

        # Tras procesar el bit, aumentamos el tiempo
        tiempoActual += duracionBit

    # Función principal para graficar
    # tiempo es la lista de valores para el eje X
    # voltaje es la lista de valores para el eje Y
    # steps-post indica que los puntos se deben conectar con lineas horizontales y luego verticales
    plt.plot(tiempo, voltaje, drawstyle="steps-post")

    # Etiquetas para los ejes
    plt.xlabel("Secuencia de bits")
    plt.ylabel("Nivel del bit")

    # El eje Y muestra 0 y 1
    plt.yticks([nivelBajo, nivelAlto], ["0", "1"])

    # El eje X muestra los bits
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Titulo del gráfico
    plt.title("Codificación NRZ-I")

    # Agregamos un grid al gráfico
    plt.grid(True)

    # Mostramos el gráfico
    plt.show()


# Función para mostrar el menu
def menu():
    # Menú de opciones
    while True:
        print("\nSeleccione el tipo de codificación:")
        print("1. NRZ-L")
        print("2. NRZ-I")
        print("3. Bipolar AMI")
        print("4. Pseudoternario")
        print("5. Manchester")
        print("6. Código diferencial")
        print("7. Nueva cadena")
        opcion = input("- ")

        if opcion == "1":
            # Llamamos a nuestra función
            codificacionNRZ_L()

        elif opcion == "2":
            # Llamamos a nuestra función
            codificacionNRZ_I()

        elif opcion == "3":
            print("Seleccionaste Bipolar AMI")
            # Implementar lógica para Bipolar AMI

        elif opcion == "4":
            print("Seleccionaste Pseudoternario")
            # Implementar lógica para Pseudoternario

        elif opcion == "5":
            print("Seleccionaste Manchester")
            # Implementar lógica para Manchester

        elif opcion == "6":
            print("Seleccionaste Código diferencial")
            # Implementar lógica para Código diferencial

        elif opcion == "7":
            print("Regresando...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


# Ciclo para verificar que la cadena sea valida
while True:
    valido = True

    # Obtenemos la cadena de bits en binario
    cadena = str(input("- "))

    # Verificamos si la cadena esta en binario o no
    for caracter in cadena:
        if caracter != "0" and caracter != "1":
            # La bandera cambia de estado, por lo que se repetirá el ciclo otra vez
            valido = False
            print("Cadena no valida")
            break

    # Si la cadena es valida, entonces llamamos a nuestra función
    if valido:
        menu()
