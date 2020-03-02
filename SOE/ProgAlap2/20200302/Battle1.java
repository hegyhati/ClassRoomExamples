class Warrior {
    private int HP;
    private int DMG;
    private String name;

    Warrior(String name, int initial_health, int damage){
        this.name=name;
        HP=initial_health;
        DMG=damage;
    }

    public String toString(){
        return name + " (HP:"+HP+",DMG:"+DMG+")";
    }

}

public class Battle1{
    public static void main(String[] args) {
        Warrior halfling = new Warrior("Halfling",3,2);
        Warrior boar = new Warrior("Boar",15,3);
        System.out.println(halfling);
        System.out.println(boar);
    }
}
