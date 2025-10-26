#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char* argv[], char* env[])
{
    char buf[256];
    size_t r,w;

    if(argc!=3)
    {
        printf("Usage: %s <dirname>\n",argv[0]),exit(0);
    }

    //deschidere fisiere
    int fd_src=open(argv[1],O_RDONLY);//intoarce file descriptorul
    if(fd_src<0)
    {
        perror("open");
        exit(-1);
    }
    int fd_dest=open(argv[2],O_WRONLY);
    if(fd_dest<0)
    {
        perror("open");
        exit(-1);
    }

    //citire fisier
    r=read(fd_src,buf,256);
    if(r<0)
    {
        perror("read");
        exit(1);
    }



    char *p=buf;
    size_t to_write=r;

    w=write(fd_dest,p,to_write);
    if(w<0)
    {
        perror("write");
        exit(1);
    }


    exit(0);
}