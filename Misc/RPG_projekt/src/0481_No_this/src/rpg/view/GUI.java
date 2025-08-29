package rpg.view;

import rpg.model.GameStateViewer;
import rpg.presenter.Presenter;

import java.awt.Insets;
import javax.swing.*;


public class GUI extends JFrame {
    private final InfoPanel unitInfo;
    private final ControlPanel actionControl;
    private final MapPanel smallMap;
    private final MapPanel largeMap;

    public GUI(Presenter presenter, GameStateViewer model) {
        super("RPG GUI");  
        UIManager.put("Label.font", new java.awt.Font("SansSerif", java.awt.Font.PLAIN, 20));
        UIManager.put("Button.font", new java.awt.Font("SansSerif", java.awt.Font.PLAIN, 50));

        setLayout(null);

        actionControl = new ControlPanel(presenter, model);
        actionControl.setBounds(60,330,300,300);
        add(actionControl);

        unitInfo = new InfoPanel(presenter, model);
        unitInfo.setBounds(10, 10, 400, 300);
        add(unitInfo);

        
        smallMap = new MapPanel(presenter, model, 400, 2);
        smallMap.setBounds(10,660,400,400);
        add(smallMap);

        largeMap = new MapPanel(presenter, model, 1050, 10);
        largeMap.setBounds(420,10,1050,1050);
        add(largeMap);

        addNotify();
        Insets insets = getInsets();
        setSize(1480 + insets.left + insets.right, 1070 + insets.top + insets.bottom);
        setResizable(false);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }  

    public void run() {
        setVisible(true);
    }
}