#include <stdio.h>
#include <stdlib.h>

#include <sys/wait.h>
//pt open
#include <fcntl.h>

//pt read
#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>

#include <string.h>

#define BUFSIZE 1024


int parsing(char *script, char* interpretor[])
{
    if(script[0]!='#' || script[1]!='!')
    {
        printf("eroare interpretor in script");
        return -1;
    }
    script+=2;//sarim peste #!

    char *x=strtok(script, " \n\t");
    int k=0;
    while(x!=NULL)
    {
        interpretor[k++]=x;
        x=strtok(NULL," \n");
    }
    interpretor[k] = NULL; 
    return k; //ret nr de argumente gasite
    
}


int main(int argc, char* argv[], char* env[])
{

    if(argc<2)
    {
        printf("eroare nr parametri\n");
        exit(0);
    }


    //deschidem fisierul script
    char *file_name=argv[1];
    int fd;
    fd=open(file_name,O_RDONLY);
    if(fd<0)
    {
        perror("open");
        return(1);
    }


    char buf[BUFSIZE];
    ssize_t r;

    //citim scriptul
    r=read(fd,buf,BUFSIZE);
    if(r<0)
    {
        perror("read");
        exit(1);
    }
    close(fd);
    buf[r] = '\0'; 
    

    //daca gasim \n adaugam terminator de sir \0
    char *newline = strchr(buf, '\n');
    if (newline != NULL) {
        *newline = '\0';
    }

    //cautam informatiile despre interpretorul de comenzi
    char* arg_exec[256];
    int n=parsing(buf,arg_exec);
    



    pid_t pid=fork();//proces nou
    if(pid<0)
    {
        perror("fork");
        exit(1);
    }
    if(pid==0)
    {
        //cod copil

        //adaugam parametrii din argv cititi de la tast
        for(int i=1;i<argc;i++)
        {
            arg_exec[n++]=argv[i];
        }
        arg_exec[n]=NULL;//execv cere NULL ca utlimul element din lista

        
        execv(arg_exec[0],arg_exec);
        perror("execv");
        exit(1);

    }
    else if (pid>0)
    {
        //cod parinte
        wait(NULL);
    }

    exit(0);
}