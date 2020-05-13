import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleDominoGameGUI implements ActionListener{
    public static void main(String[] args) {
        JFrame frame = new JFrame("SimpleDominoGameGUI");
        frame.setContentPane(new SimpleDominoGameGUI().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

    private JPanel mainPanel;
    private JTextArea state;
    private JButton button1;
    private JButton button2;
    private JButton button3;
    private DominoGame game  = new DominoGame();


    private void update(){
        state.setText(game.toString().split("\n\n")[0]);
        button1.setText(game.getTileOption(1).toString());
        button2.setText(game.getTileOption(2).toString());
        button3.setText(game.getTileOption(3).toString());

        if (game.isGameOver()){
            state.setDisabledTextColor(Color.RED);
            state.setEnabled(false);
            button1.setEnabled(false);
            button2.setEnabled(false);
            button3.setEnabled(false);
            JOptionPane.showMessageDialog(null,"Game over!");
        }
    }
    public SimpleDominoGameGUI(){
        update();
        button1.addActionListener(this);
        button2.addActionListener(this);
        button3.addActionListener(this);
    }


    @Override
    public void actionPerformed(ActionEvent actionEvent) {
        int option=1;
        if(actionEvent.getSource()==button1) option=1;
        else if(actionEvent.getSource()==button2) option=2;
        else if(actionEvent.getSource()==button3) option=3;

        try{
            game.continueWithOption(option);
            update();
        } catch (InvalidMoveException e){
            System.err.println("Wrong move");
        }
    }
}
