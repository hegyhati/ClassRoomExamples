import java.util.ArrayList;
import java.util.Scanner;

public class HangmanGame {
  private HiddenWord puzzle;
  private int wrongGuessCount = 0;
  private final int maxGuessCount;

  public HangmanGame(String word, int maxGuessCount) {
    this.puzzle=new HiddenWord(word);
    this.maxGuessCount = maxGuessCount;
  }

  public ArrayList<Integer> guess(char character) {
    if (isGameOver()||isWon()) return null;
    ArrayList<Integer> positions=puzzle.reveal(character);
    if(positions.size()==0) ++wrongGuessCount;
    return positions;
  }

  public String getHealthBar() {
    StringBuilder toReturn = new StringBuilder(" ");
    for (int count = 0; count < maxGuessCount; ++count) {
      if (count < wrongGuessCount) toReturn.append("💀 ");
      else toReturn.append("♥ ");
    }
    return toReturn.toString();
  }

  public String getClue(){
    return puzzle.toString();
  }

  public String toString(){
    return getClue() + getHealthBar();
  }

  public boolean isGameOver() {
    return wrongGuessCount >= maxGuessCount;
  }

  public boolean isWon() {
    return puzzle.isRevealed();
  }

  public static void main(String[] args) {
    System.out.print("Give me a word to guess: ");
    Scanner sc=new Scanner(System.in);
    HangmanGame game=new HangmanGame(sc.nextLine(), 5);
    while(!game.isGameOver() && !game.isWon()){
      System.out.println(game);
      System.out.print("Give me a guess: ");
      if(game.guess(sc.next().charAt(0)).size()>0) System.out.println("Lucky guess!");
      else System.out.println("Too bad, that character does not appear in the hidden word.");
    }
    if(game.isWon()) {
      System.out.println(game);
      System.out.println("Congratulations, you won the game!");
    } else System.out.println("You are hanged. 💀 💀 💀 💀 💀 ");
    sc.close();
  }

}
