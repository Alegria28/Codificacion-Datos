# Importa la librería matplotlib para crear gráficos
import matplotlib.pyplot as plt


def plot(bit_string):
    # Bipolar AMI: '0' es nivel cero, '1' alterna entre +V y -V

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
    # Define los niveles de voltaje: alto, medio (cero) y bajo
    high_level = 1
    mid_level = 0
    low_level = -1
    # Estado del pulso para el próximo '1' (True para +V, False para -V)
    is_pulse_positive = True

    # Itera sobre cada bit en la cadena de entrada
    for bit in bit_string:
        # Añade los puntos de inicio y fin del bit actual en el eje de tiempo
        time.extend([current_time, current_time + bit_duration])

        if bit == "1":
            if is_pulse_positive:
                voltage.extend([high_level, high_level])  # '1' es +V
            else:
                voltage.extend([low_level, low_level])  # '1' es -V

            is_pulse_positive = not is_pulse_positive  # Alterna para el próximo '1'
        else:
            voltage.extend([mid_level, mid_level])  # '0' es nivel cero

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
    plt.hlines(y=0, xmin=0, xmax=len(bit_string), color="gray", linestyle="--", alpha=0.5)

    # Obtener los ejes actuales
    ax = plt.gca()

    # Quitar los bordes (spines)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Define las marcas (ticks) y etiquetas para el eje Y
    plt.yticks([low_level, mid_level, high_level], ["-1", "0", "1"])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(time_positions, time_labels)

    # Establece el título del gráfico
    plt.title("Bipolar AMI Encoding")

    # Muestra el gráfico generado
    plt.show()
