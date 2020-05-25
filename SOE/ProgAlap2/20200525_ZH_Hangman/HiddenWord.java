import java.util.ArrayList;

public class HiddenWord {
  private final String word;
  private boolean[] revealed;

  public HiddenWord(String word){
    this.word = word.toUpperCase();
    this.revealed = new boolean[word.length()];
    for(int pos=0; pos<word.length();++pos)
      if (this.word.charAt(pos)<'A' || this.word.charAt(pos)>'Z') 
        revealed[pos]=true;
  }

  public ArrayList<Integer> reveal(char character) {
    ArrayList<Integer> positions = new ArrayList<Integer>();
    for(int pos=0; pos<word.length(); ++pos) {
      if(word.charAt(pos)==character) {
        positions.add(pos);
        revealed[pos]=true;
      }
    }
    return positions;
  }

  public String toString() {
    StringBuilder toReturn = new StringBuilder();
    for (int pos = 0; pos < word.length(); ++pos) {
      if (revealed[pos]) toReturn.append(word.charAt(pos));
      else toReturn.append("_");
    }
    return toReturn.toString();
  }

  public boolean isRevealed(){
    for(int pos=0; pos<word.length(); ++pos) 
      if(!revealed[pos]) return false;
    return true;
  }

  public static void main(String[] args) {
    HiddenWord test= new HiddenWord("Rickroll");

    System.out.println(test);
    if (test.toString().equals("________")) System.out.println("[OK] Correct starting clue");
    else System.err.println("[ERROR] Incorrect starting clue");

    ArrayList<Integer> response;

    response=test.reveal('R');
    if(response.size()==2) System.out.println("[OK] Found correct number of matches for R");
    else System.err.println("[ERROR] Found incorrect number of matches for R");

    System.out.println(test);
    if (test.toString().equals("R___R___")) System.out.println("[OK] Correct clue after R");
    else System.err.println("[ERROR] Incorrect clue after R");

    response=test.reveal('A');
    if(response.size()==0) System.out.println("[OK] Found correct number of matches for A");
    else System.err.println("[ERROR] Found incorrect number of matches for A");

    System.out.println(test);
    if (test.toString().equals("R___R___")) System.out.println("[OK] Correct clue after R and A");
    else System.err.println("[ERROR] Incorrect clue after R and A");

    response=test.reveal('L');
    if(response.size()==2) System.out.println("[OK] Found correct number of matches for L");
    else System.err.println("[ERROR] Found incorrect number of matches for L");

    System.out.println(test);
    if (test.toString().equals("R___R_LL")) System.out.println("[OK] Correct clue after R,A, and L");
    else System.err.println("[ERROR] Incorrect clue after R,A, and L");
  }
}
