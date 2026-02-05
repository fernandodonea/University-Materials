#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

void myprint(char *str)
{
    char c;
    for(c=*str;c!='\n';c=*str++)
        write(1,&c,1);
    
}

int main(int argc, char* argv[], char* envp[])
{
    pid_t pid;

    if((pid=fork())<0)
        perror("fork");
    else if(!pid)
        myprint("this is the child procces printing\n");
    else
        myprint("this os the parrent procces printing\n");
    
    exit(0);

    /*
    CONCLUZIE

    orice print concurent pe ecran, poate fi gurbles (este o resursa partajata)
    se incurca liniile intre ele

    totul depinde de ordinea pe care o alege kernelul
    kernelul se poate supara si opreste un proces

    - tiparesc alternativ procesele
    */
}