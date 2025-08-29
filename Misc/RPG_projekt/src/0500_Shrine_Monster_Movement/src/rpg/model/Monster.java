package rpg.model;

public class Monster extends Unit{

    private String title;

    Monster(String name, int health, int damage, int defense, float initiative) {
        this(name, health, damage, defense, initiative, null);
    }

    Monster(String name, int health, int damage, int defense, float initiative, String title) {
        super(name, health, damage, defense, initiative);
        this.title = title;
    }

    String fetchTitle() {
        if ( !isAlive() && title != null) {
            String tmp = title;
            title = null;
            return tmp;
        } else return null;
    }
}