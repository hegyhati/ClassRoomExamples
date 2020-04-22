
%{
    #include "grammar.tab.h"
    #include <cstring>
    #include <iostream>
    using namespace std;
%}


%option noyywrap

DIGITS  [0-9]
ALPHABET [a-zA-Z]
CHARACTERTOKENS [\+\-\*\/\(\)=]


%%
exit                                return '\0';
delete                              return DELETE;
{CHARACTERTOKENS}                   cerr<<"LOOKAHEAD: \'"<<yytext<<"\'\n"; return *yytext;
[1-9]{DIGITS}*                      yylval.value=atoi(yytext); cerr<<"LOOKAHEAD: NUMBER ("<<yylval.value<<")\n";  return NUMBER;
\n                                  return '\n'; 
{ALPHABET}({ALPHABET}|{DIGITS})*    strcpy(yylval.name,yytext);cerr<<"LOOKAHEAD: ID("<<yytext<<")\n"; return ID;
[ \t]*                              /* skip whitespace */


%% 


