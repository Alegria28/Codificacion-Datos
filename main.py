# cspell: ignore caracter, Pseudoternario, duracion, opcion, graficar, codificacion, transicion

# Importa la librería matplotlib para crear gráficos.
import matplotlib.pyplot as plt


# ---- Codificaciones ----#
def codificacionNRZ_L(cadena):
    # NRZ-L: '1' es nivel alto, '0' es nivel bajo
    
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
        # Añade los puntos de inicio y fin del bit actual en el eje de tiempo
        tiempo.extend([tiempoActual, tiempoActual + duracionBit])

        # Asigna el nivel de voltaje según el valor del bit
        if bit == "1":
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

    # Establece las etiquetas para los ejes X e Y
    plt.xlabel("Secuencia de bits")
    plt.ylabel("Nivel del bit")

    # Define las marcas (ticks) y etiquetas para el eje Y
    plt.yticks([nivelBajo, nivelAlto], ["0", "1"])
    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Establece el título del gráfico
    plt.title("Codificación NRZ-L")

    # Añade una cuadrícula al gráfico
    plt.grid(True)

    # Muestra el gráfico generado
    plt.show()


def codificacionNRZ_I(cadena):
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

    # Establece las etiquetas para los ejes X e Y
    plt.xlabel("Secuencia de bits")
    plt.ylabel("Nivel del bit")

    # Define las marcas (ticks) y etiquetas para el eje Y
    plt.yticks([nivelBajo, nivelAlto], ["0", "1"])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Establece el título del gráfico
    plt.title("Codificación NRZ-I")

    # Añade una cuadrícula al gráfico
    plt.grid(True)

    # Muestra el gráfico generado
    plt.show()


def codificacionBipolarAMI(cadena):
    # Bipolar AMI: '0' es nivel cero, '1' alterna entre +V y -V
    
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
    # Define los niveles de voltaje: alto, medio (cero) y bajo
    nivelAlto = 1
    nivelMedio = 0
    nivelBajo = -1
    # Estado del pulso para el próximo '1' (True para +V, False para -V)
    pulsoPositivo = True

    # Itera sobre cada bit en la cadena de entrada
    for bit in cadena:
        # Añade los puntos de inicio y fin del bit actual en el eje de tiempo
        tiempo.extend([tiempoActual, tiempoActual + duracionBit])

        if bit == "1":
            if pulsoPositivo:
                voltaje.extend([nivelAlto, nivelAlto]) # '1' es +V
            else:
                voltaje.extend([nivelBajo, nivelBajo]) # '1' es -V
                
            pulsoPositivo = not pulsoPositivo # Alterna para el próximo '1'
        else:
            voltaje.extend([nivelMedio, nivelMedio]) # '0' es nivel cero

        # Calcula la posición central del bit para la etiqueta
        posicionesTiempo.append(tiempoActual + duracionBit / 2)
        # Añade el bit actual como etiqueta
        etiquetaTiempo.append(str(bit))

        # Incrementa el tiempo actual para el siguiente bit
        tiempoActual += duracionBit

    # Dibuja la señal codificada
    plt.plot(tiempo, voltaje, drawstyle="steps-post")

    # Establece las etiquetas para los ejes X e Y
    plt.xlabel("Secuencia de bits")
    plt.ylabel("Nivel del bit")

    # Define las marcas (ticks) y etiquetas para el eje Y
    plt.yticks([nivelBajo, nivelMedio, nivelAlto], ["-1", "0", "1"])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Establece el título del gráfico
    plt.title("Codificación Bipolar AMI")

    # Añade una cuadrícula al gráfico
    plt.grid(True)

    # Muestra el gráfico generado
    plt.show()


def codificacionPseudoternario(cadena):
    # Pseudoternario: '1' es nivel cero, '0' alterna entre +V y -V
    
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
    # Define los niveles de voltaje: alto, medio (cero) y bajo
    nivelAlto = 1
    nivelMedio = 0
    nivelBajo = -1
    # Estado del pulso para el próximo '0' (True para +V, False para -V)
    pulsoPositivo = True

    # Itera sobre cada bit en la cadena de entrada
    for bit in cadena:
        # Añade los puntos de inicio y fin del bit actual en el eje de tiempo
        tiempo.extend([tiempoActual, tiempoActual + duracionBit])

        if bit == "0":
            if pulsoPositivo:
                voltaje.extend([nivelAlto, nivelAlto]) # '0' es +V
            else:
                voltaje.extend([nivelBajo, nivelBajo]) # '0' es -V

            pulsoPositivo = not pulsoPositivo # Alterna para el próximo '0'
        else:
            voltaje.extend([nivelMedio, nivelMedio]) # '1' es nivel cero

        # Calcula la posición central del bit para la etiqueta
        posicionesTiempo.append(tiempoActual + duracionBit / 2)
        # Añade el bit actual como etiqueta
        etiquetaTiempo.append(str(bit))

        # Incrementa el tiempo actual para el siguiente bit
        tiempoActual += duracionBit

    # Dibuja la señal codificada
    plt.plot(tiempo, voltaje, drawstyle="steps-post")

    # Establece las etiquetas para los ejes X e Y
    plt.xlabel("Secuencia de bits")
    plt.ylabel("Nivel del bit")

    # Define las marcas (ticks) y etiquetas para el eje Y
    plt.yticks([nivelBajo, nivelMedio, nivelAlto], ["-1", "0", "1"])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Establece el título del gráfico
    plt.title("Codificación Pseudoternario")

    # Añade una cuadrícula al gráfico
    plt.grid(True)

    # Muestra el gráfico generado
    plt.show()


def codificacionManchester(cadena):
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

        if bit == "0": # Para '0', la primera mitad es Alta
            voltaje.extend([nivelAlto, nivelAlto])
        else: # Para '1', la primera mitad es Baja
            voltaje.extend([nivelBajo, nivelBajo])

        # Segunda mitad del bit, transicion (0.5s - 1s)
        tiempo.extend([tiempoActual + duracionBit / 2, tiempoActual + duracionBit])

        if bit == "0": # Para '0', la segunda mitad es Baja (transición Alto->Bajo)
            voltaje.extend([nivelBajo, nivelBajo])
        else: # Para '1', la segunda mitad es Alta (transición Bajo->Alto)
            voltaje.extend([nivelAlto, nivelAlto])

        # Calcula la posición central del bit para la etiqueta
        posicionesTiempo.append(tiempoActual + duracionBit / 2)
        # Añade el bit actual como etiqueta
        etiquetaTiempo.append(str(bit))

        # Incrementa el tiempo actual para el siguiente bit
        tiempoActual += duracionBit

    # Dibuja la señal codificada
    plt.plot(tiempo, voltaje, drawstyle="steps-post")

    # Establece las etiquetas para los ejes X e Y
    plt.xlabel("Secuencia de bits")
    plt.ylabel("Nivel del bit")

    # Define las marcas (ticks) y etiquetas para el eje Y
    plt.yticks([nivelBajo, nivelAlto], ["0", "1"])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Establece el título del gráfico
    plt.title("Codificación Manchester")

    # Añade una cuadrícula al gráfico
    plt.grid(True)

    # Muestra el gráfico generado
    plt.show()


def codificacionCodigoDiferencial(cadena):
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
        nivel_para_primera_mitad = 0 # Variable temporal para el cálculo del nivel de la primera mitad
        nivel_para_segunda_mitad = 0 # Variable temporal para el cálculo del nivel de la segunda mitad
        
        nivel_inicio_bit = 0 # Nivel para la primera mitad del bit que se usará en la gráfica
        nivel_fin_bit = 0    # Nivel para la segunda mitad del bit que se usará en la gráfica

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

        # Grafica la primera mitad del bit
        # El voltaje se mantiene en nivel_inicio_bit
        tiempo.extend([tiempoActual, tiempoActual + duracionBit / 2])
        voltaje.extend([nivel_inicio_bit, nivel_inicio_bit])

        # Grafica la segunda mitad del bit
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

    # Establece las etiquetas para los ejes X e Y
    plt.xlabel("Secuencia de bits")
    plt.ylabel("Nivel del bit")

    # Define las marcas (ticks) y etiquetas para el eje Y
    plt.yticks([nivelBajo, nivelAlto], [str(nivelBajo), str(nivelAlto)])

    # Define las marcas (ticks) y etiquetas para el eje X
    plt.xticks(posicionesTiempo, etiquetaTiempo)

    # Establece el título del gráfico
    plt.title("Codificación Diferencial Manchester")

    # Añade una cuadrícula al gráfico
    plt.grid(True)

    # Muestra el gráfico generado
    plt.show()


# Función para mostrar el menu
def menu(cadena):
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
        print("8. Salir")
        opcion = input("- ")

        # Según la opcion del usuario, se llamara a la función deseada
        if opcion == "1":
            codificacionNRZ_L(cadena)

        elif opcion == "2":
            codificacionNRZ_I(cadena)

        elif opcion == "3":
            codificacionBipolarAMI(cadena)

        elif opcion == "4":
            codificacionPseudoternario(cadena)

        elif opcion == "5":
            codificacionManchester(cadena)

        elif opcion == "6":
            codificacionCodigoDiferencial(cadena)

        elif opcion == "7":
            # Terminamos este ciclo y regresamos a main()
            print("Ingresa nueva cadena")
            break

        elif opcion == "8":
            # Terminamos todo el programa
            exit()

        else:
            print("Opción no válida, intente de nuevo.")


def main():

    # Bucle infinito para permitir al usuario ingresar múltiples cadenas.
    while True:
        valido = True # Bandera para rastrear la validez de la cadena.

        # Solicita al usuario que ingrese una cadena de bits.
        print("\nIngrese la secuencia de bits:")
        cadena = str(input("- "))

        # Verifica que cada carácter en la cadena sea '0' o '1'.
        for caracter in cadena:
            if caracter != "0" and caracter != "1":
                valido = False # Marca la cadena como no válida.
                print("Cadena no valida. Use solo '0' y '1'.")
                break # Sale del bucle de verificación.

        # Si la cadena es válida, llama a la función del menú.
        if valido:
            menu(cadena)


# Llama a la función principal para iniciar el programa.
main()