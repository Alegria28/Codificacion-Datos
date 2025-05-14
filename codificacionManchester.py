# Importa la librería matplotlib para crear gráficos
import matplotlib.pyplot as plt


def graficar(cadena):
    # Manchester: '0' es Alto->Bajo, '1' es Bajo->Alto (transición a mitad del bit)

    # Vectores para almacenar los puntos de la gráfica (tiempo y voltaje)
    tiempo = []
    voltaje = []
    # Tiempo actual, inicia en 0
    tiempoActual = 0
    # Duración de cada bit en la gráfica
    duracionBit = 1
    # Listas para las etiquetas y sus posiciones en el eje X
    etiquetaTiempo = []
    posicionesTiempo = []
    # Define los niveles de voltaje alto y bajo
    nivelAlto = 1
    nivelBajo = 0

    # Itera sobre cada bit en la cadena de entrada
    for bit in cadena:
        # Primera mitad del bit (0s - 0.5s)
        tiempo.extend([tiempoActual, tiempoActual + duracionBit / 2])

        if bit == "0":  # Para '0', la primera mitad es Alta
            voltaje.extend([nivelAlto, nivelAlto])
        else:  # Para '1', la primera mitad es Baja
            voltaje.extend([nivelBajo, nivelBajo])

        # Segunda mitad del bit, transicion (0.5s - 1s)
        tiempo.extend([tiempoActual + duracionBit / 2, tiempoActual + duracionBit])

        if bit == "0":  # Para '0', la segunda mitad es Baja (transición Alto->Bajo)
            voltaje.extend([nivelBajo, nivelBajo])
        else:  # Para '1', la segunda mitad es Alta (transición Bajo->Alto)
            voltaje.extend([nivelAlto, nivelAlto])

        # Calcula la posición central del bit para la etiqueta
        posicionesTiempo.append(tiempoActual + duracionBit / 2)
        # Añade el bit actual como etiqueta
        etiquetaTiempo.append(str(bit))

        # Incrementa el tiempo actual para el siguiente bit
        tiempoActual += duracionBit

    # Dibuja la señal codificada
    plt.plot(tiempo, voltaje, drawstyle="steps-post")

    # Agregamos lineas verticales para separar los ejes X (recorriendo nuestra cadena)
    for t in range(0, len(cadena) + 1):
        plt.axvline(x=t, color="gray", linestyle="--", alpha=0.5)

    # Agregamos una linea horizontal
    plt.hlines(y=0.5, xmin=0, xmax=len(cadena), color="gray", linestyle="--", alpha=0.5)

    # Obtener los ejes actuales
    ax = plt.gca()

    # Quitar los bordes (spines)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Define las marcas (ticks) y etiquetas para el eje Y
    plt.yticks([nivelBajo, nivelAlto], ["0", "1"])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Establece el título del gráfico
    plt.title("Codificación Manchester")

    # Muestra el gráfico generado
    plt.show()
