import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleHanoiGui {
    private JTextArea state;
    private JButton MOVEButton;
    private JComboBox from;
    private JComboBox to;
    private JLabel message;
    private JPanel mainPanel;
    private HanoiSimulator simulator;


    private void updateState(){
        state.setText(simulator.toString());
    }

    public SimpleHanoiGui(int diskCount){
        simulator=new HanoiSimulator(diskCount);
        updateState();
        MOVEButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                if(simulator.move(Integer.parseInt(from.getSelectedItem().toString()),Integer.parseInt(to.getSelectedItem().toString()))){
                    updateState();
                    message.setText("Successful move.");
                    if(simulator.isFinished()) {
                        JOptionPane.showMessageDialog(null,"Congrats!");
                    }
                } else message.setText("Wrong move, can't do that.");
            }
        });
    }


    public static void main(String[] args) {
        JFrame frame = new JFrame("SimpleHanoiGui");
        frame.setContentPane(new SimpleHanoiGui(3).mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
