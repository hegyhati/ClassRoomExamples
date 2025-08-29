
import java.util.ArrayList;

public class Presenter {
    private final ArrayList<View> views = new ArrayList<View>();
    private final GameLogic model;

    public Presenter(GameLogic model) {
        this.model = model;
    }

    public void registerView(View view) { this.views.add(view); }

    private void updateView() {
        for (View view : views) { view.updateView(); }
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

