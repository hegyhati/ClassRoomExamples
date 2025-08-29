package rpg.view;

import rpg.model.GameStateViewer;
import rpg.presenter.Presenter;

import java.awt.Insets;
import javax.swing.*;


public class GUI extends JFrame {
    private final InfoPanel unitInfo;
    private final ControlPanel actionControl;
    private final MapPanel map;

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

        map = new MapPanel(presenter, model, 630, 10);
        map.setBounds(420,10,630,630);
        add(map);

        addNotify();
        Insets insets = getInsets();
        setSize(1060 + insets.left + insets.right, 650 + insets.top + insets.bottom);
        setResizable(false);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }  

    public void run() {
        setVisible(true);
    }
}