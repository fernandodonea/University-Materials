#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>


int main(int argc, char* argv[], char* env[])
{
    if (argc != 2) {
        fprintf(stderr, "Utilis: %s <nume_fisier>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int fd;
    const char *filename = argv[1];
    const char *str1 = "inceput";
    const char *str2 = "sfarsit";

    // Cream si deschidem fisierul pentru scriere
    // O_CREAT: creeaza fisierul daca nu exista
    // O_WRONLY: deschide doar pentru scriere
    // O_TRUNC: daca fisierul exista, il goleste
    // 0644: permisiuni (proprietarul poate citi/scrie, grupul/altii pot citi)
    fd = open(filename, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // Scriem primul sir de caractere la inceputul fisierului.
    if (write(fd, str1, strlen(str1)) < 0 ) {
        perror("write");
        close(fd);
        exit(EXIT_FAILURE);
    }

    // Mutam offset-ul fisierului la pozitia 100 pentru a crea o "gaura".
    // SEEK_SET inseamna ca offset-ul este calculat de la inceputul fisierului.
    if (lseek(fd, 100, SEEK_SET) == -1) {
        perror("lseek");
        close(fd);
        exit(EXIT_FAILURE);
    }

    // Scriem al doilea sir de caractere la noul offset.
    if (write(fd, str2, strlen(str2)) == -1) {
        perror("write 2");
        close(fd);
        exit(EXIT_FAILURE);
    }

    // Inchidem fisierul.
    if (close(fd) == -1) {
        perror("close");
        exit(EXIT_FAILURE);
    }

    return 0;
}
