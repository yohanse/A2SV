import java.util.Random; // o eficiente

public class NumeroPrimoSorteado { 
    public static boolean isPrimo(int numero) { // is prime, 1 is not prime
        if (numero <= 1) { return false; }
        for (int i = 2; i <= Math.sqrt(numero); i++) {
                if (numero % i == 0) {
                    return false;
                }
            }
        
            return true;
    }

    public static int sortearNumero() {  // generate random number
        Random random = new Random();
        return random.nextInt(500000) + 1;
    }
    
    public static void main(String[] args) {
        int menorPrimo = Integer.MAX_VALUE;
        int maiorPrimo = Integer.MIN_VALUE;
        int quantidadePrimos = 0;
    
        int quantidadeSorteios = 10;
        int[] primosPorPosicao = new int[quantidadeSorteios];
        for(int j = 0; j < 10; j++){
            System.out.print(primosPorPosicao[j]);
        }
        System.out.println();
        for (int i = 0; i < quantidadeSorteios; i++) {
            int numeroSorteado = sortearNumero();
            if (isPrimo(numeroSorteado)) {
                quantidadePrimos++;
                primosPorPosicao[i]++;
                if (numeroSorteado < menorPrimo) {
                    menorPrimo = numeroSorteado;
                }
                if (numeroSorteado > maiorPrimo) {
                    maiorPrimo = numeroSorteado;
                }
            }
        }
        System.out.println("hello");
        System.out.println("Menor número primo sorteado: " + menorPrimo);
        System.out.println("Maior número primo sorteado: " + maiorPrimo);
        System.out.println("Quantidade de números primos sorteados: " + quantidadePrimos);
    
        System.out.println("Quantidade de números primos sorteados em cada posição do vetor:");
        for (int i = 1; i <= quantidadeSorteios; i++){
            System.out.println("na iteração " + i + " " + primosPorPosicao[i - 1]);
        }
    }     
}