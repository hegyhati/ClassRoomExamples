package rpg.model;

public interface GameStateViewer {
    public Hero getHero();
    public Monster getMonsterInFrontOfHero();    
    public boolean isGameOver();
    public boolean canSeeWall(int relRow, int relCol);
    public boolean canSeeMonster(int relRow, int relCol);
    public boolean canSee(int relRow, int relCol);
}