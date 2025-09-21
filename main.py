# cspell: ignore caracter, Pseudoternario, duracion, opcion, graficar, codificacion, transicion

# Importamos los archivos para las modificaciones
import nrz_l_encoding
import nrz_i_encoding
import bipolar_ami_encoding
import pseudoternary_encoding
import manchester_encoding
import differential_manchester_encoding


# Función para mostrar el menu
def show_menu(bit_string):
    # Menú de opciones
    while True:
        print("\nSelect the encoding type:")
        print("1. NRZ-L")
        print("2. NRZ-I")
        print("3. Bipolar AMI")
        print("4. Pseudoternary")
        print("5. Manchester")
        print("6. Differential Manchester")
        print("7. New bit string")
        print("8. Exit")
        option = input("- ")

        # Según la opcion del usuario, se llamara a la función deseada
        if option == "1":
            nrz_l_encoding.plot(bit_string)

        elif option == "2":
            nrz_i_encoding.plot(bit_string)

        elif option == "3":
            bipolar_ami_encoding.plot(bit_string)

        elif option == "4":
            pseudoternary_encoding.plot(bit_string)

        elif option == "5":
            manchester_encoding.plot(bit_string)

        elif option == "6":
            differential_manchester_encoding.plot(bit_string)

        elif option == "7":
            # Terminamos este ciclo y regresamos a main()
            print("Enter a new bit string")
            break

        elif option == "8":
            # Terminamos todo el programa
            exit()

        else:
            print("Invalid option, please try again.")


def main():

    # Bucle infinito para permitir al usuario ingresar múltiples cadenas.
    while True:
        is_valid = True  # Bandera para rastrear la validez de la cadena.

        # Solicita al usuario que ingrese una cadena de bits.
        print("\nEnter the bit sequence:")
        bit_string = str(input("- "))

        # Verifica que cada carácter en la cadena sea '0' o '1'.
        for character in bit_string:
            if character != "0" and character != "1":
                is_valid = False  # Marca la cadena como no válida.
                print("Invalid string. Use only '0' and '1'.")
                break  # Sale del bucle de verificación.

        # Si la cadena es válida, llama a la función del menú.
        if is_valid:
            show_menu(bit_string)


# Iniciamos el programa desde el main
main()
