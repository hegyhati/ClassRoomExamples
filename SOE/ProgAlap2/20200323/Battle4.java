import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Scanner;

class Warrior {
    protected int HP;
    protected int DMG;
    protected String name;

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

class ShieldWarrior extends Warrior {
    boolean indefense;
    ShieldWarrior(String name, int initial_health, int damage) {
        super(name,initial_health,damage);
        indefense=true;
    }
    public void takeDamage(Warrior attacker){
        if(!indefense){
            HP -= attacker.DMG;
            if(HP<0) HP=0;
        }
        indefense=!indefense;
    }
}

class Army{
    private String name;
    private ArrayList<Warrior> warriors;

    public Army(String name, String fileName, boolean shielded){
        this.name=name;
        warriors=new ArrayList<Warrior>();
        try {
            Scanner sc=new Scanner(new File(fileName));
            while(sc.hasNextLine()){
                if (!shielded) warriors.add(new Warrior(sc.next(),sc.nextInt(),sc.nextInt())); 
                else warriors.add(new ShieldWarrior(sc.next(),sc.nextInt(),sc.nextInt())); 
            }
                
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("Could not read army data from "+fileName);
        } catch (NoSuchElementException e) {}

    }

    public String toString(){
        StringBuilder toReturn=new StringBuilder("Warriors in the "+name+" army:\n");
        for(Warrior warrior: warriors)
            toReturn.append("\t"+warrior+"\n");
        return toReturn.toString();
    }

    public Warrior getFrontWarrior(){ 
        if(warriors.isEmpty()) return null;
        else return warriors.get(0);
    }

    public void buryDead(){
        if(warriors.isEmpty()) return;
        else if (!warriors.get(0).isAlive()) warriors.remove(0);
    }

    public static Army fight(Army a1, Army a2){
        while(!a1.warriors.isEmpty() && !a2.warriors.isEmpty()){
            a1.getFrontWarrior().takeDamage(a2.getFrontWarrior());
            a2.getFrontWarrior().takeDamage(a1.getFrontWarrior());
            a1.buryDead();
            a2.buryDead();
        }
        if(!a1.warriors.isEmpty()) return a1;
        else if(!a2.warriors.isEmpty()) return a2;
        else return null;
    }

}



public class Battle4{
    public static void main(String[] args) {
        Army good=new Army("Wizard","Wizard.txt",false);
        Army evil=new Army("Necromancer", "Necromancer.txt",true);
        System.out.println(good+""+evil);
        Army winner=Army.fight(good, evil);
        if(winner!=null) System.out.println("The victorious army is: "+winner);
        else System.out.println("The two armies annihilated each other.");
    }
}
