//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        System.out.println("This is Screen mach");
        System.out.println("Filme: Top Gun: Maverick");

        int ano = 2022;
        System.out.println("Ano de lançamento: " + ano);
        boolean incluidoNoPlano = true;
        double notaDoFilme = 8.1;
        double media = (9.8+6.3+8.0)/3;
        System.out.println(media);
        String sinopse;
        sinopse = """
                Filme Top Gun
                Filme de aventura com um galã dos anos 80
                Muito bom
                ano de lançamento: 
                """ + ano;
        System.out.println(sinopse);

        int classificacao = (int) media/2; //Transforma o double em int
        System.out.println(classificacao);
    }
}