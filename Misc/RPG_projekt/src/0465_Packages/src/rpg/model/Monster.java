package rpg.model;

class Monster extends Unit implements MonsterViewer {

    private String title;

    public Monster(String name, int health, int damage, int defense, float initiative) {
        this(name, health, damage, defense, initiative, null);
    }

    public Monster(String name, int health, int damage, int defense, float initiative, String title) {
        super(name, health, damage, defense, initiative);
        this.title = title;
    }

    public String fetchTitle() {
        if ( !isAlive() && this.title != null) {
            String tmp = title;
            this.title = null;
            return tmp;
        } else return null;
    }
}