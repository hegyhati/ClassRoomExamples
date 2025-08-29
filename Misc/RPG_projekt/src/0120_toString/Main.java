
class Main {

   private static void printStatus(Unit unit1, Unit unit2) {
        System.out.printf("%s vs. %s\n", unit1, unit2);
    }
   
    public static void main(String[] args) {

        Unit hero = new Unit("Bilbo", 10, 1, 1);
        Unit monster = new Unit("Cavetroll", 40, 5, 0);
        
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
            System.out.println("The hero won the battle \\o/");
        } else {
            System.out.println("The hero lost the battle :-(");
        }
    }
}
