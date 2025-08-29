package rpg.view;

import rpg.model.*;
import rpg.presenter.Presenter;
import javax.swing.*;

class ControlPanel extends ViewPanel {
    private final JButton upButton;
    private final JButton downButton;
    private final JButton rightButton;
    private final JButton leftButton;
    private final JButton battleButton;

    ControlPanel(Presenter presenter, GameStateViewer model) {
        super(presenter,model);

        setLayout(null);

        upButton = new JButton("↑");
        downButton = new JButton("↓");
        rightButton = new JButton("→");
        leftButton = new JButton("←");
        battleButton = new JButton("⚔");

        upButton.addActionListener(e -> presenter.move("north"));
        downButton.addActionListener(e -> presenter.move("south"));
        rightButton.addActionListener(e -> presenter.move("east"));
        leftButton.addActionListener(e -> presenter.move("west"));
        battleButton.addActionListener(e -> presenter.battle());

        upButton.setBounds(100,0,100,100);
        downButton.setBounds(100, 200, 100, 100);
        leftButton.setBounds(0, 100, 100, 100);
        rightButton.setBounds(200, 100, 100, 100);
        battleButton.setBounds(100, 100, 100, 100);

        add(upButton);
        add(downButton);
        add(leftButton);
        add(rightButton);   
        add(battleButton);

        updateView();
    }

    @Override
    public void updateView() {
        Hero hero = model.getHero();
        Monster monster = model.getMonsterInFrontOfHero();

        battleButton.setEnabled(hero.isAlive() && monster != null);
        upButton.setEnabled(hero.isAlive() && !model.isWall(-1,0));
        downButton.setEnabled(hero.isAlive() && !model.isWall(1,0));
        leftButton.setEnabled(hero.isAlive() && !model.isWall(0,-1));
        rightButton.setEnabled(hero.isAlive() && !model.isWall(0,1));
    }
}