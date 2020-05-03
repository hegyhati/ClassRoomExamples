import java.util.Scanner;

public class Level1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("How much time did you on the phone last month? (hh:mm:ss) ");
        Duration totalTime=new Duration(sc.next());
        System.out.print("How many messages (SMS) did you send? ");
        int totalSMS=sc.nextInt();
        PhoneUsage myUsage = new SimplePhoneUsage(totalTime,totalSMS);

        System.out.print("How much does a minute of phone call cost in your pre-payed plan? (HUF/min) " );
        double minuteCost=sc.nextDouble();
        System.out.print("How much does an SMS cost? (HUF) ");
        double smsCost=sc.nextDouble();
        PrePayedPlan myPlan = new PrePayedPlan(minuteCost,smsCost);

        System.out.println("You will have to pay " + myPlan.getCost(myUsage) + " HUF for last month.");

        sc.close();
    }
}
