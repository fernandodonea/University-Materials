#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char* argv[], char* envp[])
{
    pid_t pid;

    // Cream un proces nou
    pid = fork();

    if (pid < 0)
    {
        //cod de tratare a erorii
        perror("fork");
        exit(1);

    }
    else if(!pid)
    {
        // pid ==0, cod copil

        printf("copil: pid: %d\n", getpid());
        exit(0); 
    }
    else
    {
        // pid >0, cod parinte 
        printf("parinte - pid: %d. copil cu pid-ul: %d.\n", getpid(), pid);


        //
        sleep(20);//in acest timp copilul va fi zombie

        
        printf("wakey wakey");
    }
    return 0;
}