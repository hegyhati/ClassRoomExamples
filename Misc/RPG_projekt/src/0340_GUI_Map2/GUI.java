import java.awt.Image;
import java.awt.event.ActionEvent;
import javax.swing.*;


public class GUI extends JFrame {
    private JLabel messageLabel;
    private JLabel monsterLabel;
    private JLabel heroLabel;
    private JButton upButton;
    private JButton downButton;
    private JButton rightButton;
    private JButton leftButton;
    private JButton battleButton;
    private final int MAP_VISIBILITY = 3;
    private final int tileSize = 300 / (2*MAP_VISIBILITY+1);
    private final JLabel[][] mapView =  new JLabel[2*MAP_VISIBILITY+1][2*MAP_VISIBILITY+1];

    private ImageIcon getScaledTile(String file) {
        return new ImageIcon(new ImageIcon("tiles/" + file).getImage().getScaledInstance(tileSize, tileSize, Image.SCALE_SMOOTH));
    }
    private final ImageIcon WALL_ICON = getScaledTile("wall.png");
    private final ImageIcon FREE_ICON = getScaledTile("free.png");
    private final ImageIcon MONSTER_ICON = getScaledTile("monster.png");
    private final ImageIcon HERO_ICON = getScaledTile("hero.png");
    private final ImageIcon HERO_MONSTER_ICON = getScaledTile("heromonster.png");

    private final GameLogic model;

    public GUI(String mapFileName) throws Exception {
        super("RPG GUI");  
        initialize_elements();  
        model = new GameLogic(mapFileName);
        update();
    }

    private void initialize_elements() {
        UIManager.put("Label.font", new java.awt.Font("SansSerif", java.awt.Font.PLAIN, 20));
        UIManager.put("Button.font", new java.awt.Font("SansSerif", java.awt.Font.PLAIN, 50));

        setLayout(null);

        heroLabel = new JLabel("");
        messageLabel =  new JLabel("Welcome to the game");
        monsterLabel = new JLabel("");

        heroLabel.setBounds(320, 20, 400, 80);
        messageLabel.setBounds(320, 120, 400, 80);
        monsterLabel.setBounds(320, 220, 400, 80);

        add(messageLabel);
        add(heroLabel);
        add(monsterLabel);

        upButton = new JButton("↑");
        downButton = new JButton("↓");
        rightButton = new JButton("→");
        leftButton = new JButton("←");
        battleButton = new JButton("⚔");

        upButton.addActionListener(e -> moveButtonClicked(e, "north"));
        downButton.addActionListener(e -> moveButtonClicked(e, "south"));
        rightButton.addActionListener(e -> moveButtonClicked(e, "east"));
        leftButton.addActionListener(e -> moveButtonClicked(e, "west"));
        battleButton.addActionListener(this::attackButtonClicked);

        upButton.setBounds(110,10,100,100);
        downButton.setBounds(110, 210, 100, 100);
        leftButton.setBounds(10, 110, 100, 100);
        rightButton.setBounds(210, 110, 100, 100);
        battleButton.setBounds(110, 110, 100, 100);

        add(upButton);
        add(downButton);
        add(leftButton);
        add(rightButton);   
        add(battleButton);

        for (int row=-MAP_VISIBILITY; row <= MAP_VISIBILITY; ++row)
            for (int col = -MAP_VISIBILITY; col <= MAP_VISIBILITY; ++col) {
                JLabel tile = new JLabel();
                tile.setBounds(890 - tileSize/2 + col * tileSize, 160 - tileSize/2 + row * tileSize, tileSize, tileSize);
                this.mapView[row + MAP_VISIBILITY][col + MAP_VISIBILITY] = tile;
                add(tile);
            }


        setSize(1050, 320);
        setResizable(false);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    private void update() {
        HeroViewer hero = this.model.getHero();
        MonsterViewer monster = this.model.getMonsterInFrontOfHero();

        this.heroLabel.setText(hero.toString());
        monsterLabel.setText( 
            monster != null 
            ? "<html>There is a monster in front of you:<br>" + monster  + "</html>"
            : "There is nothing in front of you."
        ); 

        battleButton.setEnabled(hero.isAlive() && monster != null);
        upButton.setEnabled(hero.isAlive() && !this.model.isWall(-1,0));
        downButton.setEnabled(hero.isAlive() && !this.model.isWall(1,0));
        leftButton.setEnabled(hero.isAlive() && !this.model.isWall(0,-1));
        rightButton.setEnabled(hero.isAlive() && !this.model.isWall(0,1));

        for (int row=-MAP_VISIBILITY; row <= MAP_VISIBILITY; ++row)
            for (int col = -MAP_VISIBILITY; col <= MAP_VISIBILITY; ++col) 
                this.mapView[row+MAP_VISIBILITY][col+MAP_VISIBILITY].setIcon(
                    this.model.isWall(row, col)
                    ? WALL_ICON 
                    : row == 0 && col == 0 && hero.isAlive()
                        ? this.model.hasMonster(row, col) ? HERO_MONSTER_ICON : HERO_ICON
                        : this.model.hasMonster(row, col) ? MONSTER_ICON : FREE_ICON
                );

        if (model.isGameOver()) messageLabel.setText( 
            hero.isAlive() 
            ? "Congrats, " + hero.getOfficialName() + " cleansed the world  of monsters."
            : "The hero died, the monsters reign over the world."
        );
    }

    private void moveButtonClicked(ActionEvent e, String direction) {
        messageLabel.setText( 
            this.model.moveHero(direction.substring(0,1))
            ? String.format("You moved %s.", direction)
            : String.format("You cannot move %s.", direction)
        );
        update();
    }

    private void attackButtonClicked(ActionEvent e) {
        this.model.battle();
        messageLabel.setText("You attacked the monster");
        update();
    }

    public void run() {
        setVisible(true);
    }
}