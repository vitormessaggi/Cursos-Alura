import java.util.Scanner;

public class Conta {
    public static void main(String[] args) {
        String nome = "vitor Messaggi";
        int conta = 002;
        String tipoConta = "Corrente";
        double saldo = 200;

        Scanner leitor = new Scanner(System.in);
        int opcao=0;
        int valor;

        //menu
        System.out.println("***************************");
        System.out.println("Nome: " + nome);
        System.out.println("Conta " + conta);
        System.out.println("Tipo de conta " + tipoConta);
        System.out.println("Seu saldo: R$" + saldo);
        System.out.println("***************************");


        while(opcao != 4){
            //Lógica do menu
            System.out.println("Escolha uma das opções");
            System.out.println("1 = Consultar saldo");
            System.out.println("2 = Transferir");
            System.out.println("3 = Receber");
            System.out.println("4 = Sair");
            opcao = leitor.nextInt();

            // Lógica menu
            switch (opcao){
                case 1:
                    System.out.println("Seu saldo é de: R$" + saldo);
                    break;
                case 2:
                    System.out.println("Digite o valor para ser transferido");
                    valor = leitor.nextInt();
                    if (valor < saldo){
                        saldo -= valor;
                        System.out.println("Saldo atualizado para: R$" + saldo);
                    }
                    else {
                        System.out.println("Transação não autorizada!");
                    }
                    break;

                case 3:
                    System.out.println("Digite o valor recebido");
                    valor = leitor.nextInt();
                    if (valor>0){
                        saldo+= valor;
                        System.out.println("Saldo atualizado: R$" + saldo);
                    }
                    else{
                        System.out.println("Transação não autorizada!");
                    }
                    break;
            }

        }
        System.out.println("Fechando sistema *");
        System.out.println("Fechando sistema **");
        System.out.println("Fechando sistema ***");

    }
}
