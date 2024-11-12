import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws Exception {
        LilyPond_Lexer l = new LilyPond_Lexer(new InputStreamReader(System.in));
        LilyPond_Parser p = new LilyPond_Parser(l);
        p.parse();
    }
}