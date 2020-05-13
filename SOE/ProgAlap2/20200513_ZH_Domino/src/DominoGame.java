import java.util.ArrayList;
import java.util.Scanner;

class InvalidMoveException extends Exception {}

public class DominoGame {
    private ArrayList<DominoTile> queue = new ArrayList<DominoTile>();
    private DominoTile[] options = new DominoTile[3];

    public DominoGame(){
        queue.add(new DominoTile());
        for (int option = 0; option < 3; option++) {
            options[option]=new DominoTile();
        }
    }

    public DominoTile getTileOption(int option){
        return  options[option-1];
    }

    public void continueWithOption(int option) throws InvalidMoveException{
        if(options[option-1].canConnectFromLeft(queue.get(0))){
            queue.add(0,options[option-1]);
            options[option-1]=new DominoTile();
        } else throw new InvalidMoveException();
    }

    public String toString(){
        StringBuilder sb=new StringBuilder("\n");
        for (int i = 0; i < queue.size(); i+=2) sb.append(" "+queue.get(i));
        sb.append("\n    ");
        for (int i = 1; i < queue.size(); i+=2) sb.append(" "+queue.get(i));
        sb.append("\n\n");
        for (int i = 0; i < 3; i++) sb.append("Option "+(i+1)+": "+options[i]+"\n");
        return sb.toString();
    }

    public boolean isGameOver(){
        return ! options[0].canConnectFromLeft(queue.get(0)) &&
               ! options[1].canConnectFromLeft(queue.get(0)) &&
               ! options[2].canConnectFromLeft(queue.get(0));
    }

    public static void main(String[] args) {
        DominoGame game = new DominoGame();
        Scanner sc=new Scanner(System.in);
        while(!game.isGameOver()) {
            System.out.println(game);
            System.out.print("Which domino should I use? (1-3) ");
            int domino = sc.nextInt();
            try{
                game.continueWithOption(domino);
            } catch (InvalidMoveException e) {
                System.out.println("Domino "+game.getTileOption(domino)+" can not be used to continue.");
            }
        }
        System.err.println(game);
        System.out.println("Game over");

    }


}
