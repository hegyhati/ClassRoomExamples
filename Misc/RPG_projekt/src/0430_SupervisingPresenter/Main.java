class Main {
    public static void main(String[] args) throws Exception{
        GameLogic model = new GameLogic("maps/test.xml");
        Presenter presenter = new Presenter(model);
        GUI view = new GUI(presenter,model);
        presenter.setView(view);
        view.run();
    }
}
