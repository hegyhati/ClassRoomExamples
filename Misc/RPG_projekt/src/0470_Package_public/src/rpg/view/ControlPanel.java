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

        this.upButton = new JButton("↑");
        this.downButton = new JButton("↓");
        this.rightButton = new JButton("→");
        this.leftButton = new JButton("←");
        this.battleButton = new JButton("⚔");

        this.upButton.addActionListener(e -> this.presenter.move("north"));
        this.downButton.addActionListener(e -> this.presenter.move("south"));
        this.rightButton.addActionListener(e -> this.presenter.move("east"));
        this.leftButton.addActionListener(e -> this.presenter.move("west"));
        this.battleButton.addActionListener(e -> this.presenter.battle());

        this.upButton.setBounds(100,0,100,100);
        this.downButton.setBounds(100, 200, 100, 100);
        this.leftButton.setBounds(0, 100, 100, 100);
        this.rightButton.setBounds(200, 100, 100, 100);
        this.battleButton.setBounds(100, 100, 100, 100);

        add(this.upButton);
        add(this.downButton);
        add(this.leftButton);
        add(this.rightButton);   
        add(this.battleButton);

        updateView();
    }

    @Override
    public void updateView() {
        HeroViewer hero = this.model.getHero();
        MonsterViewer monster = this.model.getMonsterInFrontOfHero();

        this.battleButton.setEnabled(hero.isAlive() && monster != null);
        this.upButton.setEnabled(hero.isAlive() && !this.model.isWall(-1,0));
        this.downButton.setEnabled(hero.isAlive() && !this.model.isWall(1,0));
        this.leftButton.setEnabled(hero.isAlive() && !this.model.isWall(0,-1));
        this.rightButton.setEnabled(hero.isAlive() && !this.model.isWall(0,1));
    }
}