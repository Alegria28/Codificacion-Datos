# Importa la librería matplotlib para crear gráficos
import matplotlib.pyplot as plt

def graficar(cadena):
    # NRZ-I: '1' invierte el nivel, '0' lo mantiene

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
    # Estado del pulso actual (False para bajo, True para alto)
    pulsoPositivo = False

    # Itera sobre cada bit en la cadena de entrada
    for bit in cadena:
        # Añade los puntos de inicio y fin del bit actual en el eje de tiempo
        tiempo.extend([tiempoActual, tiempoActual + duracionBit])

        # Si el bit es '1', invierte el estado del pulso
        if bit == "1":
            pulsoPositivo = not pulsoPositivo

        # Asigna el nivel de voltaje según el estado del pulso
        if pulsoPositivo:
            voltaje.extend([nivelAlto, nivelAlto])
        else:
            voltaje.extend([nivelBajo, nivelBajo])

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
    plt.title("Codificación NRZ-I")

    # Muestra el gráfico generado
    plt.show()