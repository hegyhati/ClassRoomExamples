package rpg;

import rpg.model.GameLogic;
import rpg.presenter.Presenter;
import rpg.view.GUI;

class Main {
    public static void main(String[] args) throws Exception{
        GameLogic model = new GameLogic("resources/maps/final.xml");
        Presenter presenter = new Presenter(model);
        GUI view = new GUI(presenter,model);
        view.run();
    }
}
