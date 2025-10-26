#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>


int main(int argc, char* argv[], char* envp[])
{
    if(argc!=2)
    {
        printf("Utilis: %s <nume_fisier>\n",argv[0]);
        exit(0);
    }

    char* file_name=argv[1];
    struct stat file_info;

    // Apelam stat() pentru a obtine informatii despre fisier.
    if (stat(file_name, &file_info) == -1) {
        perror("Eroare la stat");
        exit(EXIT_FAILURE);
    }
    
    // st_blocks contine numarul de blocuri de 512B alocate.
    long long real_size = (long long)file_info.st_blocks * 512;

    printf("%lld\t%s\n", real_size, file_name);
    return 0;
}