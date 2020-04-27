import java.util.Scanner;


public class TerminalMMGame {
    static boolean play(int maxtry){
        MMGuess whatever = new MMGuess();
        System.err.println("CHEAT: " + whatever);
        int usertry=0;
        boolean success=false;
        Scanner sc=new Scanner(System.in);
        int g1,g2,g3,g4;
        while(usertry<maxtry && !success){
            g1=sc.nextInt();
            g2=sc.nextInt();
            g3=sc.nextInt();
            g4=sc.nextInt();
            try {
                MMGuess newguess = new MMGuess(g1, g2, g3, g4);
                int common = whatever.common(newguess);
                System.out.println("Good guesses: "+common);
                if(common==4) success=true;
            } catch (BadColorException e){
                System.out.println("This try was wasted on bad colors.");
            }
            usertry++;
        }
        if(success)
            System.out.println("Congrats");
        else
            System.out.println("Maybe next time");

        return success;
    }

    public static void main(String[] args) {
        play(3);
    }
}
