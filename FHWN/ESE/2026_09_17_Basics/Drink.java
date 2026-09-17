import java.util.Scanner;

public class Drink {
    public static void main(String[] args) {
        final int BEER_AGE_LIMIT = 16;
        final int ALMDUDLER_AGE_LIMIT = 3;

        // Create the sc object to read user input. needed only once.
        Scanner sc = new Scanner(System.in);
        System.out.println("Good day!");

        System.out.println("What is your name?");
        String userName = sc.next();
        userName = "Lord " + userName + " first of his name";
        System.out.println("Hi " + userName + ", nice to meet you!");

        System.out.println("How old are you?");
        int age = sc.nextInt();

        while (age < 0) {
            System.out.println("I think you made a mistake, what is your real age? ");
            age = sc.nextInt();
        }

        if (age >= BEER_AGE_LIMIT) {
            System.out.println("Have a beer with me!!!");
        } else if (age > ALMDUDLER_AGE_LIMIT) {
            System.out.println("Well, you are too young, have an Almdudler.");
        } else {
            System.out.println("How can you even type, anyhow, drink some Milk.");
        }

        sc.close();
    }
}