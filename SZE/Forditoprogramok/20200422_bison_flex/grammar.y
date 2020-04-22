%{
    #include <iostream>
    #include <map>
    #include <string>
    using namespace std;
    int yylex();
    int yyerror(char* message){
        return 1;
    }

    map<string,int> identifiers;
%}

%union{
    int value;
    char name[16];
}

%token DELETE
%token<value> NUMBER
%token<name> ID

%type<value> term multiplication expression 

%%

commands: command '\n'   commands 
        | /* empty */ 
        ;

command: expression { cout<<"Correct input, calculated value: "<<$1<<"\n"; }
        | ID '=' NUMBER  { 
            cout<<"New ID \'"<<$1<<"\' with value "<<$3<<"\n";
            string temp($1);
            identifiers[ temp ]= $3;
            } 
        | DELETE ID {
         string tmp($2);
         if(identifiers.count(tmp)==1) {
             cout << "Variable "<<tmp<<" deleted\n";
             identifiers.erase(identifiers.find(tmp));
         }
         else { cout << "No such variable\n"; }
        }
        ;


expression: expression '+' multiplication { $$= $1 + $3; }
            | expression '-' multiplication { $$= $1 - $3; }
            | multiplication { $$= $1; }
            ;

multiplication: multiplication '*' term { $$= $1 * $3; }
               | multiplication '/' term { $$= $1 / $3; }
               | term { $$ = $1; }
               ;

term: '(' expression ')' { $$ = $2; }
     | NUMBER { $$ = $1; }
     | ID {
         string tmp($1);
         if(identifiers.count(tmp)==1) $$=identifiers[tmp];
         else {
            cout<<"wrong identifier, assume 0 value\n";
            $$ = 0;
         }
     }
     ;

%%


int main(){
    if (yyparse() == 0) cout<<"<ACC>\n";
    else cout<<"ERROR\n";
    return 0;
}
