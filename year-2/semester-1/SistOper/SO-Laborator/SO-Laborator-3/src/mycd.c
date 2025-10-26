#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <dirent.h>



int main( int argc, char *argv[], char *envp[])
{
    DIR *dp;
    struct diren *dirp;

    char buf[8192];

    if(argc !=2)
    {
        printf("Usage: %s <dirname>\n",argv[0]),exit(0);
    }

    if(chdir(argv[1])<0)
        perror("chdir"),exit(1);

    if(getcwd(buf,8192)==NULL)
        perror("getcwd"),exit(1);
    
    printf("CWD = %s\n",buf);
    exit(0);

}