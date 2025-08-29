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

        heroLabel = new JLabel("");
        messageLabel =  new JLabel("Welcome to the game");
        monsterLabel = new JLabel("");

        heroLabel.setBounds(0, 0, 400, 80);
        messageLabel.setBounds(0, 100, 400, 80);
        monsterLabel.setBounds(0, 200, 400, 80);

        add(messageLabel);
        add(heroLabel);
        add(monsterLabel);

        updateView();
    }

    @Override
    public void updateView() {
        Hero hero = model.getHero();
        Monster monster = model.getMonsterInFrontOfHero();

        heroLabel.setText(hero.toString());
        monsterLabel.setText( 
            monster != null 
            ? "<html>There is a monster in front of you:<br>" + monster  + "</html>"
            : "There is nothing in front of you."
        ); 
        if (model.isGameOver()) messageLabel.setText( 
            hero.isAlive() 
            ? "Congrats, " + hero.getOfficialName() + " cleansed the world  of monsters."
            : "The hero died, the monsters reign over the world."
        );
    }
}