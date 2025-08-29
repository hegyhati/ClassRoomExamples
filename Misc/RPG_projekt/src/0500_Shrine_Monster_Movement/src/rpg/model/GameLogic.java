package rpg.model;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

import javax.xml.parsers.*;
import org.w3c.dom.*;

public class GameLogic implements GameStateViewer{
    
    private record Position(int row, int col){
        int distanceSq(Position other) {
            return (row-other.row)*(row-other.row)+(col-other.col)*(col-other.col);
        }
        ArrayList<Position> getNeighbors(){
            return new ArrayList<>(Arrays.asList(
                new Position(row-1,col),
                new Position(row+1, col),
                new Position(row, col-1),
                new Position(row, col+1)
                ));
        }
    } 

    private final boolean[][] accessible;
    private final HashMap<Position,Monster> monsters = new HashMap<>();
    private final HashSet<Position> shrines = new HashSet<>();
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
                } else if (Character.isDigit(cell)){
                    Node monsterNode = monsterNodes.get(Integer.valueOf(String.valueOf(cell)));                        
                    monsters.put(new Position(r,c), new Monster(
                        getStringAttribute(monsterNode, "name"),
                        getIntAttribute(monsterNode, "health"),
                        getIntAttribute(monsterNode, "damage"),
                        getIntAttribute(monsterNode, "defense"),
                        getFloatAttribute(monsterNode, "initiative"),
                        getStringAttribute(monsterNode, "title")
                    ));
                } else if (cell == '*') { shrines.add(new Position(r, c)); }
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

    private void moveMonstersRandomly() {
        for (Position currentPosition : new HashSet<>(monsters.keySet())){
            if (currentPosition.equals(heroPosition)) continue;
            ArrayList <Position> possiblePositions = new ArrayList<>();
            possiblePositions.add(currentPosition);
            possiblePositions.add(currentPosition);
            possiblePositions.add(currentPosition);
            for (Position newPosition: currentPosition.getNeighbors()) {
                if (
                    accessible[newPosition.row][newPosition.col]
                    && !monsters.containsKey(newPosition)
                    && !shrines.contains(newPosition)
                    && !newPosition.equals(heroPosition)
                ) possiblePositions.add(newPosition);
            }
            Position newPosition = possiblePositions.get(ThreadLocalRandom.current().nextInt(0,possiblePositions.size()));
            if (!newPosition.equals(currentPosition)) monsters.put(newPosition,monsters.remove(currentPosition));
        }
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
        if (shrines.contains(heroPosition)) hero.healToFull();
        moveMonstersRandomly();
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
        moveMonstersRandomly();
    }

    private boolean isValidPosition(Position pos) {
        return pos.row >= 0 && pos.row < accessible.length
            && pos.col >= 0 && pos.col < accessible[0].length;
    }

    private boolean isInVisibilityRange(Position pos) {
        return hero.getVisionRangeSq() >= heroPosition.distanceSq(pos);
    }
    
    private boolean canSee(Position pos) { 
        return isValidPosition(pos) && isInVisibilityRange(pos); 
    }

    private Position getAbsolutePosition(int relRow, int relCol) {
        return new Position(heroPosition.row + relRow, heroPosition.col + relCol);
    } 

    @Override
    public boolean canSeeWall(int relRow, int relCol) {
        Position pos = getAbsolutePosition(relRow, relCol);
        return canSee(pos) && !accessible[pos.row][pos.col];
    }

    @Override
    public boolean canSeeMonster(int relRow, int relCol) {
        Position pos = getAbsolutePosition(relRow, relCol);
        return canSee(pos) && monsters.containsKey(pos);
    }

    @Override
    public boolean canSeeShrine(int relRow, int relCol) {
        Position pos = getAbsolutePosition(relRow, relCol);
        return canSee(pos) && shrines.contains(pos);
    }

    @Override
    public boolean canSee(int relRow, int relCol) {
        return canSee(getAbsolutePosition(relRow, relCol));        
    }
    
    @Override
    public int getMaxSightRange() {
        return (int) Math.sqrt(hero.getVisionRangeSq());
    }
}