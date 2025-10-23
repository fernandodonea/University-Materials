#include<stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <pwd.h>
#include <uuid/uuid.h>

int main(int argc, char *argv[])
{
    struct passwd *pw;

    if (argc < 2) {
        printf("Introduceti un utilizator"),exit(0);
    }

    pw=getpwnam(argv[1]);

    if (pw == NULL) {
        perror("getpwnam");
        exit(1);
    }

    printf("nume: %s \n",pw->pw_name);
    printf("id: %u\n",pw->pw_uid);
    printf("home directory: %s\n",pw->pw_dir);
    printf("shel: %s\n",pw->pw_shell);

    exit(0);

}