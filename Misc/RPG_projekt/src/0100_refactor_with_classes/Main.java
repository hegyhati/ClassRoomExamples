class Unit {
    String name;
    int health;
    int damage;
    int defense;

    boolean isAlive() {
        return health > 0;
    }

    void attack(Unit other) {
        int realdamage = damage > other.defense ? damage - other.defense : 0;
        other.health -= realdamage;
        if (other.health < 0) {
            other.health = 0;
        }
    }

    String getDisplayText() {
        return String.format("%s (HP: %d, DMG: %d, DEF:%d)", name, health, damage, defense);
    }
}

class Main {

    static void printStatus(Unit unit1, Unit unit2) {
        System.out.printf("%s vs. %s\n", unit1.getDisplayText(), unit2.getDisplayText());
    }
   
    public static void main(String[] args) {

        Unit hero = new Unit();
        hero.name = "Hero";
        hero.health = 10;
        hero.damage = 1;
        hero.defense = 1;
        Unit monster = new Unit();
        monster.name = "Monster";
        monster.health = 5;
        monster.damage = 2;
        monster.defense = 0;
        
        printStatus(hero, monster);

        for (int turn = 0; hero.isAlive() && monster.isAlive() ; turn += 1) {
            if (turn % 2 == 0) {
                System.out.printf("%s attacks %s...\n", hero.getDisplayText(), monster.getDisplayText());
                hero.attack(monster);
            } else {
                System.out.printf("%s attacks %s...\n", monster.getDisplayText(), hero.getDisplayText());
                monster.attack(hero);
            }
        }

        if (hero.isAlive()) {
            System.out.println("The hero won the battle \\o/");
        } else {
            System.out.println("The hero lost the battle :-(");
        }
    }
}
