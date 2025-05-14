# Importa la librería matplotlib para crear gráficos
import matplotlib.pyplot as plt


def graficar(cadena):
    # Manchester Diferencial: '0' transiciona al inicio, '1' no; siempre transiciona a mitad del bit

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
    # Nivel al final del bit anterior, se asume alto inicialmente
    nivelAlFinalDelBitAnterior = nivelAlto

    # Itera sobre cada bit en la cadena de entrada
    for bit in cadena:
        nivel_para_primera_mitad = (
            0  # Variable temporal para el cálculo del nivel de la primera mitad
        )
        nivel_para_segunda_mitad = (
            0  # Variable temporal para el cálculo del nivel de la segunda mitad
        )

        nivel_inicio_bit = (
            0  # Nivel para la primera mitad del bit que se usará en la gráfica
        )
        nivel_fin_bit = (
            0  # Nivel para la segunda mitad del bit que se usará en la gráfica
        )

        # Determina el nivel al inicio del bit actual (para la primera mitad)
        # basado en el bit y el nivel final del bit anterior
        if bit == "0":
            # Hay transición al inicio del bit para un '0'
            if nivelAlFinalDelBitAnterior == nivelBajo:
                nivel_para_primera_mitad = nivelAlto
            else:  # nivelAlFinalDelBitAnterior == nivelAlto
                nivel_para_primera_mitad = nivelBajo
        else:  # bit == '1'
            # No hay transición al inicio del bit para un '1'
            nivel_para_primera_mitad = nivelAlFinalDelBitAnterior

        # Determina el nivel para la segunda mitad del bit
        # Siempre hay una transición a mitad del bit
        if nivel_para_primera_mitad == nivelBajo:
            nivel_para_segunda_mitad = nivelAlto
        else:  # nivel_para_primera_mitad == nivelAlto
            nivel_para_segunda_mitad = nivelBajo

        # Asigna los niveles calculados a las variables que se usarán para graficar
        nivel_inicio_bit = nivel_para_primera_mitad
        nivel_fin_bit = nivel_para_segunda_mitad

        # Gráfica la primera mitad del bit
        # El voltaje se mantiene en nivel_inicio_bit
        tiempo.extend([tiempoActual, tiempoActual + duracionBit / 2])
        voltaje.extend([nivel_inicio_bit, nivel_inicio_bit])

        # Gráfica la segunda mitad del bit
        # El voltaje se mantiene en nivel_fin_bit
        tiempo.extend([tiempoActual + duracionBit / 2, tiempoActual + duracionBit])
        voltaje.extend([nivel_fin_bit, nivel_fin_bit])

        # Actualiza el nivel final para el siguiente bit
        nivelAlFinalDelBitAnterior = nivel_fin_bit

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
    plt.yticks([nivelBajo, nivelAlto], [str(nivelBajo), str(nivelAlto)])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Establece el título del gráfico
    plt.title("Codificación Diferencial Manchester")

    # Muestra el gráfico generado
    plt.show()
