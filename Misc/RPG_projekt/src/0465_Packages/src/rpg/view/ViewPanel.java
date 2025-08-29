package rpg.view;

import rpg.model.GameStateViewer;
import rpg.presenter.Presenter;
import rpg.presenter.View;

import javax.swing.JPanel;

public abstract class ViewPanel extends JPanel implements View {
    protected final Presenter presenter;
    protected final GameStateViewer model;

    public ViewPanel(Presenter presenter, GameStateViewer model) {
        this.presenter = presenter;
        presenter.registerView(this);
        this.model = model;
    }
}