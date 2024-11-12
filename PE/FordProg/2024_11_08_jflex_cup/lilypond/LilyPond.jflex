

%%

%class LilyPond_Lexer
%unicode
%type String



%%

[cdefgab]           { System.out.println("Note: " + yytext()); }
'                   { System.out.println("Octave up."); }
,                   { System.out.println("Octave down."); }
1|2|4|8|16|32|64    { System.out.println("Duraction: " + yytext()); }
[ \t\n\r]           { /* ignore whitespace */ }
.                   { System.out.println("Error with  char: " + yytext());}
