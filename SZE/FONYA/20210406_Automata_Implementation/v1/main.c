#include <stdio.h>

int accept(char* input) {
    int state;
    for (state=0; *input != '\0'; ++input){
        switch(state){
            case 0: switch(*input) {
                    case 'b' : state=1; break;
                    default: state=0;
                }; break;
            case 1:switch(*input) {
                    case 'a' : state=2; break;
                    case 'b' : state=1; break;
                    default: state=0; 
                }; break;
            case 2:switch(*input) {
                    case 'b' : state=3; break;
                    default: state=0; 
                }; break;
            case 3:switch(*input) {
                    default: state=3; 
                }; break;
        }
    }
    return state==3;
}

int main(){
    char input[1000010];
    scanf("%s",input);
    printf("%sElfogadva\n", (accept(input) ? "" : "Nincs ") );
    return 0;
}
