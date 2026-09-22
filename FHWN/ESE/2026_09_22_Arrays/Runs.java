import java.util.Scanner;

public class Runs {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("How many runs did you have? ");
        int runCount = sc.nextInt();
        double[] runDistances = new double[runCount];
        double[] runDurations = new double[runCount];

        for (int questionCount = 0; questionCount < runCount; ++questionCount) {
            System.out.println("How long was the next run?");
            runDistances[questionCount] = sc.nextDouble();
            System.out.println("How many minutes did you need for that?");
            runDurations[questionCount] = sc.nextDouble();
        }

        for (int i = 0; i < runCount; ++i) {
            System.out.println("distance of " + (i + 1) + ". run: " + runDistances[i]);
        }

        double totalDistance = 0;
        for (int i = 0; i < runCount; ++i) {
            totalDistance += runDistances[i];
        }

        double maxDistance = runDistances[0];
        for (int i = 1; i < runCount; ++i) {
            if (runDistances[i] > maxDistance) {
                maxDistance = runDistances[i];
            }
        }

        double fastestPace = runDurations[0] / runDistances[0];
        for (int i = 1; i < runCount; ++i) {
            if (runDurations[i] / runDistances[i] < fastestPace) {
                fastestPace = runDurations[i] / runDistances[i];
            }
        }

        System.out.println("Total distance: " + totalDistance);
        System.out.println("Average distance: " + totalDistance / runCount);
        System.out.println("Maximal distance: " + maxDistance);
        System.out.println("Best average pace: " + fastestPace);
    }
}