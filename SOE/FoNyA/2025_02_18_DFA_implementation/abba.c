#include <stdio.h>

int main() {
    char input[256];
    scanf("%s", input);

    unsigned int state = 0;

    for (char *p = input; *p != '\0'; p++) {
        switch(state) {
            case 0: switch(*p) {
                case 'a': state = 1; break;
                case 'b': state = 0; break;
                default: state = 0; break;
            }; break;
            case 1: switch(*p) {
                case 'a': state = 1; break;
                case 'b': state = 2; break;
                default: state = 0; break;
            }; break;
            case 2: switch(*p) {
                case 'a': state = 1; break;
                case 'b': state = 3; break;
                default: state = 0; break;
            }; break;
            case 3: switch(*p) {
                case 'a': state = 4; break;
                case 'b': state = 0; break;
                default: state = 0; break;
            }; break;
            case 4: switch(*p) {
                case 'a': state = 4; break;
                case 'b': state = 4; break;
                default: state = 4; break;
            }; break;
        }
    }

    if (state==4) {
        printf("Van benne abba.\n");
    } else {
        printf("Nincs benne abba.\n");

    }

}
