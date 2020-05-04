import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class MainWindow implements ActionListener{
    private JPanel mainPanel;
    private JButton UPButton;
    private JButton DOWNButton;
    private JButton RIGHTButton;
    private JButton LEFTButton;
    private JPanel gamePanel;

    private JLabel[][] fields = new JLabel[4][4];
    private GameState state;

    private void updateView(){
        for(int row=0; row<4;row++) {
            for (int col = 0; col < 4; col++) {
                fields[row][col].setText(state.getField(row,col));
            }
        }
    }

    @Override
    public void actionPerformed(ActionEvent actionEvent){
        try {
            if(actionEvent.getSource()==LEFTButton) state.left();
            else if(actionEvent.getSource()==RIGHTButton) state.right();
            else if(actionEvent.getSource()==UPButton) state.up();
            else if(actionEvent.getSource()==DOWNButton) state.down();
        } catch (GameOverException e) {
            JOptionPane.showMessageDialog(null,"Game Over");
            state.reset();
        } finally {
            updateView();
        }
    }



    public MainWindow(){
        RIGHTButton.addActionListener(this);
        LEFTButton.addActionListener(this);
        UPButton.addActionListener(this);
        DOWNButton.addActionListener(this);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("MainWindow");
        frame.setContentPane(new MainWindow().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

    private void createUIComponents() {
        gamePanel=new JPanel(new GridLayout(4,4));
        for(int row=0; row<4;row++) {
            for (int col = 0; col < 4; col++) {
                fields[row][col] = new JLabel();
                gamePanel.add(fields[row][col]);
            }
        }
        state=new GameState();
        updateView();
    }
}
