import java.awt.Dimension;
import java.awt.Image;
import javax.swing.*;


public class GUI extends JFrame implements View {
    private InfoPanel unitInfo;
    private ControlPanel actionControl;
    private MapPanel smallMap;
    private MapPanel largeMap;

    private final GameStateViewer model;
    private final Presenter presenter;

    public GUI(Presenter presenter, GameStateViewer model) {
        super("RPG GUI");  
        this.model = model;
        this.presenter = presenter;
        this.presenter.registerView(this);
        initialize_elements();  
        updateView();
    }

    private void initialize_elements() {
        UIManager.put("Label.font", new java.awt.Font("SansSerif", java.awt.Font.PLAIN, 20));
        UIManager.put("Button.font", new java.awt.Font("SansSerif", java.awt.Font.PLAIN, 50));

        setLayout(null);

        this.actionControl = new ControlPanel(this.presenter, this.model);
        this.presenter.registerView(this.actionControl);
        this.actionControl.setBounds(60,330,300,300);
        add(this.actionControl);

        this.unitInfo = new InfoPanel(this.model);
        this.presenter.registerView(this.unitInfo);
        this.unitInfo.setBounds(10, 10, 400, 300);
        add(this.unitInfo);

        
        this.smallMap = new MapPanel(this.model, 400, 2);
        this.presenter.registerView(this.smallMap);
        this.smallMap.setBounds(10,660,400,400);
        add(this.smallMap);

        this.largeMap = new MapPanel(this.model, 1050, 10);
        this.presenter.registerView(this.largeMap);
        this.largeMap.setBounds(420,10,1050,1050);
        this.add(largeMap);

        setSize(1480, 1070);
        setResizable(false);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    @Override
    public void updateView() { }    

    public void run() {
        setVisible(true);
    }
}

class ControlPanel extends JPanel implements View {
    private final JButton upButton;
    private final JButton downButton;
    private final JButton rightButton;
    private final JButton leftButton;
    private final JButton battleButton;

    private final GameStateViewer model;
    private final Presenter presenter;

    public ControlPanel(Presenter presenter, GameStateViewer model) {
        this.presenter = presenter;
        this.model = model;

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

class InfoPanel extends JPanel implements View{
    private final JLabel messageLabel;
    private final JLabel monsterLabel;
    private final JLabel heroLabel;

    private final GameStateViewer model;

    public InfoPanel(GameStateViewer model) {
        this.model = model;

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

class MapPanel extends JPanel implements View{
    private final int visibilityRange;
    private final int size;
    private final int tileSize;
    private final JLabel[][] mapView;
    private final ImageIcon WALL_ICON, FREE_ICON, MONSTER_ICON, HERO_ICON, HERO_MONSTER_ICON; 

    private final GameStateViewer model;

    private ImageIcon getScaledTile(String file) {
        return new ImageIcon(new ImageIcon("tiles/" + file).getImage().getScaledInstance(tileSize, tileSize, Image.SCALE_SMOOTH));
    }

    public MapPanel(GameStateViewer model, int size, int visibilityRange) {
        this.visibilityRange = visibilityRange;
        this.size = size;
        this.tileSize  = size / (2*visibilityRange+1);
        this.mapView = new JLabel[2*visibilityRange+1][2*visibilityRange+1];
        this.WALL_ICON = getScaledTile("wall.png");
        this.FREE_ICON = getScaledTile("free.png");
        this.MONSTER_ICON = getScaledTile("monster.png");
        this.HERO_ICON = getScaledTile("hero.png");
        this.HERO_MONSTER_ICON = getScaledTile("heromonster.png");
        this.model = model;

        setLayout(null);
        for (int row = 0; row <  2 * this.visibilityRange + 1 ; ++row)
            for (int col = 0; col < 2 * this.visibilityRange + 1; ++col) {
                JLabel tile = new JLabel();
                tile.setBounds(tileSize*col,tileSize*row, tileSize, tileSize);
                this.mapView[row][col] = tile;
                add(tile);
            }
        setPreferredSize(new Dimension(size,size));

        updateView();
    }

    @Override
    public void updateView() {
         for (int row=-visibilityRange; row <= visibilityRange; ++row)
            for (int col = -visibilityRange; col <= visibilityRange; ++col) 
                this.mapView[row+visibilityRange][col+visibilityRange].setIcon(
                    this.model.isWall(row, col)
                    ? WALL_ICON 
                    : row == 0 && col == 0 && this.model.getHero().isAlive()
                        ? this.model.hasMonster(row, col) ? HERO_MONSTER_ICON : HERO_ICON
                        : this.model.hasMonster(row, col) ? MONSTER_ICON : FREE_ICON
                );
    }
}