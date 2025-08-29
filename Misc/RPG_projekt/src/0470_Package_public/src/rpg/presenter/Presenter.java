package rpg.presenter;

import rpg.model.GameLogic;
import java.util.ArrayList;

public class Presenter {
    private final ArrayList<PresenterObserver> views = new ArrayList<PresenterObserver>();
    private final GameLogic model;

    public Presenter(GameLogic model) {
        this.model = model;
    }

    public void registerView(PresenterObserver view) { this.views.add(view); }

    private void updateView() {
        for (PresenterObserver view : views) { view.updateView(); }
    }

    public void move(String direction) {
        this.model.moveHero(direction.substring(0,1));
        updateView();
    }

    public void battle() {
        this.model.battle();
        updateView();
    }
}

