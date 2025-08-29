package rpg.view;

import rpg.model.*;
import rpg.presenter.Presenter;
import javax.swing.*;

class InfoPanel extends ViewPanel{
    private final JLabel messageLabel;
    private final JLabel monsterLabel;
    private final JLabel heroLabel;

    InfoPanel(Presenter presenter, GameStateViewer model) {
        super(presenter, model);

        setLayout(null);

        this.heroLabel = new JLabel("");
        this.messageLabel =  new JLabel("Welcome to the game");
        this.monsterLabel = new JLabel("");

        this.heroLabel.setBounds(0, 0, 400, 80);
        this.messageLabel.setBounds(0, 100, 400, 80);
        this.monsterLabel.setBounds(0, 200, 400, 80);

        add(this.messageLabel);
        add(this.heroLabel);
        add(this.monsterLabel);

        updateView();
    }

    @Override
    public void updateView() {
        HeroViewer hero = this.model.getHero();
        MonsterViewer monster = this.model.getMonsterInFrontOfHero();

        this.heroLabel.setText(hero.toString());
        this.monsterLabel.setText( 
            monster != null 
            ? "<html>There is a monster in front of you:<br>" + monster  + "</html>"
            : "There is nothing in front of you."
        ); 
        if (this.model.isGameOver()) this.messageLabel.setText( 
            hero.isAlive() 
            ? "Congrats, " + hero.getOfficialName() + " cleansed the world  of monsters."
            : "The hero died, the monsters reign over the world."
        );
    }
}