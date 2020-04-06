package tariff;

import java.util.ArrayList;
import java.util.Scanner;
import tariff.Duration;
import tariff.PhoneHistory;
import tariff.PrePayedPlan;
import tariff.PostPayedPlan;

public class Level3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        PhoneHistory myHistory = PhoneHistory(args[2]);

        ArrayList<Plan> planOptions = new ArrayList<Plan>();
        planOptions.addAll(PrePayedPlan.loadPlanssFromFile(args[0]));
        planOptions.addAll(PostPayedPlan.loadPlansFromFile(args[1]));

        Plan bestOption = Planner.getBestPlan(planOptions,myHistory);

        System.out.println("Last month you had "+myHistory.getTotalOutgoingDuration()+" of outgoing calls and "+myHistory.getTotalSentSMS+" SMS sent.");

        System.out.println("Your best option for is the plan " + bestOption.getName() + " and you will pay " + bestOption.getCost(myUsage) + " HUF.");
    
        sc.close();
    }
}
