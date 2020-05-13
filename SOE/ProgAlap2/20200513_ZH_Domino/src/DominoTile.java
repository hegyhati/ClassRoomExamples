import java.util.Random;

class InvalidDotNumberException extends Exception{}

public class DominoTile {
    private int left;
    private int right;

    public DominoTile(){
        Random rand = new Random();
        left=rand.nextInt(3)+1;
        right=rand.nextInt(3)+1;
    }

    public DominoTile(int left, int right) throws InvalidDotNumberException{
        if(left<1 || left>6 || right<1 || right>6 ) throw new InvalidDotNumberException();
        this.left=left;
        this.right=right;
    }

    public void rotate(){
        int tmp=left;
        left=right;
        right=tmp;
    }

    public boolean canConnectFromLeft(DominoTile other){
        return this.right == other.left;
    }

    public String toString(){
        return "["+left+" | "+right+"]";
    }

    public static void main(String[] args) {
        try {
            DominoTile d11=new DominoTile(1,1);
            System.out.println("[OK] [1|1] domino tile created successfully.");
            try {
                DominoTile d12=new DominoTile(1,2);
                System.out.println("[OK] [1|2] domino tile created successfully.");
                try {
                    DominoTile d17=new DominoTile(1,7);
                    System.err.println("[ERROR] [1|7] domino tile created successfully.");
                } catch (InvalidDotNumberException e){
                    System.out.println("[OK] Domino [1|7] could not be created.");
                }
                if(d11.canConnectFromLeft(d12)) System.out.println("[OK] [1|1] can connect to [1|2]");
                else System.err.println("[ERROR] [1|1] can not connect to [1|2]");
                if(!d12.canConnectFromLeft(d11)) System.out.println("[OK] [1|2] cannot connect to [1|1]");
                else System.err.println("[ERROR] [1|2] can connect to [1|1]");
                d12.rotate();
                if(!d11.canConnectFromLeft(d12)) System.out.println("[OK] [1|1] cannot connect to [2|1]");
                else System.err.println("[ERROR] [1|1] can not connect to [2|1]");
                if(d12.canConnectFromLeft(d11)) System.out.println("[OK] [2|1] ca connect to [1|1]");
                else System.err.println("[ERROR] [2|1] cannot connect to [1|1]");
            } catch (InvalidDotNumberException e){
                System.err.println("[ERROR] Domino [1|2] could not be created.");
            }
        } catch (InvalidDotNumberException e){
            System.err.println("[ERROR] Domino [1|1] could not be created.");
        }
    }

}
