
class Main {

   private static void printStatus(Unit unit1, Unit unit2) {
        System.out.printf("%s vs. %s\n", unit1, unit2);
    }
   
    public static void main(String[] args) {

        Unit hero = new Unit("Bilbo", 80, 1, 1, true);
        Unit monster = new Unit("Cavetroll", 100, 5, 0, false);
        
        printStatus(hero, monster);

        for (int turn = 0; hero.isAlive() && monster.isAlive() ; turn += 1) {
            if (turn % 2 == 0) {
                System.out.printf("%s attacks %s...\n", hero, monster);
                hero.attack(monster);
            } else {
                System.out.printf("%s attacks %s...\n", monster, hero);
                monster.attack(hero);
            }
        }

        if (hero.isAlive()) {
            hero.setTitle("slayer of trolls");
            System.out.printf("%s won the battle, and should be called henceforth as %s.\n", hero.name, hero.getOfficialName());
        } else {
            System.out.printf("The hero lost the battle :-(\n");
        }
    }
}
