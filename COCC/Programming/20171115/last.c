/*
 * Ask for a number, print out the Pascal triangle with that depth.
 */

#include <stdio.h>

int main()
{
    int n, x;
    int a, b;
    int facta,factb,factamb;
    int row, column;
    
    scanf("%d",&n);

    row=0;
    while(row<=n+2)
    {
        column=0;
        while(column<=n+1-row)
        {
            a=row+column;
            b=row;
            
            x=1; facta=1;
            while(x<=a)
            {
                facta=facta*x;
                x=x+1;
            }
            x=1; factb=1;
            while(x<=b)
            {
                factb=factb*x;
                x=x+1;
            }
            x=1; factamb=1;
            while(x<=a-b)
            {
                factamb=factamb*x;
                x=x+1;
            }
            printf("%4d",facta/factb/factamb);
            column = column+1;            
        }
        printf("\n");
        row=row+1;
    }    
   
    return 0;
}
