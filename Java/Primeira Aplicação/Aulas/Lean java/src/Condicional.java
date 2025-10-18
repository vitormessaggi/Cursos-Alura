public class Condicional {
    public static void main(String[] args) {
        int anoDeLancamento = 1990;
        boolean incluidoNoPlano = false;
        double notaDoFilme = 8.1;
        String tipoPlano = "Plus";

        if (anoDeLancamento >= 2022) {
            System.out.println("Lançamentos mais assistidos");
        } else {
            System.out.println("Filme retro recomendado");
        }

        if (incluidoNoPlano == true || tipoPlano.equals("Plus")) { //Equals server como se fosse um ==
            System.out.println("Filme liberado");
        }else {
            System.out.println("Deve pagar a locação");
            }
        }
    }

