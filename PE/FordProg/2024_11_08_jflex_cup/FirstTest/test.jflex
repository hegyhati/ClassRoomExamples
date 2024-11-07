
// code verbatim copied. imports and such
package FirstTest;

%%

%class Test
%unicode 
%type Integer

%{
// code included in the class
%}

// Macro definitions

NonZeroDigit = [1-9]
Digit = [0-9]

// %state whatever
%%

"fd"                    { System.out.println("FORWARD"); }
"lt"                    { System.out.println("TURN LEFT"); }
"rt"                    { System.out.println("TURN RIGHT"); }
{NonZeroDigit} {Digit}* { System.out.println(yytext()); }
[ \t\n\r]+              { /* Ignore whitespace */ }
.                       { System.out.println("Error, unrecognized character: " + yytext()); }