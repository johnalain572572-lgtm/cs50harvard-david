# include <stdio.h>
void meow (void);
int main(void){
        for (int i=0; i < 3; i++){
                meow();
        }
}
void meow(void){
        printf("meow\n");
}
/*a way to check if the file exist and run it by make
 cs50harvardDavid ls
cs50code hello    hello.c  hello1   hello1.c hello1.s link.txt
➜  cs50harvardDavid make hello1
make: `hello1' is up to date.
➜  cs50harvardDavid ./hello1
meow
meow
meow*/