import java.util.Scanner;

public class Yahtzee {
  private final Dice[] dices = new Dice[5];

  public Yahtzee() {
    for (int i = 0; i < 5; ++i) {
      dices[i] = new Dice();
      dices[i].roll();
    }
  }

  public void rollDices(final int[] selection) {
    for (final int diceID : selection)
      dices[diceID - 1].roll();
  }

  public String toString() {
    final StringBuilder sb = new StringBuilder("<< ");
    for (int i = 0; i < 5; i++)
      sb.append(dices[i].toString()).append(" ");
    sb.append(">>");
    return sb.toString();
  }

  public boolean isYahtzee() {
    for (int value = dices[0].getValue(), i = 1; i < 5; i++)
      if (dices[i].getValue() != value)
        return false;
    return true;
  }

  public static void main(final String[] args) {
    final Yahtzee game = new Yahtzee();
    final Scanner sc = new Scanner(System.in);

    while (!game.isYahtzee()) {
      System.out.println("" + game + " Which dices would you like to roll?");
      final char[] selectionChars = sc.nextLine().replaceAll("\\D", "").toCharArray();
      final int[] selection = new int[selectionChars.length];
      for (int i = 0; i < selection.length; ++i)
        selection[i] = Character.getNumericValue(selectionChars[i]);
      game.rollDices(selection);
    }
    System.out.println(game);
    System.out.println("Congrats, you won the game!");
  }

  Dice getDice(final int index) {
    return dices[index];
  }

}
