# Importa la librería matplotlib para crear gráficos
import matplotlib.pyplot as plt


def plot(bit_string):
    # Manchester: '0' es Alto->Bajo, '1' es Bajo->Alto (transición a mitad del bit)

    # Vectores para almacenar los puntos de la gráfica (tiempo y voltaje)
    time = []
    voltage = []
    # Tiempo actual, inicia en 0
    current_time = 0
    # Duración de cada bit en la gráfica
    bit_duration = 1
    # Listas para las etiquetas y sus posiciones en el eje X
    time_labels = []
    time_positions = []
    # Define los niveles de voltaje alto y bajo
    high_level = 1
    low_level = 0

    # Itera sobre cada bit en la cadena de entrada
    for bit in bit_string:
        # Primera mitad del bit (0s - 0.5s)
        time.extend([current_time, current_time + bit_duration / 2])

        if bit == "0":  # Para '0', la primera mitad es Alta
            voltage.extend([high_level, high_level])
        else:  # Para '1', la primera mitad es Baja
            voltage.extend([low_level, low_level])

        # Segunda mitad del bit, transicion (0.5s - 1s)
        time.extend([current_time + bit_duration / 2, current_time + bit_duration])

        if bit == "0":  # Para '0', la segunda mitad es Baja (transición Alto->Bajo)
            voltage.extend([low_level, low_level])
        else:  # Para '1', la segunda mitad es Alta (transición Bajo->Alto)
            voltage.extend([high_level, high_level])

        # Calcula la posición central del bit para la etiqueta
        time_positions.append(current_time + bit_duration / 2)
        # Añade el bit actual como etiqueta
        time_labels.append(str(bit))

        # Incrementa el tiempo actual para el siguiente bit
        current_time += bit_duration

    # Dibuja la señal codificada
    plt.plot(time, voltage, drawstyle="steps-post")

    # Agregamos lineas verticales para separar los ejes X (recorriendo nuestra cadena)
    for t in range(0, len(bit_string) + 1):
        plt.axvline(x=t, color="gray", linestyle="--", alpha=0.5)

    # Agregamos una linea horizontal
    plt.hlines(y=0.5, xmin=0, xmax=len(bit_string), color="gray", linestyle="--", alpha=0.5)

    # Obtener los ejes actuales
    ax = plt.gca()

    # Quitar los bordes (spines)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Define las marcas (ticks) y etiquetas para el eje Y
    plt.yticks([low_level, high_level], ["0", "1"])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(time_positions, time_labels)

    # Establece el título del gráfico
    plt.title("Manchester Encoding")

    # Muestra el gráfico generado
    plt.show()
