import java.util.Scanner;


class Run {
    double distance;
    double duration;
    boolean isCommunity;
    boolean isRace;

    public void prettyPrint() {
        System.out.println("Distance: " + this.distance + " km");
        int duration = (int) this.duration;
        System.out.println("Time: " + duration / 60 + " hours amd " + duration % 60 + " minutes");
        if (this.isCommunity) {
            System.out.println("This was a COMMUNITY run.");
        } else {
            System.out.println("This was NOT a community run.");
        }
        if (this.isRace) {
            System.out.println("This was a RACE.");
        } else {
            System.out.println("This was NOT a race.");
        }
        System.out.println("");
    }
}

public class RunManager {

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

    public static Run getRunDataFromUser(Scanner sc) {
        Run newRun = new Run();

        System.out.println("How long was the run?");
        newRun.distance = sc.nextDouble();

        System.out.println("How many minutes did you need for that?");
        newRun.duration = sc.nextDouble();

        System.out.println("Was this a community run? (yes/no) ");
        String userAnswer = sc.next();
        newRun.isCommunity = isApprovingAnswer(userAnswer);

        System.out.println("Was this a race? (yes/no) ");
        userAnswer = sc.next();
        newRun.isRace = isApprovingAnswer(userAnswer);

        return newRun;
    }

    public static double calculateTotalDistance(Run[] runs){
        double totalDistance = 0;
        for (Run run: runs) {
            totalDistance += run.distance;
        }
        return totalDistance;
    }

    public static double getMaxDistance(Run[] runs) {
        double maxDistance = runs[0].distance;
        for (Run run: runs) {
            if (run.distance > maxDistance) {
                maxDistance = run.distance;
            }
        }
        return maxDistance;
    }
    
    public static double getFastestPace(Run[] runs) {
        double fastestPace = runs[0].duration / runs[0].distance;
        for (int i = 1; i < runs.length; ++i) {
            if (runs[i].duration / runs[i].distance < fastestPace) {
                fastestPace = runs[i].duration / runs[i].distance;
            }
        }
        return fastestPace;
    }
    
    public static void printStatistics(Run[] runs) {
        System.out.println("Total distance: " + calculateTotalDistance(runs));
        System.out.println("Average distance: " + calculateTotalDistance(runs) / runs.length);
        System.out.println("Maximal distance: " + getMaxDistance(runs));

        int bestPaceInSeconds = (int) (getFastestPace(runs) * 60);
        System.out.println("Best average pace: " + (bestPaceInSeconds / 60) + ":" + (bestPaceInSeconds % 60));
    }

    public static void printAllRunData(Run[] runs) {
        for (int i = 0; i < runs.length; ++i) {
            System.out.println("Run #" + (i + 1));
            System.out.println("-------------");
            runs[i].prettyPrint();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("How many runs did you have? ");
        int runCount = sc.nextInt();

        Run[] runs = new Run[runCount];

        for (int questionCount = 0; questionCount < runCount; ++questionCount) {
            runs[questionCount] = getRunDataFromUser(sc);
        }

        printAllRunData(runs);
        printStatistics(runs);

        sc.close();
    }
}
