package FirstTest;

import FirstTest.Test;

import java.io.IOException;
import java.io.InputStreamReader;


class TestUser {
    public static void main(String[] args) {
        Test t = new Test(new InputStreamReader(System.in));
        try {
            while(t.yylex() != null) {}
        } catch (IOException e) {}
    }
}