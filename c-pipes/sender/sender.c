#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int fd;
    char* pipe = "/tmp/cpipe";

    mkfifo(pipe, 0666);

    srand((unsigned int)(time(NULL)));
    int index = 0;

    char char1[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$\%^&*()";
    char char2[73];
    fd = open(pipe, O_WRONLY);
    while(1)
    {
        for(index = 0; index < 72; index++){
            char2[index] = char1[rand() % (sizeof char1 - 1)];
        }
        write(fd, char2, sizeof(char2)); 
    }
    
    
    close(fd);
    unlink(pipe);

    return 0;
}