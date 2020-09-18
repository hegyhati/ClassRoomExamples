import java.util.Scanner;

public class War {
    private static void report(Country human, Country computer) {
        System.out.println("Human country: " + human + " Computer country: " + computer);
    }
    public static void human_vs_ai(Country human, Country computer){
        Scanner sc; 

        while (true) {
            report(human,computer);
            if(human.canAttack()) {
                sc=new Scanner(System.in);
                System.out.println("Do you want to attack?");
                while(human.canAttack() && !computer.isDefeated() && sc.next().contains("yes")){
                    System.out.println("Human attacks computer:");
                    System.out.println(human.attack(computer));
                    report(human, computer);
                    if(human.canAttack()) System.out.println("Do you want to attack again?");
                }
                sc.close();
            }
            if(computer.isDefeated()){
                System.out.println("Computer lost, human wins.");
                return;
            } else if (computer.canAttack()) {
                while(computer.canAttack() && !human.isDefeated()) {
                    System.out.println("Computer attacks human:");
                    System.out.println(computer.attack(human));
                    report(human, computer);
                }
            }
            if(human.isDefeated()){
                System.out.println("Human lost, computer wins.");
                return;
            } else {
                System.out.println("Time for reinforcements!");
                report(human, computer);
            }            
        }
    }
    
    public static void main(String[] args) {
        human_vs_ai(new Country(Integer.parseInt(args[0]),Integer.parseInt(args[1])), new Country(Integer.parseInt(args[2]),Integer.parseInt(args[3])));
    }
}
