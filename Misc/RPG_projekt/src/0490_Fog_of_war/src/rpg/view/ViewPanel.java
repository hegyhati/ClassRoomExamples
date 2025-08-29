package rpg.view;

import rpg.model.GameStateViewer;
import rpg.presenter.Presenter;
import rpg.presenter.PresenterObserver;

import javax.swing.JPanel;

public abstract class ViewPanel extends JPanel implements PresenterObserver {
    protected final Presenter presenter;
    protected final GameStateViewer model;

    public ViewPanel(Presenter presenter, GameStateViewer model) {
        this.presenter = presenter;
        presenter.registerView(this);
        this.model = model;
    }
}