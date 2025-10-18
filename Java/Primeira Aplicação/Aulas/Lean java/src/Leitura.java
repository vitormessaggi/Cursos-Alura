import java.util.Scanner;

public class Leitura {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        System.out.println("Qual o nome do filme?");
        String filme = leitor.nextLine();
        System.out.println("Qual o ano de lançamento?");
        int ano = leitor.nextInt();
        System.out.println("Qual a avaliação?");
        double avaliacao = leitor.nextDouble();

        System.out.println(filme);
        System.out.println(ano);
        System.out.println(avaliacao);
    }
}
