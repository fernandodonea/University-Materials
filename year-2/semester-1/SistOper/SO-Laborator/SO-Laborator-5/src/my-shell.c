#include <stdio.h>

//pt read
#include <unistd.h>

//pt fgets
#include <stdlib.h>

//pt strtok
#include <string.h>

#define BUFSIZE 1024
#define MAX_ARGS 256



void parse_line(char* line, char* exec_argv[])
{
    char *x;
    int k=0;

    x=strtok(line," \n\t");
    while(x!=NULL)
    {
        exec_argv[k++]=x;
        x=strtok(NULL," \n\t");
    }
    exec_argv[k]=NULL; //lista de argumente trbuie sa se termine cu NULL

}



int main(int argc, char* argv[], char* envp[])
{
    char buf[BUFSIZE];
    pid_t pid;

    while(1)
    {
        
        printf("my-shell> ");
        fflush(stdout);

        buf[0]='\0';

        ssize_t r=read(0,buf,BUFSIZE);
        if(r<0)
        {
            perror("read");
            exit(1);
        }

        if(buf[0]=='\0')
        {
            printf("^D\n");
            break;
        }

        

        char* exec_argv[MAX_ARGS];
        parse_line(buf,exec_argv);

        

        pid=fork();
        if(pid<0)
        {
            perror("fork");
            exit(1);
        }
        else if(pid==0)
        {
            //cod copil
            execvp(exec_argv[0],exec_argv);
            perror("execvp");
            exit(1);

        }
        else if(pid>0)
        {
            //cod parinte
            wait(NULL);

        }

    }
    return 0;
}