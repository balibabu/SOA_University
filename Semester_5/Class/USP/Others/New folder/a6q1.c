#include<stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
int main()
{
    int fd,i;
    for(i=0;i<10;i++){
        fd=open("read.c",O_RDONLY);
        if(fd==-1){
            perror("Open error");
            return 1;
        }
        sleep(2);
        printf("File descriptor Number=%d\n",fd);
    }
    return 0;
}