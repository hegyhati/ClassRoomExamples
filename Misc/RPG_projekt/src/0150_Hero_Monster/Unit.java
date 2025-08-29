class Unit {
    private final boolean  hero;
    private String title = "";
    final public String name;
    private int health;
    private int damage;
    private int defense;
    private int experience = 0;


    public Unit(String name, int health, int damage, int defense, boolean hero) {
        this.name = name;
        this.health = health;
        this.damage = damage;
        this.defense = defense;
        this.hero = hero;
    } 

    public void setTitle(String newTitle) {
        if (this.hero) this.title = newTitle;
    }

    public String getOfficialName() {
        return this.title.equals("") ? this.name : this.name + ", the " + this.title;
    }

    public int getHealth() {
        return this.health;
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
        if (this.hero) gainExperience();
    }

    private void gainExperience() {
        this.experience++;
        if (this.experience % 10 == 0) levelUp();
    }

    private void levelUp() {
        this.damage++;
        this.defense++;
        this.health *= 1.5;
    }
    
    @Override
    public String toString() {
        return String.format("%s (HP: %d, DMG: %d, DEF: %d)", this.name, this.health, this.damage, this.defense);
    }
}