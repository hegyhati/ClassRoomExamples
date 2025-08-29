public class Presenter {
    private GUI view = null;
    private final GameLogic model;

    public Presenter(GameLogic model) {
        this.model = model;
    }

    public void setView(GUI view) { this.view = view; }

    private void updateView() {
        if (this.view != null) this.view.updateView();
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

