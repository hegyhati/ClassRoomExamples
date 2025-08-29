import java.io.*;
import java.util.HashMap;
import javax.xml.parsers.*;
import org.w3c.dom.*;

class GameLogic {
    
    private record Position(int row, int col){} 

    private final boolean[][] accessible;
    private final HashMap<Position,Monster> monsters = new HashMap<>();
    private final Hero hero;
    private Position heroPosition;

    private static String getStringAttribute(Node node, String attributeName) {
        Node attribute = node.getAttributes().getNamedItem(attributeName);
        return attribute == null ? null : attribute.getNodeValue();
    }
    private static int getIntAttribute(Node node, String attributeName) {
        String value = getStringAttribute(node, attributeName);
        return value == null ? 0 : Integer.parseInt(value);
    }

    public GameLogic(String filename) throws Exception {        

        Document document = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new File(filename));
        
        String mapString = document.getElementsByTagName("map").item(0).getTextContent().trim();
        String[] rows = mapString.split("\n");
        int height = rows.length;
        int width = rows[0].length();
        this.accessible = new boolean[height][width];

        HashMap <Integer,Node> monsterNodes = new HashMap<Integer,Node>();
        NodeList monstersNodeList = document.getElementsByTagName("monster");
        for (int i=0; i<monstersNodeList.getLength(); ++i) {
            Node monsterNode = monstersNodeList.item(i);            
            monsterNodes.put(getIntAttribute(monsterNode, "type"), monsterNode);
        }

        Node heroNode = null;
        for (int r = 0 ; r < height ; ++r) {
            for (int c = 0 ; c < width ; ++c) {
                char cell = rows[r].charAt(c);
                this.accessible[r][c] = (cell != '#');
                if (cell == 'H' && heroNode == null) {
                    this.heroPosition = new Position(r,c);
                    heroNode = document.getElementsByTagName("hero").item(0);                        
                }
                else if (Character.isDigit(cell)){
                    Node monsterNode = monsterNodes.get(Integer.valueOf(String.valueOf(cell)));                        
                    this.monsters.put(new Position(r,c), new Monster(
                        getStringAttribute(monsterNode, "name"),
                        getIntAttribute(monsterNode, "health"),
                        getIntAttribute(monsterNode, "damage"),
                        getIntAttribute(monsterNode, "defense"),
                        getStringAttribute(monsterNode, "title")
                    ));
                }
            }
        }
        this.hero = new Hero(
            getStringAttribute(heroNode, "name"),
            getIntAttribute(heroNode, "health"),
            getIntAttribute(heroNode, "damage"),
            getIntAttribute(heroNode, "defense")
        );
    }

    public Hero getHero() { return this.hero; }
    
    public boolean isGameOver() {
        return this.monsters.isEmpty() || !this.hero.isAlive();
    }

    public Monster getMonsterInFrontOfHero() {
        return this.monsters.get(this.heroPosition);
    }

    boolean moveHero(String direction) {
        Position newPosition;
        switch(direction) {
            case "n", "N" -> newPosition = new Position(this.heroPosition.row - 1, this.heroPosition.col);
            case "e", "E" -> newPosition = new Position(this.heroPosition.row, this.heroPosition.col + 1);
            case "w", "W" -> newPosition = new Position(this.heroPosition.row, this.heroPosition.col - 1);
            case "s", "S" -> newPosition = new Position(this.heroPosition.row + 1, this.heroPosition.col);
            default -> { return false; }
        }
        if (!this.accessible[newPosition.row][newPosition.col]) return false;
        this.heroPosition = newPosition;
        return true;
    }

    void attack() {
        Monster monster = getMonsterInFrontOfHero();
        if (monster == null) return;
        this.hero.attack(monster);
        if (monster.isAlive()) monster.attack(hero);
        else this.monsters.remove(this.heroPosition);
    }
}