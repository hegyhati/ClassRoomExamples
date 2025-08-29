class Hero extends Unit {
    private String title = "";
    private int experience = 0;
    private int maxHealth;

    public Hero(String name, int health, int damage, int defense) {
        super(name, health, damage, defense);
        this.maxHealth = health;
    } 

    public void heal(int points) {
        if (isAlive()) {
            this.health += points;
            if (this.health > this.maxHealth) 
                this.health = this.maxHealth;
        }
    }

    public void healToFull() {
        if (isAlive()) this.health = this.maxHealth;
    }

    public void setTitle(String newTitle) {
        this.title = newTitle;
    }

    public String getOfficialName() {
        return this.title.equals("") ? this.name : this.name + ", the " + this.title;
    }

    @Override
    public void attack(Unit other) {
        super.attack(other);
        gainExperience();
    }

    private void gainExperience() {
        this.experience++;
        if (this.experience % 10 == 0) levelUp();
    }

    private void levelUp() {
        this.damage++;
        this.defense++;
        this.maxHealth += 10;
        healToFull();
    }    
}