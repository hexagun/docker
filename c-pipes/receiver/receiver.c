#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>

#define MAXBUF 1024

int main(){
    int fd;
    char* pipe = "/tmp/cpipe";
    char buf[MAXBUF];

    fd = open(pipe, O_RDONLY);
    while(1){
        read(fd, buf, MAXBUF);
        printf("Received: %s\n", buf);
    }
   
    close(fd);

    return 0;
}