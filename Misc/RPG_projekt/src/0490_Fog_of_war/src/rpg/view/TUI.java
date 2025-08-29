package rpg.view;

import rpg.model.*;

import java.util.Scanner;

class TUI {
    private final GameLogic model;
    private final Scanner scanner = new Scanner(System.in);

    private void print(Object... text) { for (Object s : text) System.out.print(s); }

    public TUI(GameLogic model) {
        this.model = model;
        print("Welcome to the game!\n\n");
    }

    public TUI(String mapFileName) throws Exception {
        this(new GameLogic(mapFileName));
    }

    private void printState() {
        print("\n\n", model.getHero(), "\n");
        Monster monster = model.getMonsterInFrontOfHero();
        if (monster != null) print("There is a monster in front of you: ", monster, "\n");
        else print("There is nothing in front of you.\n");
    }

    private void nextStep(){
        print("Attack(A) or move(N/E/W/S)? ");
        String command = scanner.next();
        switch (command) {
            case "n", "N", "e", "E", "w", "W", "s", "S" -> {
                if (!model.moveHero(command)) print("You cannot move there.\n");
            }
            case "a", "A" -> model.battle();
            default -> print("Unknown command, use N/E/W/S or A.\n");
        }
    }

    public void run() {
        printState();
        while (!model.isGameOver()) {
            nextStep();
            printState();
        }
        if (model.getHero().isAlive()) print("The hero cleansed the world of monsters!\n");
        else print("The hero died, the monsters reign over the world.\n");
    }
}