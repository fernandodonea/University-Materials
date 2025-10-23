#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

int main(int argc, char* argv[], char* env[])
{
    ssize_t r, w;
    char buf[256];


    while(1)
    {
        r=read(0,buf,256);
        if(r<0)
        {
            perror("read");
            exit(1);
        }
        if(r==0) //EOF
            break;
        
        char *p=buf;
        size_t to_write=r;
        w=write(1,p,to_write);
        if(w<0)
        {
            perror("write");
            exit(1);
        }        
    }


    return 0;
}