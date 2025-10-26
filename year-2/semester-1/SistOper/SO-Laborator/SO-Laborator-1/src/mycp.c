#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#define BUFSIZE 8192


int main(int argc, char* argv[], char* env[])
{
   int n;
    char buf[BUFSIZE];


    while((n=read(0,buf,BUFSIZE))>0)
    {
        if(write(1,buf,n)!=n)
        {
            perror("write");
            exit(1);
        }
    }
    if(n<0)
    {
        perror("read");
        exit(1);
    }

    return 0;
}