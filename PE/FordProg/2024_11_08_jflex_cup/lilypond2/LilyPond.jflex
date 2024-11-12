import java_cup.runtime.*;


%%


%class LilyPond_Lexer
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

[cdefgab]           { return symbol(sym.NOTE, "cdefgab".indexOf(yytext())); }
,+|'+               { return symbol(sym.OCTAVE, yytext().length() * (yytext().charAt(0) == ',' ? 1 : -1) ); }
1|2|4|8|16|32|64    { return symbol(sym.DURATION, Integer.parseInt(yytext())); }
[ \t]               { /* ignore whitespace */ }
[\n]                { return null; }
