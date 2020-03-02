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

    public void takeDamage(Warrior attacker){
        HP -= attacker.DMG;
        if(HP<0) HP=0;
    }

    public boolean isAlive(){
        return HP>0;
    }

}

public class Battle2{
    public static void main(String[] args) {
        Warrior halfling = new Warrior("Halfling",3,2);
        Warrior mage = new Warrior("Mage",30,8);
        System.out.println("Attacker: "+halfling);
        System.out.println("Defender: "+mage);
        while(mage.isAlive()){
            System.out.print("ATTACK! ");
            mage.takeDamage(halfling);
            System.out.println("Defender: "+mage);
        }
        System.out.println("Defender dead.");
    }
}
