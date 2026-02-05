#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>


int main(int argc, char* argv[], char* envp[])
{
    if(argc<2)
    {
        printf("Introduceti macar un program executabil");
        exit(0);
    }

    pid_t pid=fork();

    if(pid<0)
    {
        //cod de tratare a erorii
        perror("fork");
        exit(1);
    }
    else if(pid==0)
    {
        //cod copil
        execvp(argv[1], &argv[1]);

        perror("execvp");//se executa doar daca execvp esueaza 
        exit(1);
    }
    else
    {
        //cod parinte
        wait(NULL);
    }

    exit(0);
}