package rpg.model;

import java.io.*;
import java.util.HashMap;
import javax.xml.parsers.*;
import org.w3c.dom.*;

public class GameLogic implements GameStateViewer{
    
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
    private static float getFloatAttribute(Node node, String attributeName) {
        String value = getStringAttribute(node, attributeName);
        return value == null ? 0.0f : Float.parseFloat(value);
    }

    public GameLogic(String filename) throws Exception {        

        Document document = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new File(filename));
        
        String mapString = document.getElementsByTagName("map").item(0).getTextContent().trim();
        String[] rows = mapString.split("\n");
        int height = rows.length;
        int width = rows[0].length();
        accessible = new boolean[height][width];

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
                accessible[r][c] = (cell != '#');
                if (cell == 'H' && heroNode == null) {
                    heroPosition = new Position(r,c);
                    heroNode = document.getElementsByTagName("hero").item(0);                        
                }
                else if (Character.isDigit(cell)){
                    Node monsterNode = monsterNodes.get(Integer.valueOf(String.valueOf(cell)));                        
                    monsters.put(new Position(r,c), new Monster(
                        getStringAttribute(monsterNode, "name"),
                        getIntAttribute(monsterNode, "health"),
                        getIntAttribute(monsterNode, "damage"),
                        getIntAttribute(monsterNode, "defense"),
                        getFloatAttribute(monsterNode, "initiative"),
                        getStringAttribute(monsterNode, "title")
                    ));
                }
            }
        }
        hero = new Hero(
            getStringAttribute(heroNode, "name"),
            getIntAttribute(heroNode, "health"),
            getIntAttribute(heroNode, "damage"),
            getIntAttribute(heroNode, "defense"),
            getFloatAttribute(heroNode, "initiative")
        );
    }

    @Override public Hero getHero() { return hero; }
    @Override public Monster getMonsterInFrontOfHero() { return getMonster(); }
    
    @Override
    public boolean isGameOver() {
        return monsters.isEmpty() || !hero.isAlive();
    }

    private Monster getMonster() {
        return monsters.get(heroPosition);
    }


    public boolean moveHero(String direction) {
        Monster monster = getMonster();
        if (monster != null && !hero.isFaster(monster)) monster.attack(hero);
        if (!hero.isAlive()) return false;

        Position newPosition;
        switch(direction) {
            case "n", "N" -> newPosition = new Position(heroPosition.row - 1, heroPosition.col);
            case "e", "E" -> newPosition = new Position(heroPosition.row, heroPosition.col + 1);
            case "w", "W" -> newPosition = new Position(heroPosition.row, heroPosition.col - 1);
            case "s", "S" -> newPosition = new Position(heroPosition.row + 1, heroPosition.col);
            default -> { return false; }
        }
        if (!accessible[newPosition.row][newPosition.col]) return false;
        heroPosition = newPosition;
        return true;
    }

    public void battle() {
        Monster monster = getMonster();
        if (monster == null) return;

        Unit faster, slower;
        if (hero.isFaster(monster)) {
            faster = hero;
            slower = monster; 
        } else {
            faster = monster;
            slower = hero;
        }

        faster.attack(slower);
        if (slower.isAlive()) slower.attack(faster);

        if (!monster.isAlive()) monsters.remove(heroPosition);
    }

    private boolean isValidPosition(Position pos) {
        return pos.row >= 0 && pos.row < accessible.length
            && pos.col >= 0 && pos.col < accessible[0].length;
    }

    private Position getAbsolutePosition(Position relativePos) {
        return new Position(
            heroPosition.row + relativePos.row,
            heroPosition.col + relativePos.col
        );
    } 

    @Override
    public boolean isWall(int relRow, int relCol) {
        Position pos = getAbsolutePosition(new Position(relRow, relCol));
        return !isValidPosition(pos) || !accessible[pos.row][pos.col];
    }

    @Override
    public boolean hasMonster(int relRow, int relCol) {
        Position pos = getAbsolutePosition(new Position(relRow, relCol));
        return monsters.containsKey(pos);
    }    
}