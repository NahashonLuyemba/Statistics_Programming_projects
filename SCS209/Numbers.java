public class Numbers {
    public static void main(String[] args) {

        int[] numbers = new int[100];

        for(int i = 0; i < 100; i++) {
            numbers[i] = i + 1;
        }

        for(int i = 0; i < 100; i++) {
            System.out.println(numbers[i]);
        }
    }
}
