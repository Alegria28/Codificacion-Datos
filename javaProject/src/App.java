import java.util.Scanner;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class App {
    public static void main(String[] args) throws Exception {

        limpiarPantalla();

        String cadena = obtenerCadena();

        // Iniciamos nuestro scanner
        Scanner lectura = new Scanner(System.in);

        // Según la opción que el usuario elija mostramos la gráfica indicada
        System.out.println("Seleccione una opción:");
        System.out.println("1. NRZ-L");
        System.out.println("2. NRZ-I");
        System.out.println("3. Bipolar AMI");
        System.out.println("4. Pseudoternario");
        System.out.println("5. Manchester");
        System.out.println("6. Código diferencia");

        int opcion = 0;
        do {

            opcion = scanner.nextInt();

        } while (opcion < 1 && opcion > 6);

        // Creamos la ventana a mostrar con su titulo 
        JFrame ventana = new JFrame("Codificación de señales");
        // Configuramos la operación predeterminada al cerrar la ventana (finalizar el programa)
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Establecemos el tamaño de la ventana a 800 píxeles de ancho y 400 píxeles de alto
        ventana.setSize(800, 400);

        switch (opcion) {
            case 1:

                break;
            case 2:

                break;
            case 3:

                break;
            case 4:

                break;
            case 5:

                break;
            case 6:

                break;
        }

    }

    public static String obtenerCadena() {
        // Iniciamos nuestro scanner
        Scanner lectura = new Scanner(System.in);

        // Variable String para almacenar la cadena de bits
        String cadena = new String("");

        // Variable para controlar el ciclo según si la cadena es valida o no
        boolean valido = true;
        do {
            valido = true;

            // Obtenemos la cadena de bits con la que queremos trabajar
            System.out.print("- ");
            cadena = lectura.next();

            // Verificamos si esta cadena esta en binario o no
            for (int i = 0; i < cadena.length(); i++) {
                if (cadena.charAt(i) != '0' && cadena.charAt(i) != '1') {
                    System.out.println("Cadena no valida");
                    valido = false;
                    break;
                }
            }

        } while (!valido);

        lectura.close();

        return cadena;
    }

    public static void limpiarPantalla() {
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Clase para mostrar la gráfica para la codificación NRZ-L
    class NRZ_L extends JPanel {

        // Atributo de la clase
        private String cadena;

        public NRZ_L(String cadena) {
            this.cadena = cadena;
        }

    }
}