class Unit implements UnitViewer {
    final protected String name;
    protected  int health;
    protected  int damage;
    protected  int defense;

    public Unit(String name, int health, int damage, int defense){
        this.name = name;
        this.health = health;
        this.damage = damage;
        this.defense = defense;
    } 

    @Override public String getName() { return this.name; }
    @Override public int getHealth() { return this.health; }
    @Override public int getDamage() { return this.damage; }
    @Override public int getDefense() { return this.defense; }
    
    @Override
    public boolean isAlive() {
        return this.health > 0;
    }

    public void attack(Unit unit) {
        unit.takeDamage(this.damage);
    }

    protected void takeDamage(int damage) {
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