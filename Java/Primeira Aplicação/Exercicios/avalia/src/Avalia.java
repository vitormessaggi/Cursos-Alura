import java.util.Random;
import java.util.Scanner;

public class Avalia {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);
        int gerado = new Random().nextInt(5);
        int contador =0;
        int tentativa;
        while (contador<5){
            System.out.println("Advinhe o numero que eu pensei" + "\nVOCÊ TEM 5 TENTATIVAS");
            tentativa = leitura.nextInt();
            if (gerado != tentativa){
                System.out.println("Não penssei nesse numero!");
                contador ++;
            }
            else {
                System.out.println("Parabens eu pensei em " + gerado);
                break;
            }
        }



    }
}
