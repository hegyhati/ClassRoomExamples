package rpg.model;

public class Hero extends Unit {
    private String title = "";
    private int experience = 0;
    private int maxHealth;

    Hero(String name, int health, int damage, int defense, float initiative) {
        super(name, health, damage, defense, initiative);
        maxHealth = health;
    } 

    public int getExperience() { return experience; }
    public int maxHealth() { return maxHealth; }

    public String getOfficialName() { 
        return name + title; 
    }

    void heal(int points) {
        if (isAlive()) {
            health += points;
            if (health > maxHealth) 
                health = maxHealth;
        }
    }

    void healToFull() {
        if (isAlive()) health = maxHealth;
    }

    private void addTitle(String newTitle) {
        if (newTitle != null) title += ", the " + newTitle;
    }

    @Override
    public void attack(Unit other) {
        super.attack(other);
        gainExperience();
        if (!other.isAlive() && other instanceof Monster) {
            addTitle(((Monster) other).fetchTitle());
        }
    }

    private void gainExperience() {
        experience++;
        if (experience % 10 == 0) levelUp();
    }

    private void levelUp() {
        damage++;
        defense++;
        maxHealth += 10;
        healToFull();
        initiative *= 1.1;
    }    

}