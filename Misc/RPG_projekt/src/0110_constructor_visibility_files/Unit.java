class Unit {
    private String name;
    private int health;
    private int damage;
    private int defense;

    public Unit(String name, int health, int damage, int defense) {
        this.name = name;
        this.health = health;
        this.damage = damage;
        this.defense = defense;
    } 

    public boolean isAlive() {
        return this.health > 0;
    }

    public void attack(Unit other) {
        int damage = this.damage > other.defense ? this.damage - other.defense : 0;
        other.health -= damage;
        if (other.health < 0) {
            other.health = 0;
        }
    }
    
    public String getDisplayText() {
        return String.format("%s (HP: %d, DMG: %d, DEF: %d)", this.name, this.health, this.damage, this.defense);
    }
}