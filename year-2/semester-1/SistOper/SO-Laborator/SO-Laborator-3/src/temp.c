#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>


int main(int argc, char *argv[])
{
    int fd=open(argv[0],O_RDWR);//returneaza file descriptorul

    if(fd<0)
    {
        perror("open");
        exit(-1);
    }

    //dam unlink fisierului temporar
    if(unlink(fd)==-1)
    {
        perror("unlink");
        exit(-1);
    }
    print("Fisierul %s a fost sters",argv[1]);

    sleep(15);


    char* buf;
    int n=read(fd,buf,5000);

    




    exit(0);
}