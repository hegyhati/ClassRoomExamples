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

    public String getName() { return name; }
    public int getHealth() { return health; }
    public int getDamage() { return damage; }
    public int getDefense() { return defense; }
    
    public boolean isAlive() {
        return health > 0;
    }

    boolean isFaster(Unit other) {
        return initiative >= other.initiative;
    }

    void attack(Unit unit) {
        unit.takeDamage(damage);
    }

    private int calculateDamage(int originalDamage) {
        int max = originalDamage - defense;
        if (max < 0) return 0;
        int min = (int) Math.ceil(max*0.8);
        return ThreadLocalRandom.current().nextInt(min, max+1);
    }

    protected void takeDamage(int damage) {
        health -= calculateDamage(damage);
        if (health < 0) health = 0;
    }
    
    @Override
    public String toString() {
        return String.format("%s (HP: %d, DMG: %d, DEF: %d)", name, health, damage, defense);
    }
}