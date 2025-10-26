#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>

int main(int argc, char* argv[], char* env[])
{
    ssize_t r, w;
    char buf[256];
    int fd_sursa,fd_dest;

    if(argc!=3)
    {
        print("Nr invalid de parametrii\n");
        exit(0);
    }


    fd_sursa=open(argv[1],O_RDONLY);
    if(fd_sursa<0)
    {
        perror("open");
        exit(-1);
    }

    fd_dest=open(argv[2],O_WRONLY);
    if(fd_dest<0)
    {
        perror("open");
        exit(-1);
    }

    //dup2 -> duplica filedescriptorul 
    dup2(fd_sursa,0);
    dup2(fd_dest,1);

    close(fd_sursa);
    close(fd_dest);



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