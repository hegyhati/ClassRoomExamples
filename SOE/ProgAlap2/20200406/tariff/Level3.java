package tariff;

import java.util.ArrayList;
import java.util.Scanner;
import tariff.Duration;
import tariff.PhoneUsage;
import tariff.PrePayedPlan;
import tariff.PostPayedPlan;

public class Level3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("How much time did you on the phone last month? (hh:mm:ss)");
        Duration totalTime=new Duration(sc.next());
        System.out.print("How many messages (SMS) did you send? ");
        int totalSMS=sc.nextInt();
        PhoneUsage myUsage = new Usage(totalTime,totalSMS);

        ArrayList<Plan> planOptions = new ArrayList<Plan>();
        planOptions.addAll(PrePayedPlan.loadPlanssFromFile(args[0]));
        planOptions.addAll(PostPayedPlan.loadPlansFromFile(args[1]));

        Plan bestOption = Planner.getBestPlan(planOptions,myUsage);

        System.out.println("Your best option for the last month is the plan " + bestOption.getName() + " and you will pay " + bestOption.getCost(myUsage) + " HUF.");
    
        sc.close();
    }
}
