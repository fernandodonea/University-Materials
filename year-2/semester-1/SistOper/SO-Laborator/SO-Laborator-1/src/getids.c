#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h> //pentru getpid, getuid, getgid
#include <stdio.h> //pentru printf
 

int main(int argc, char* argv[])
{
    int pid,uid,guid;

    pid=getpid();
    uid=getuid();
    guid=getgid();

    printf("Procces Id: %u\n",pid);
    printf("User Id: %u\n",uid);
    printf("Group Id: %u\n\n",guid);

    exit(0);
    

}