public class NumeroPrimoSorteado { 
    public static void main(String args[]) {
        // Test
        int N = 7;
        System.out.println(findLevel(N)); // The program should print "3".
    }
    
    static int findLevel(int N){
        int height = 1, totalNumberOfNode = 1, NumberOfNodeAtHeight = 1;
        while (totalNumberOfNode < N){
            height++;     // height increase
            NumberOfNodeAtHeight *= height;       // To compute the count of nodes for each level.
            totalNumberOfNode += NumberOfNodeAtHeight;      // To derive the total count of nodes.
        }
        return height;   // Return the numerical value's height.
    }
}