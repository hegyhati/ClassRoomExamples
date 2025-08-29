class Hero {
    private Unit base;
    private String title = "";
    private int experience = 0;

    public Hero(String name, int health, int damage, int defense) {
        this.base = new Unit(name, health, damage, defense);
    } 

    public int getHealth() { return this.base.getHealth(); }
    public boolean isAlive() { return this.base.isAlive(); }
    public void takeDamage(int damage) { this.base.takeDamage(damage); }
    @Override
    public String toString() { return this.base.toString(); }

    public void setTitle(String newTitle) {
        this.title = newTitle;
    }

    public String getOfficialName() {
        return this.title.equals("") ? this.base.name : this.base.name + ", the " + this.title;
    }

    public void attack(Monster monster) {
        monster.takeDamage(this.base.damage);
        gainExperience();
    }

    private void gainExperience() {
        this.experience++;
        if (this.experience % 10 == 0) levelUp();
    }

    private void levelUp() {
        this.base.damage++;
        this.base.defense++;
        this.base.health *= 1.5;
    }    
}