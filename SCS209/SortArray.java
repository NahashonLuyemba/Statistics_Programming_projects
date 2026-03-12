import java.util.Scanner;

public class SortArray {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int[] numbers = new int[10];

        System.out.println("Enter 10 numbers:");

        for(int i = 0; i < 10; i++) {
            numbers[i] = input.nextInt();
        }

        for(int i = 0; i < 9; i++) {
            for(int j = i + 1; j < 10; j++) {
                if(numbers[i] > numbers[j]) {
                    int temp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = temp;
                }
            }
        }

        System.out.println("Sorted numbers:");
        for(int i = 0; i < 10; i++) {
            System.out.println(numbers[i]);
        }
    }
}
