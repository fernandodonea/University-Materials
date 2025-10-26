#include <sys/types.h>
#include <sys/stat.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{
    struct stat buf;

    mode_t m;
    char *type;

    for(int i=1;i<argc;i++)
    {
        if(lstat(argv[i],&buf)<0)
        {
            perror("lstat");
            continue;
        }

        m=buf.st_mode;
        if(S_ISREG(m)) type="regular file";
        else if(S_ISDIR(m)) type="directory";
        else if(S_ISCHR(m)) type="character file";
        else if(S_ISBLK(m)) type="block file";
        else if(S_ISFIFO(m)) type="FIFO file (named piped)";
        else if(S_ISLNK(m)) type="simbolic link";
        else if(S_ISSOCK(m)) type="socket file";
        else type="unknown file type";
        printf("%s: %s\n",argv[i],type);
    }

    exit(0);
}

