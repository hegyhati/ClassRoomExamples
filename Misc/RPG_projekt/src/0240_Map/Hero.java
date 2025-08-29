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

    private void addTitle(String newTitle) {
        if (newTitle != null) this.title += ", the " + newTitle;
    }

    public String getOfficialName() {
        return this.name + this.title;
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