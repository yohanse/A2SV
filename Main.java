import java.io.* ;

class Main {
  public static void main ( String[] args ) {
    int[] data = {3, 1, 5, 7, 4, 12, -3, 8, -2};
    
    // Declare and initialize variables for the two largest
    int largest = Integer.MIN_VALUE;
    int secondLargest = Integer.MIN_VALUE;

    // Compute the two largest
    for (int value : data) {
      if (value > largest) {
        secondLargest = largest; // Update the second largest
        largest = value; // Update the largest
      } else if (value > secondLargest && value < largest) {
        secondLargest = value; // Update the second largest
      }
    }
      
    // Write out the two largest
    System.out.println("Largest: " + largest);
    System.out.println("Second Largest: " + secondLargest);
  }
}