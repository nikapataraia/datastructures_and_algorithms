import java.util.Scanner;

public class add {
    public static void main(String[] args) {
        //Write a program, which read a String from System.in and print "Hello, <input string>"
        Scanner scann = new Scanner(System.in);
        String text = scann.nextLine();
        System.out.print("Hello, " + text);
        scann.close();
    }

}
