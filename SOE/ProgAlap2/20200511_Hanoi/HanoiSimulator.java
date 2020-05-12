import java.lang.reflect.Array;
import java.util.Scanner;

public class HanoiSimulator {
    private HanoiTower [] towers = new HanoiTower[3];

    public HanoiSimulator(int diskCount){
        towers[0]=new HanoiTower(diskCount);
        towers[1]=new HanoiTower();
        towers[2]=new HanoiTower();
    }

    public boolean isFinished(){
        return towers[0].isEmpty() && towers[2].isEmpty();
    }

    public String toString(){
        String toReturn = "State of Hanoi towers:\n";
        for (int i = 0; i < 3; i++) {
            toReturn += " - Tower "+(i+1)+": "+towers[i]+"\n";
        }
        return toReturn;
    }

    public boolean move(int from, int to){
        if (from<1 || from > 3 || to < 1 || to >3 ) return false;
        else if (towers[from-1].isEmpty()) return false;
        else {
            int disk=towers[from-1].pop();
            if(towers[to-1].put(disk)) {
                return true;
            } else {
                towers[from-1].put(disk);
                return false;
            }
        }
    }

    public static void main(String[] args) {
        HanoiSimulator simulator = new HanoiSimulator(2);
        Scanner sc=new Scanner(System.in);
        while(!simulator.isFinished()) {
            System.out.println(simulator);
            System.out.print("Which tower should I take the top disk from? (1-3) ");
            int from = sc.nextInt();
            System.out.print("On which tower should I put it down? (1-3) ");
            int to = sc.nextInt();
            if(simulator.move(from,to)) System.out.println("Move successful.");
            else System.out.println("This move can not be carried out.");
        }

        System.out.println(simulator);
        System.out.println("Congrats, you win. You've just brought the end of the world. Thanks.... -.-");
    }
}





