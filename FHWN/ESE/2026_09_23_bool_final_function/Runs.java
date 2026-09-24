import java.util.Scanner;

public class Runs {

    public static boolean isApprovingAnswer(String answer) {
        final String[] APPROVE_ANSWERS = {"ja", "genau", "igen", "si", "1", "yes", "yeah", "yep", "y", "yes!"};
        answer = answer.toLowerCase();
        for (String approve : APPROVE_ANSWERS) {
            if (answer.equals(approve)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("How many runs did you have? ");
        int runCount = sc.nextInt();

        double[] runDistances = new double[runCount];
        double[] runDurations = new double[runCount];
        boolean[] runIsCommunity = new boolean[runCount];
        boolean[] runIsRace = new boolean[runCount];

        for (int questionCount = 0; questionCount < runCount; ++questionCount) {
            System.out.println("How long was the next run?");
            runDistances[questionCount] = sc.nextDouble();

            System.out.println("How many minutes did you need for that?");
            runDurations[questionCount] = sc.nextDouble();

            System.out.println("Was this a community run? (yes/no) ");
            String answer = sc.next();
            runIsCommunity[questionCount] = isApprovingAnswer(answer);

            System.out.println("Was this a race? (yes/no) ");
            answer = sc.next();
            runIsRace[questionCount] = isApprovingAnswer(answer);
        }

        for (int i = 0; i < runDistances.length; ++i) {
            System.out.println("Run #" + (i + 1));
            System.out.println("-------------");
            System.out.println("Distance: " + runDistances[i] + " km");
            int duration = (int) runDurations[i];
            System.out.println("Time: " + duration / 60 + " hours amd " + duration % 60 + " minutes");
            if (runIsCommunity[i]) {
                System.out.println("This was a COMMUNITY run.");
            } else {
                System.out.println("This was NOT a community run.");
            }
            if (runIsRace[i]) {
                System.out.println("This was a RACE.");
            } else {
                System.out.println("This was NOT a race.");
            }
            System.out.println("");
        }

        double totalDistance = 0;
        for (double distance : runDistances) {
            totalDistance += distance;
        }

        double maxDistance = runDistances[0];
        for (double distance : runDistances) {
            if (distance > maxDistance) {
                maxDistance = distance;
            }
        }

        double fastestPace = runDurations[0] / runDistances[0];
        for (int i = 1; i < runDistances.length; ++i) {
            if (runDurations[i] / runDistances[i] < fastestPace) {
                fastestPace = runDurations[i] / runDistances[i];
            }
        }

        System.out.println("Total distance: " + totalDistance);
        System.out.println("Average distance: " + totalDistance / runCount);
        System.out.println("Maximal distance: " + maxDistance);

        int bestPaceInSeconds = (int) (fastestPace * 60);
        System.out.println("Best average pace: " + (bestPaceInSeconds / 60) + ":" + (bestPaceInSeconds % 60));

        sc.close();
    }
}
