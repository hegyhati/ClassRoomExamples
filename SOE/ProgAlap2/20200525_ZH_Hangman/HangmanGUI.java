import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Scanner;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.Font;

public class HangmanGUI extends JFrame implements ActionListener {
  private final JPanel mainPanel=new JPanel(new BorderLayout(30,30));
  private final JPanel charPanel=new JPanel(new GridLayout(4,7));
  private final HangmanGame game;
  private String clueFormatString="<html><body style=\"text-align: justify;  text-justify: inter-word;\">%s</body></html>";
  private final JLabel clue;
  private final JLabel healthBar;

  public HangmanGUI(final String word) {
    super("Hangman GUI");

    // Initialize game and labels
    game = new HangmanGame(word, 5);
    clue = new JLabel(String.format(clueFormatString,game.getClue()));
    clue.setFont(new Font(Font.MONOSPACED, Font.PLAIN, 50));
    clue.setHorizontalAlignment(JLabel.CENTER);
    healthBar = new JLabel(game.getHealthBar());
    healthBar.setFont(new Font(Font.MONOSPACED, Font.BOLD, 50));
    healthBar.setHorizontalAlignment(JLabel.CENTER);

    // Add guess buttons
    JButton tmp;
    for(char c='A'; c<='Z'; c++) {
      tmp=new JButton(String.valueOf(c));
      tmp.addActionListener(this);
      if(c=='V') charPanel.add(new JLabel());
      charPanel.add(tmp);
    }

    // Compose main panel
    mainPanel.add(clue,BorderLayout.NORTH);
    mainPanel.add(charPanel,BorderLayout.CENTER);
    mainPanel.add(healthBar,BorderLayout.SOUTH);

    // Setup frame
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setContentPane(mainPanel);
    this.pack();
    this.setVisible(true);
  }

  @Override
  public void actionPerformed(final ActionEvent event) {
    if(!game.isGameOver() && !game.isWon()) {
      JButton clicked = (JButton) event.getSource();
      clicked.setEnabled(false);
      char character = clicked.getText().charAt(0);
      if(game.guess(character).size()==0) {
        clicked.setBackground(Color.RED);
        healthBar.setText(game.getHealthBar());
        if(game.isGameOver()) {
          clue.setForeground(Color.RED);
          healthBar.setForeground(Color.RED);
          JOptionPane.showMessageDialog(this, "Game over!");
        }
      } else {
        clicked.setBackground(Color.GREEN);
        clue.setText(String.format(clueFormatString,game.getClue()));
        if(game.isWon()) {
          clue.setForeground(Color.GREEN);
          healthBar.setForeground(Color.GREEN);
          JOptionPane.showMessageDialog(this, "Congrats, you won!");
        }
      }
    }
  }

  public static void main(String[] args) {
    System.out.print("Give me a word to guess: ");
    Scanner sc=new Scanner(System.in);
    new HangmanGUI(sc.nextLine());
    sc.close();
  }
  
}
