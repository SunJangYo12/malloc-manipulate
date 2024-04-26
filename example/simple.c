#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int len(char *str)
{
    int i;
    for (i=0; str[i]; i++);

    return(i);
}

int main(int argc, char **argv)
{
    char *str;
    int i = 1;

    if (argc == 2)
    {
       str = malloc(len(argv[1]) + 1);
       strcpy(str, argv[1]);
    }
    else {
       printf("usage: %s <string>\n", argv[0]);
       exit(1);
    }

    while(1) {
       printf("[%d] %s - addr: %p\n", i, str, str);

       sleep(1);
       i++;
    }
    free(str);

    return 0;
}
