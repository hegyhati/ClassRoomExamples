class Monster {
    final public String name;
    private int health;
    private final int damage;
    private final int defense;

    public Monster(String name, int health, int damage, int defense) {
        this.name = name;
        this.health = health;
        this.damage = damage;
        this.defense = defense;
    } 

    public int getHealth() {
        return this.health;
    }

    public boolean isAlive() {
        return this.health > 0;
    }

    public void attack(Hero hero) {
        hero.takeDamage(this.damage);
    }

    public void takeDamage(int damage) {
        damage -= this.defense;
        if (damage > 0) {
            this.health -= damage;
            if (this.health < 0) this.health = 0;
        }
    }
    
    @Override
    public String toString() {
        return String.format("%s (HP: %d, DMG: %d, DEF: %d)", this.name, this.health, this.damage, this.defense);
    }
}