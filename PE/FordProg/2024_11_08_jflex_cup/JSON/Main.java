
import java.io.InputStreamReader;


class Main {
    public static void main(String[] args) throws Exception {
        JSON_Lexer lexer = new JSON_Lexer(new InputStreamReader(System.in));
        parser json_parser = new parser(lexer);
        json_parser.parse();
        System.out.println("Yeppee");
    }
}