#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>//pt open

int global=6;
char buf[]="unbuffered write to stdout\n";




int main(int argc, char* argv[], char* envp[])
{
    int local=10;

    write(1,buf,sizeof(buf)-1); // 1 -> in terminal

    printf("inainte de fork\n"); 
    //PRINTF scrie intr-un buffer, nu direct pe ecran



     
    //in fork buffer-ul nu s a flushit
    //FLUSH = goloste bufferul


    pid_t pid;
    //in fork se copie nu doar variabilele absolut tot


    if ((pid=fork()) < 0)
    {
        //cod de tratare a erorii
        perror("fork");
        exit(1);

    }
    else if(!pid)
    {
        // pid ==0, cod copil

        global++;
        local++;


        printf("pid: %d, global: %d, local: %d\n", getpid(), global, local);

        
    }
    else
    {
        // pid >0, cod parinte 


        //suspendam executia parintelui
        sleep(2);

        printf("pid: %d, global: %d, local: %d\n", getpid(), global, local);

        exit(0);

    }
    
    _exit(0); //nu mai vezi nimic, nu mai face flush



}