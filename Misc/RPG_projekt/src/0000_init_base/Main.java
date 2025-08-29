
class Main {

    public static void main(String[] args) {

        int heroHP = 8;
        int heroDMG = 1;
        int monsterHP = 5;
        int monsterDMG = 2;

        System.out.printf("Hero (DMG: %d, HP: %d) vs. Monster (DMG: %d, HP: %d)\n", heroDMG, heroHP, monsterDMG, monsterHP);

        while (true) {
            System.out.println("The hero attacks the monster...");
            monsterHP -= heroDMG;
            if (monsterHP < 0) {
                monsterHP = 0;
            }
            System.out.printf("Hero (DMG: %d, HP: %d) vs. Monster (DMG: %d, HP: %d)\n", heroDMG, heroHP, monsterDMG, monsterHP);
            if (monsterHP == 0) {
                System.out.println("The hero won the battle \\o/");
                break;
            }
            System.out.println("The monster attacks the hero...");
            heroHP -= monsterDMG;
            if (heroHP < 0) {
                heroHP = 0;
            }
            System.out.printf("Hero (DMG: %d, HP: %d) vs. Monster (DMG: %d, HP: %d)\n", heroDMG, heroHP, monsterDMG, monsterHP);
            if (heroHP == 0) {
                System.out.println("The hero lost the battle :-(");
                break;
            }
        }
    }
}
