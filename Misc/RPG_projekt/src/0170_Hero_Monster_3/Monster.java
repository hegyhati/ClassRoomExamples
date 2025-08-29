
class Monster {
    Unit base;

    public Monster(String name, int health, int damage, int defense) {
        this.base = new Unit(name,health, damage, defense);
    } 

    public int getHealth() { return this.base.getHealth(); }
    public boolean isAlive() { return this.base.isAlive(); }
    public void takeDamage(int damage) { this.base.takeDamage(damage); }
    @Override
    public String toString() { return this.base.toString(); }

    public void attack(Hero hero) {
        hero.takeDamage(this.base.damage);
    }    
}