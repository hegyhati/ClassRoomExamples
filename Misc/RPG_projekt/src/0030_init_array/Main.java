class Main {

    static String unitDisplayText(String name, int[] unitData) {
        return String.format("%s (HP: %d, DMG: %d, DEF: %d)", name, unitData[0], unitData[1], unitData[2]);
    }

    static void printStatus(int[] heroData, int[] monsterData) {
        System.out.printf("%s vs. %s\n", unitDisplayText("Hero", heroData), unitDisplayText("Monster", monsterData));
    }

    static void attack(int[] attacker, int[] defender) {        
        int damage = attacker[1] > defender[2] ? attacker[1] - defender[2] : 0;
        defender[0] -= damage;
        if (defender[0] < 0) {
            defender[0] = 0;
        }
    }

    static boolean isAlive(int[] unit) {
        return unit[0] > 0;
    }

    public static void main(String[] args) {

        // Always HP first, DMG second, DEF third.
        int[] heroData = {8, 1, 1};
        int[] monsterData = {5, 2, 0};

        printStatus(heroData, monsterData);

        
        for (int turn = 0; isAlive(heroData) && isAlive(monsterData) ; turn += 1) {
            if (turn % 2 == 0) {
                System.out.println("The hero attacks the monster...");
                attack(heroData, monsterData);
            } else {
                System.out.println("The monster attacks the hero...");
                attack(monsterData, heroData);
            }
            printStatus(heroData, monsterData);
        }

        if (isAlive(heroData)) {
            System.out.println("The hero won the battle \\o/");
        } else {
            System.out.println("The hero lost the battle :-(");
        }
    }
}
