import java.util.Arrays;
import java.util.Collections;
import java.util.Random;

public class Country {
    private int soldiers;
    private int reinforcments;
    static Random rand = new Random();

    public Country(int initial_soldiers, int reinforcments){
        this.soldiers = initial_soldiers;
        this.reinforcments=reinforcments;
    }

    public void reinforcments(){
        if(this.soldiers >= this.reinforcments)
            this.soldiers+=this.reinforcments;
    }

    private Integer[] sortedRoll(int count){
        Integer[] rolls=new Integer[count];
        for(int i=0;i<count;i++)
            rolls[i]=rand.nextInt(6)+1;
        Arrays.sort(rolls, Collections.reverseOrder());
        return rolls;
    }
    private String dices(Integer[] rolls){
        String toReturn=" ";
        for(int i=0; i<rolls.length; i++)
            toReturn += Character.toString(0x267F + rolls[i]) + " ";
        return toReturn;
    }

    public String attack (Country defender) {
        StringBuilder report = new StringBuilder();
        final int attackers = (soldiers>=4) ? 3 : soldiers-1;
        final int defenders = (defender.soldiers >= 2) ? 2 : defender.soldiers;
        Integer[] attackRolls = sortedRoll(attackers);
        Integer[] defendRolls = sortedRoll(defenders);

        report.append(attackers).append(" soldiers attack with: ").append(dices(attackRolls)).append("\n");
        report.append(defenders).append(" soldiers defend with: ").append(dices(defendRolls)).append("\n");

        for(int i=0; i<Math.min(attackers,defenders); i++)
            if(attackRolls[i]>defendRolls[i]) defender.soldiers--;
            else soldiers--;

        return report.toString();        
    }

    public String toString(){
        return String.valueOf(soldiers) + " soldiers";
    }

    public boolean isDefeated(){
        return soldiers==0;
    }
    public boolean canAttack(){
        return soldiers>1;
    }
}
