#include <stdio.h>
#include <conio.h>
int main(int argc, char const *argv[])
{
    int col, row ;
    int i1 = 1;
    printf("How many column you want: ");
    scanf("%d", &col);
    printf("How many rows you want: ");
    scanf("%d", &row);
    for (int i = 0; i < col; i++)
    {
   for (int i1 = 0; i1 < row; i1++)
   {
    printf("%d\n",i1);
   }
   
    }                                                 
                       
return 0;
}
