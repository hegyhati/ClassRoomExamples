package rpg.model;

import java.util.concurrent.ThreadLocalRandom;

public class Unit {
    final protected String name;
    protected  int health;
    protected  int damage;
    protected  int defense;
    protected float initiative;

    Unit(String name, int health, int damage, int defense, float initiative){
        this.name = name;
        this.health = health;
        this.damage = damage;
        this.defense = defense;
        this.initiative = initiative;
    } 

    public String getName() { return this.name; }
    public int getHealth() { return this.health; }
    public int getDamage() { return this.damage; }
    public int getDefense() { return this.defense; }
    
    public boolean isAlive() {
        return this.health > 0;
    }

    boolean isFaster(Unit other) {
        return this.initiative >= other.initiative;
    }

    void attack(Unit unit) {
        unit.takeDamage(this.damage);
    }

    private int calculateDamage(int originalDamage) {
        int max = originalDamage - this.defense;
        if (max < 0) return 0;
        int min = (int) Math.ceil(max*0.8);
        return ThreadLocalRandom.current().nextInt(min, max+1);
    }

    protected void takeDamage(int damage) {
        this.health -= calculateDamage(damage);
        if (this.health < 0) this.health = 0;
    }
    
    @Override
    public String toString() {
        return String.format("%s (HP: %d, DMG: %d, DEF: %d)", this.name, this.health, this.damage, this.defense);
    }
}