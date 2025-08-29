package rpg.model;

public interface GameStateViewer {
    public Hero getHero();
    public Monster getMonsterInFrontOfHero();    
    public boolean isGameOver();
    public boolean isWall(int relRow, int relCol);
    public boolean hasMonster(int relRow, int relCol);
}