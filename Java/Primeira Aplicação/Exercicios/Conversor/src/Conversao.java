public class Conversao {
    public static void main(String[] args) {
        double temp = 25.6;
        double far = (temp*1.8) + 32;
        int convertido = (int)far;

        System.out.println("A temperatura de "+temp + "°C, Passando para Fahrenheit é "+ convertido );

    }
}
