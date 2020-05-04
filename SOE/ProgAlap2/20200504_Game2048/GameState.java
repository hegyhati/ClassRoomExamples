import java.util.Random;

class GameOverException extends Exception {

}

public class GameState {
    private int[][] field = new int[4][4];

    public GameState(){
        reset();
    }

    public void reset(){
        for(int r=0; r<4; r++) {
            for (int c = 0; c < 4; c++) {
                field[r][c] = 0;
            }
        }
        try { insertNewRandom(); }
        catch (GameOverException e){}
    }
    String getField(int row, int column){
        if(field[row][column]==0) return "   ";
        else return " "+field[row][column]+" ";
    }
    public boolean isGameOver(){
        for (int row = 0; row < 4; row++) {
            for (int column = 0; column < 4; column++) {
                if (field[row][column]==0) return false;
            }
        }
        return true;
    }
    private void insertNewRandom() throws GameOverException{
        if(!isGameOver()) {
            Random rand = new Random();
            int row, column;
            do {
                row = rand.nextInt(4);
                column = rand.nextInt(4);
            } while (field[row][column] != 0);
            field[row][column] = (rand.nextInt(2)+1)*2;
        } else throw new GameOverException();
    }
    private void checkMergeMove(int r1, int c1, int r2, int c2){ // 2 -> 1
        if(field[r1][c1]==0) {
            field[r1][c1]=field[r2][c2];
            field[r2][c2]=0;
        } else if (field[r1][c1]==field[r2][c2]){
            field[r1][c1]+=field[r2][c2];
            field[r2][c2]=0;
        }

    }

    public void right() throws GameOverException{
        for (int row = 0; row < 4; row++) {
            for (int meh = 0; meh < 3; meh++) {
                for (int column = 3; column > 0 ; column--) {
                    checkMergeMove(row,column,row, column-1);
                }
            }
        }
        insertNewRandom();
    }
    public void left() throws GameOverException{
        for (int row = 0; row < 4; row++) {
            for (int meh = 0; meh < 3; meh++) {
                for (int column = 0; column < 3 ; column++) {
                    checkMergeMove(row,column,row, column+1);
                }
            }
        }
        insertNewRandom();
    }
    public void up() throws GameOverException{
        for (int column = 0; column < 4; column++) {
            for (int meh = 0; meh < 3; meh++) {
                for (int row = 0; row < 3 ; row ++) {
                    checkMergeMove(row,column,row+1, column);
                }
            }
        }
        insertNewRandom();
    }
    public void down() throws GameOverException{
        for (int column = 0; column < 4; column++) {
            for (int meh = 0; meh < 3; meh++) {
                for (int row = 3; row > 0 ; row --) {
                    checkMergeMove(row,column,row-1, column);
                }
            }
        }
        insertNewRandom();
    }
}