import java.util.Scanner;

public class Loop2 {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);
        double media = 0;
        double nota = 0;
        int total=0;
        while (nota!=-1) {
            System.out.println("QUal a nota para o filme ou digite -1 para sair");
            nota = leitura.nextDouble();
            if(nota!= -1){
                media += nota; //Valor da média mais nota
                total++;
            }

            if (nota == 0){
                System.out.println("Não foi digitado nenhuma nota");
            }
        }
        System.out.println("Média de avaliações " + media/total);

    }
}
