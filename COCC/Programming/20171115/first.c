/*
 * Print out the positive integer numbers until 100 in increasing order
 */

#include <stdio.h>

int main()
{

    int x;
    x=1;

    
    while(x<=100)
    {
        printf("%4d\n",x);
        x=x+1;
    }


    return 0;
}
