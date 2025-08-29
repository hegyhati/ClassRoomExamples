
class Main {

    static int hpAfterAttack(int currentHP, int attackerDMG) {
        if (attackerDMG >= currentHP) {
            return 0;
        } else {
            return currentHP - attackerDMG;
        }
    }

    static String unitDisplayText(String name, int DMG, int HP) {
        return String.format("%s (DMG: %d, HP: %d)", name, DMG, HP);
    }

    static void printStatus(int heroHP, int heroDMG, int monsterHP, int monsterDMG) {
        System.out.printf("%s vs. %s\n", unitDisplayText("Hero", heroDMG, heroHP), unitDisplayText("Monster", monsterDMG, monsterHP));
    }

    public static void main(String[] args) {

        int heroHP = 8;
        int heroDMG = 1;
        int monsterHP = 5;
        int monsterDMG = 2;
        
        printStatus(heroHP, heroDMG, monsterHP, monsterDMG);

        while (true) {
            System.out.println("The hero attacks the monster...");
            monsterHP = hpAfterAttack(monsterHP, heroDMG);
            printStatus(heroHP, heroDMG, monsterHP, monsterDMG);
            if (monsterHP == 0) {
                System.out.println("The hero won the battle \\o/");
                break;
            }
            System.out.println("The monster attacks the hero...");
            heroHP = hpAfterAttack(heroHP, monsterDMG);
            printStatus(heroHP, heroDMG, monsterHP, monsterDMG);
            if (heroHP == 0) {
                System.out.println("The hero lost the battle :-(");
                break;
            }
        }
    }
}
