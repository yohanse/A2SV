import java.util.Random; // o eficiente

public class NumeroPrimoSorteado { 
    public static void main(String args[]) { // is prime, 1 is not prime
        int rows = 5;

        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= i; j++) {
                if (j == 1 || j == i)
                    System.out.print("* ");
                else
                    System.out.print("  ");
            }
            System.out.println();
        }
    }

}