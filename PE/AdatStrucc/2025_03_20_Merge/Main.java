
import java.util.Scanner;

public class Main {

    public static SortedList readSortedList(){
        return readSortedList(false);
    }
    public static SortedList readSortedList(boolean debug){
        SortedList l = new SortedList();
        if (debug) System.out.println(l);
        int num;
        Scanner scanner = new Scanner(System.in);
        while (true) {
            num = scanner.nextInt();
            if (num == 0) break;
            l.push(num);
            if (debug) System.out.println(l);
        }
        return l;
    }
    
    public static void main(String[] args) {
        // readSortedList(true);

        SortedList l1 = readSortedList(); 
        System.out.print("L1: ");
        System.out.println(l1);

        SortedList l2 = readSortedList();
        System.out.print("L2: ");
        System.out.println(l2);

        SortedList merged = new SortedList(l1,l2);
        System.out.println("\nAfter merge:\n");
        System.out.print("Merged: ");
        System.out.println(merged);
        System.out.print("L1: ");
        System.out.println(l1);
        System.out.print("L2: ");
        System.out.println(l2);
    }
}