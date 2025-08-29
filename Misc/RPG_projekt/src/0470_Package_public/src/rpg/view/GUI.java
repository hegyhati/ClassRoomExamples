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

        this.actionControl = new ControlPanel(presenter, model);
        this.actionControl.setBounds(60,330,300,300);
        add(this.actionControl);

        this.unitInfo = new InfoPanel(presenter, model);
        this.unitInfo.setBounds(10, 10, 400, 300);
        add(this.unitInfo);

        
        this.smallMap = new MapPanel(presenter, model, 400, 2);
        this.smallMap.setBounds(10,660,400,400);
        add(this.smallMap);

        this.largeMap = new MapPanel(presenter, model, 1050, 10);
        this.largeMap.setBounds(420,10,1050,1050);
        this.add(largeMap);

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