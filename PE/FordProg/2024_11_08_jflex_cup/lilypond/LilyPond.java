import java.io.InputStreamReader;

class LilyPond {
    public static void main(String[] args) throws Exception {
        LilyPond_Lexer l = new LilyPond_Lexer(new InputStreamReader(System.in));
        l.yylex();
    }
}