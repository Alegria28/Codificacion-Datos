# Importa la librería matplotlib para crear gráficos
import matplotlib.pyplot as plt


def plot(bit_string):
    # Manchester Diferencial: '0' transiciona al inicio, '1' no; siempre transiciona a mitad del bit

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
    # Nivel al final del bit anterior, se asume alto inicialmente
    level_at_end_of_previous_bit = high_level

    # Itera sobre cada bit en la cadena de entrada
    for bit in bit_string:
        level_for_first_half = (
            0  # Variable temporal para el cálculo del nivel de la primera mitad
        )
        level_for_second_half = (
            0  # Variable temporal para el cálculo del nivel de la segunda mitad
        )

        bit_start_level = (
            0  # Nivel para la primera mitad del bit que se usará en la gráfica
        )
        bit_end_level = (
            0  # Nivel para la segunda mitad del bit que se usará en la gráfica
        )

        # Determina el nivel al inicio del bit actual (para la primera mitad)
        # basado en el bit y el nivel final del bit anterior
        if bit == "0":
            # Hay transición al inicio del bit para un '0'
            if level_at_end_of_previous_bit == low_level:
                level_for_first_half = high_level
            else:  # level_at_end_of_previous_bit == high_level
                level_for_first_half = low_level
        else:  # bit == '1'
            # No hay transición al inicio del bit para un '1'
            level_for_first_half = level_at_end_of_previous_bit

        # Determina el nivel para la segunda mitad del bit
        # Siempre hay una transición a mitad del bit
        if level_for_first_half == low_level:
            level_for_second_half = high_level
        else:  # level_for_first_half == high_level
            level_for_second_half = low_level

        # Asigna los niveles calculados a las variables que se usarán para graficar
        bit_start_level = level_for_first_half
        bit_end_level = level_for_second_half

        # Gráfica la primera mitad del bit
        # El voltaje se mantiene en nivel_inicio_bit
        time.extend([current_time, current_time + bit_duration / 2])
        voltage.extend([bit_start_level, bit_start_level])

        # Gráfica la segunda mitad del bit
        # El voltaje se mantiene en nivel_fin_bit
        time.extend([current_time + bit_duration / 2, current_time + bit_duration])
        voltage.extend([bit_end_level, bit_end_level])

        # Actualiza el nivel final para el siguiente bit
        level_at_end_of_previous_bit = bit_end_level

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
    plt.yticks([low_level, high_level], [str(low_level), str(high_level)])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(time_positions, time_labels)

    # Establece el título del gráfico
    plt.title("Differential Manchester Encoding")

    # Muestra el gráfico generado
    plt.show()
