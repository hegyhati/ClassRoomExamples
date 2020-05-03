
import java.util.ArrayList;
import java.util.Scanner;

public class Level4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        PhoneHistory myHistory = new PhoneHistory(args[2]);

        ArrayList<Plan> planOptions = new ArrayList<Plan>();
        planOptions.addAll(PrePayedPlan.loadPlansFromFile(args[0]));
        planOptions.addAll(PostPayedPlan.loadPlansFromFile(args[1]));

        Plan bestOption = Planner.getBestPlan(planOptions,myHistory);

       System.out.println("Last month you had "+myHistory.getCallDuration()+" of outgoing calls and "+myHistory.getSMSCount()+" SMS sent.");

        System.out.println("Your best option for is the plan " + bestOption.getName() + " and you will pay " + bestOption.getCost(myHistory) + " HUF.");
        sc.close();
    }
}
