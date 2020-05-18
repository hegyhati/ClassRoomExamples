import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class YahtzeeGUI extends JFrame {
  private static final long serialVersionUID = 1L;
  private Yahtzee game;
  private final JPanel mainPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
  private final DefaultListModel<Dice> listModel = new DefaultListModel<Dice>();
  private final JList<Dice> listView = new JList<Dice>(listModel);
  private final JButton rollButton = new JButton("Roll");

  private void resetGUI() {
    game = new Yahtzee();
    listModel.clear();
    for (int i = 0; i < 5; ++i)
      listModel.add(i, game.getDice(i));
  }

  public YahtzeeGUI() {
    super("Yahtzee!!!");
    resetGUI();
    listView.setFont(new Font(Font.MONOSPACED, Font.BOLD, 50));
    mainPanel.add(listView);
    mainPanel.add(rollButton);
    setContentPane(mainPanel);

    rollButton.addActionListener((ActionListener) new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent arg0) {
        int[] selected = listView.getSelectedIndices();
        for (int i=0; i<selected.length; ++i) selected[i]++;
        game.rollDices(selected);
        listView.updateUI();
        if (game.isYahtzee()){
          JOptionPane.showMessageDialog(null, "Yahtzee!!!");
          resetGUI();
        }
      }
    });
  }

  public static void main(final String[] args) {
    final YahtzeeGUI game = new YahtzeeGUI();
    game.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    game.pack();
    game.setVisible(true);
  }

}
