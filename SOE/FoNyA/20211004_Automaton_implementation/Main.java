import java.util.Scanner;

class Main {
    public static void main(String[] args){
        int state=0;
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        for (int idx=0; idx<input.length(); idx++){
            switch(state){
                case 0: switch (input.charAt(idx)) {
                    case 'a': state = 0; break;
                    case 'b': state = 1; break;
                    case 'c': state = 0; break;
                    default: throw new IllegalArgumentException();
                } break;
                case 1: switch (input.charAt(idx)) {
                    case 'a': state = 2; break;
                    case 'b': state = 1; break;
                    case 'c': state = 0; break;
                    default: throw new IllegalArgumentException();
                } break;
                case 2: switch (input.charAt(idx)) {
                    case 'a': state = 0; break;
                    case 'b': state = 3; break;
                    case 'c': state = 0; break;
                    default: throw new IllegalArgumentException();
                } break;
                case 3: switch (input.charAt(idx)) {
                    case 'a': state = 3; break;
                    case 'b': state = 3; break;
                    case 'c': state = 3; break;
                    default: throw new IllegalArgumentException();
                } break;
            }
        }
        System.out.println(state==3?"Accepted":"Not accepted");
    }
}
