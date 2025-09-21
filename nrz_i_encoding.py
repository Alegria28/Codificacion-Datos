# Importa la librería matplotlib para crear gráficos
import matplotlib.pyplot as plt

def plot(bit_string):
    # NRZ-I: '1' invierte el nivel, '0' lo mantiene

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
    # Estado del pulso actual (False para bajo, True para alto)
    is_pulse_positive = False

    # Itera sobre cada bit en la cadena de entrada
    for bit in bit_string:
        # Añade los puntos de inicio y fin del bit actual en el eje de tiempo
        time.extend([current_time, current_time + bit_duration])

        # Si el bit es '1', invierte el estado del pulso
        if bit == "1":
            is_pulse_positive = not is_pulse_positive

        # Asigna el nivel de voltaje según el estado del pulso
        if is_pulse_positive:
            voltage.extend([high_level, high_level])
        else:
            voltage.extend([low_level, low_level])

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
    plt.title("NRZ-I Encoding")

    # Muestra el gráfico generado
    plt.show()