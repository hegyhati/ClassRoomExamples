
import java_cup.runtime.*;

%%

%class JSON_Lexer
%unicode 
%cup

%{  
    private Symbol symbol(int type) {
        return new Symbol(type, yyline, yycolumn);
    }
    
    private Symbol symbol(int type, Object value) {
        return new Symbol(type, yyline, yycolumn, value);
    }
%}

%%

":" { return symbol(sym.COLON); }
"," { return symbol(sym.COMMA); }
"{" { return symbol(sym.LBRACE); }
"}" { return symbol(sym.RBRACE); }
"[" { return symbol(sym.LBRACKET); }
"]" { return symbol(sym.RBRACKET); }
"null" { return symbol(sym.NULL); }


\" [^\n\r\"\\]+ \" { 
    return symbol(sym.STRING, yytext().substring(1, yytext().length() - 1)); 
}

true | false { 
    return symbol(sym.BOOL,yytext().equals("true")); 
}

[1-9][0-9]* { 
    System.out.println("Number matched: "+yytext());
    return symbol(sym.NUMBER, Float.parseFloat(yytext()));
} 

[ \t\r] { /* whitespace */ }

\n      { return null; }

