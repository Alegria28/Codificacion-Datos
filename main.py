# cspell: ignore caracter, Pseudoternario, duracion, opcion, graficar, codificacion, transicion

# Importamos los archivos para las modificaciones
import codificacionNRZ_L
import codificacionNRZ_I
import codificacionBipolarAMI
import codificacionPseudoternario
import codificacionManchester
import codificacionCodigoDiferencial


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
            codificacionNRZ_L.graficar(cadena)

        elif opcion == "2":
            codificacionNRZ_I.graficar(cadena)

        elif opcion == "3":
            codificacionBipolarAMI.graficar(cadena)

        elif opcion == "4":
            codificacionPseudoternario.graficar(cadena)

        elif opcion == "5":
            codificacionManchester.graficar(cadena)

        elif opcion == "6":
            codificacionCodigoDiferencial.graficar(cadena)

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
        valido = True  # Bandera para rastrear la validez de la cadena.

        # Solicita al usuario que ingrese una cadena de bits.
        print("\nIngrese la secuencia de bits:")
        cadena = str(input("- "))

        # Verifica que cada carácter en la cadena sea '0' o '1'.
        for caracter in cadena:
            if caracter != "0" and caracter != "1":
                valido = False  # Marca la cadena como no válida.
                print("Cadena no valida. Use solo '0' y '1'.")
                break  # Sale del bucle de verificación.

        # Si la cadena es válida, llama a la función del menú.
        if valido:
            menu(cadena)


# Iniciamos el programa desde el main
main()
