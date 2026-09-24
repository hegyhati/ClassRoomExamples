
import java.util.Scanner;

public class Main {
    private static final Scanner sc = new Scanner(System.in);

    final static String[] YES_ANSWERS = {"ja", "genau", "igen", "si", "1", "yes", "yeah", "yep", "y"};
    final static String[] NO_ANSWERS = {"nein", "ne", "nem", "0", "no", "nope", "n"};

    private static boolean isIn(String[] options, String answer) {
        for (String option : options) 
            if (answer.equals(option))
                return true;
        return false;
    }

    private static boolean askYesNoQuestion(String question) {
        System.out.println(question + " (yes/no) ");
        while (true) {
            final String answer = sc.next().toLowerCase();
            if (isIn(YES_ANSWERS,answer)) return true;
            if (isIn(NO_ANSWERS,answer)) return false;
            System.out.println("Provide a yes or no answer. " + question);
        }
    }

    private static Run readRunFromUser() {
        System.out.println("How long was the next run?");
        final double distance = sc.nextDouble();

        System.out.println("How many minutes did you need for that?");
        final Duration duration = new Duration((int) (sc.nextDouble() * 60));

        Run.RunType type;
        if (askYesNoQuestion("Was this a grouprun?")) type = Run.RunType.GROUP;
        else if (askYesNoQuestion("Was this a race?")) type = Run.RunType.RACE;
        else type = Run.RunType.REGULAR;
        
        return new Run(distance,duration,type);
    }

    public static void main(String[] args) {
        RunCollection runs = new RunCollection();

        MAIN_LOOP: while (true) {
            System.out.println("""
            What do you want to do?
                1) Add a run.
                2) Print total distance.
                3) Print the fastest run.
                4) Print the longest run.
                5) Exit.
            """);
            switch(sc.nextInt()) {
                case 1 -> { runs.addRun(readRunFromUser()); }
                case 2 -> { System.err.println(runs.getTotalDistanceInKm()) ;}
                case 3 -> { System.out.println(runs.getFastestRun()); }
                case 4 -> { System.out.println(runs.getLongestRun()); }
                case 5 -> { System.err.println("Bye-bye!"); break MAIN_LOOP; }
            }
        }
        
    }
}