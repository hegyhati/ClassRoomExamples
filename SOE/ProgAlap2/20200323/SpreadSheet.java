class Cell {
    public String display(int width){   
            return spaces(width);
    }
    static String chars(int width, char c){
        StringBuilder s=new StringBuilder();
        for(int i=0;i<width;++i) s.append(c);
        return s.toString();
    }
    public static String spaces(int width){
        return chars(width,' ');
    }
    protected String toolong(int width){
        return chars(width,'#');
    }
}
class NumberCell extends Cell{
    int number;
    NumberCell(int number){this.number=number;}
    private int digits(){
        int digits=0;
        for(int tmp=number;tmp>0;tmp/=10) digits++;
        return digits;
    }
    public String display(int width){
        if(digits()<=width){
            return spaces(width-digits())+number;
        } else {
            return toolong(width);
        }
    }
}
class TextCell extends Cell{
    String text;
    TextCell(String text){this.text=text;}
    public String display(int width){
        if (text.length()<=width){
            return text + spaces(width-text.length());
        } else {
            return text.substring(0, width-1)+"~";
        }
    }
}

public class SpreadSheet {
    private int maxcol;
    private int maxrow;
    Cell[][] cells;

    public SpreadSheet(int col, int row) {
        maxcol=col;
        maxrow=row;
        cells=new Cell[col][row];
    }
    boolean check(int col, int row){
        return col >= 0 && col < maxcol && row >= 0 && row < maxrow;
    }
    void insert(int col, int row , Cell cell){
        if (check(col,row)) cells[col][row] = cell;
    }
    public void display(int cellwidth) {        
        displaydivider(cellwidth);
        for(int r=0; r<maxrow; r++){
            for(int c=0; c<maxcol;c++){
                System.out.print("|");
                if(cells[c][r]!=null) System.out.print(cells[c][r].display(cellwidth));
                else System.out.print(Cell.spaces(cellwidth));
            }
            System.out.println("|");                   
            displaydivider(cellwidth);
        }
    }
    private void displaydivider(int cellwidth){
        for(int c=0; c<maxcol;c++) {
            System.out.print("+"+Cell.chars(cellwidth,'-'));
        }
        System.out.println("+");
    }
    public static void main(String[] args) {
        SpreadSheet s=new SpreadSheet(4, 5);
        s.insert(0, 0, new NumberCell(123));
        s.insert(1, 1, new NumberCell(234342));
        s.insert(3, 4, new TextCell("alma"));
        s.insert(3, 3, new TextCell("almajkasfhasjkfhak"));
        s.display(8);
        System.out.println();
        s.display(5);
        
    }
}


