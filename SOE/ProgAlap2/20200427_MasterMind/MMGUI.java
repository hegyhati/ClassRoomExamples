import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MMGUI {
    private JPanel mainpanel;
    private JButton button1;
    private DefaultListModel<String> model=new DefaultListModel<String>();
    private JList list1;
    private DefaultComboBoxModel<Integer> model1=new DefaultComboBoxModel<Integer>();
    private DefaultComboBoxModel<Integer> model2=new DefaultComboBoxModel<Integer>();
    private DefaultComboBoxModel<Integer> model3=new DefaultComboBoxModel<Integer>();
    private DefaultComboBoxModel<Integer> model4=new DefaultComboBoxModel<Integer>();
    private JComboBox comboBox1;
    private JComboBox comboBox2;
    private JComboBox comboBox3;
    private JComboBox comboBox4;
    private MMGuess whatever;
    private int guesscount;

    private void reset(){
        whatever=new MMGuess();
        System.out.println(whatever);
        model.clear();
        guesscount=0;
    }
    public MMGUI() {
        reset();
        list1.setModel(model);
        for(int i=1;i<=6;i++){
            model1.addElement(i);
            model2.addElement(i);
            model3.addElement(i);
            model4.addElement(i);
        }
        comboBox1.setModel(model1);
        comboBox2.setModel(model2);
        comboBox3.setModel(model3);
        comboBox4.setModel(model4);

        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                int g1 = (Integer) model1.getSelectedItem();
                int g2 = (Integer) model2.getSelectedItem();
                int g3 = (Integer) model3.getSelectedItem();
                int g4 = (Integer) model4.getSelectedItem();
                try {
                    MMGuess userguess = new MMGuess(g1, g2, g3, g4);
                    guesscount++;
                    int common=whatever.common(userguess);
                    model.addElement(userguess + " -> "+common);
                    if(common==4){
                        JOptionPane.showMessageDialog(null, "Congrats! You solved the problem in "+guesscount+" steps.");
                        reset();
                    }
                } catch (BadColorException e){

                }
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("MMGUI");
        frame.setContentPane(new MMGUI().mainpanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
