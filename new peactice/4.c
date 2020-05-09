#include <stdio.h>
int main()
{
    int number,rem;
    number=12;
    rem=number%2;
    if(rem==0){
        printf("the number is even\n");
    }
    else{
        printf("the number is odd\n");
    }
    return 0;
}
