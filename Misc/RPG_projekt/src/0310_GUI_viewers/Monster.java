class Monster extends Unit implements MonsterViewer {

    private String title;

    public Monster(String name, int health, int damage, int defense) {
        this(name, health, damage, defense,null);
    }

    public Monster(String name, int health, int damage, int defense, String title) {
        super(name, health, damage, defense);
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