package Java;

import java.util.Scanner;

public class Grade {  
    
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter marks: ");
        int mark = input.nextInt();

        if(mark >= 80 && mark <= 100)
            System.out.println("A");
        else if(mark >= 60)
            System.out.println("B");
        else if(mark >= 50)
            System.out.println("C");
        else
            System.out.println("Fail");
    }
}
   

