
class Main {

    static int hpAfterAttack(int defenderHP, int attackerDMG, int defenderDEF) {
        int damage = attackerDMG > defenderDEF ? attackerDMG - defenderDEF : 0;
        return damage < defenderHP ? defenderHP - damage : 0;
    }

    static String unitDisplayText(String name, int DMG, int HP, int DEF) {
        return String.format("%s (DMG: %d, HP: %d, DEF: %d)", name, DMG, HP, DEF);
    }

    static void printStatus(int heroHP, int heroDMG, int heroDEF, int monsterHP, int monsterDMG, int monsterDEF) {
        System.out.printf("%s vs. %s\n", unitDisplayText("Hero", heroDMG, heroHP, heroDEF), unitDisplayText("Monster", monsterDMG, monsterHP, monsterDEF));
    }

    public static void main(String[] args) {

        int heroHP = 8;
        int heroDMG = 1;
        int heroDEF = 1;
        int monsterHP = 5;
        int monsterDMG = 2;
        int monsterDEF = 0;
        
        printStatus(heroHP, heroDMG, heroDEF, monsterHP, monsterDMG, monsterDEF);

        while (true) {
            System.out.println("The hero attacks the monster...");
            monsterHP = hpAfterAttack(monsterHP, heroDMG, monsterDEF);
            printStatus(heroHP, heroDMG, heroDEF, monsterHP, monsterDMG, monsterDEF);
            if (monsterHP == 0) {
                System.out.println("The hero won the battle \\o/");
                break;
            }
            System.out.println("The monster attacks the hero...");
            heroHP = hpAfterAttack(heroHP, monsterDMG, heroDEF);
            printStatus(heroHP, heroDMG, heroDEF, monsterHP, monsterDMG, monsterDEF);
            if (heroHP == 0) {
                System.out.println("The hero lost the battle :-(");
                break;
            }
        }
    }
}
