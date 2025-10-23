#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[], char *env[])
{

    char* x=env[0],*var_mediu;
    int i=0,n,ok=0;

    if(argc!=2)
    {
        printf("Introduceti o singura variabial de mediu pentru comanda 'env\n");
        exit(0);
    }

    var_mediu=argv[1];
    n=strlen(var_mediu);

    while(x!=NULL)
    {


        if(strncmp(x,var_mediu,n)==0)
        {
            printf("%s\n",x);
            exit(0);
        }
        i++;
        x=env[i];
    }

    printf("Variabila de mediu nu a fost gasita\n");
    exit(0);

}