import java.util.Random;

class BadColorException extends Exception {

}

public class MMGuess {
    private int[] colors=new int[4];

    public MMGuess(){ // TODO RANDOM
        Random rand = new Random();
        colors[0]=1+rand.nextInt(5);
        colors[1]=1+rand.nextInt(5);
        colors[2]=1+rand.nextInt(5);
        colors[3]=1+rand.nextInt(5);
    }

    public MMGuess(int first, int second, int third, int fourth) throws BadColorException {
        if(first<1 || first > 6 || second<1 || second>6 || third<1 || third>6 || fourth<1 || fourth>6 )
            throw new BadColorException();
        colors[0]=first;
        colors[1]=second;
        colors[2]=third;
        colors[3]=fourth;
    }

    public int common(MMGuess other){
        int same=0;
        for(int x=0; x<4; x++)
            if(colors[x]==other.colors[x]) same++;
        return  same;
    }

    public String toString(){
        return "("+colors[0]+" "+colors[1]+" "+colors[2]+" "+colors[3]+")";
    }
    public static void main(String[] args) {
        MMGuess guess1=new MMGuess();
        MMGuess guess2=new MMGuess();
        MMGuess guess3=new MMGuess();
        MMGuess guess4=new MMGuess();

        System.out.println("Konstruktor tesztelese...");
        try{
            guess1=new MMGuess(1,2,3,4);
            System.out.println("[OK] guess1 letrehozasa sikeres");
        } catch (BadColorException e) {
            System.out.println("[HIBA] guess1 letrehozasa nem sikeres");
        }
        try{
            guess2=new MMGuess(1,1,1,1);
            System.out.println("[OK] guess2 letrehozasa sikeres");
        } catch (BadColorException e) {
            System.out.println("[HIBA] guess2 letrehozasa nem sikeres");
        }
        try{
            guess3=new MMGuess(2,1,3,4);
            System.out.println("[OK] guess3 letrehozasa sikeres");
        } catch (BadColorException e) {
            System.out.println("[HIBA] guess3 letrehozasa nem sikeres");
        }
        try{
            guess4=new MMGuess(1,2,-3,8);
            System.out.println("[HIBA] guess4 letrehozasa sikeres");
        } catch (BadColorException e) {
            System.out.println("[OK] guess4 letrehozasa nem sikeres");
        }

        System.out.println("Osszehansonlitas tesztelese...");
        if(guess1.common(guess1)==4) System.out.println("[OK] guess1 megegyezik magaval");
        else System.out.println("[ERROR] guess1 nem egyezik meg magaval");
        if(guess2.common(guess2)==4) System.out.println("[OK] guess2 megegyezik magaval");
        else System.out.println("[ERROR] guess2 nem egyezik meg magaval");
        if(guess3.common(guess3)==4) System.out.println("[OK] guess3 megegyezik magaval");
        else System.out.println("[ERROR] guess3 nem egyezik meg magaval");

        if(guess1.common(guess2)==1) System.out.println("[OK] 1111 ~ 1234 => 1");
        else System.out.println("[ERROR] 1111 ~ 1234 => "+guess1.common(guess2));
        if(guess2.common(guess1)==1) System.out.println("[OK] 1234 ~ 1111 => 1");
        else System.out.println("[ERROR] 1234 ~ 1111 => "+guess2.common(guess1));
        if(guess1.common(guess3)==2) System.out.println("[OK] 1111 ~ 2134 => 2");
        else System.out.println("[ERROR] 1111 ~ 2134 => "+guess1.common(guess3));

    }

}
