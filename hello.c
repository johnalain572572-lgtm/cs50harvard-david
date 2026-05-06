#include <cs50.h>
#include <stdio.h>
int main(void){
        string name = get_string("what's your name: ");
        printf("hello, %s\n", name);
}
/*➜ how to create file by code command and run it
cs50harvardDavid code hello.c
zsh: command not found: code
➜  cs50harvardDavid code hello.c
➜  cs50harvardDavid clang hello.c
➜  cs50harvardDavid ls
a.out    hello.c  link.txt
➜  cs50harvardDavid ./a.out
hello, world%                                                                                                    
➜  cs50harvardDavid */
// see note in agenda 23 juillet 2010
//   cs50harvardDavid mv hello.c a.out cs50code move 2 files to cs50code folder
/*➜another way to run the file
cs50code clang -o hello hello.c
➜  cs50code ls
a.out   hello   hello.c
➜  cs50code ./hello
hello, world%                                                                                                    
➜  cs50code */
/*➜  remove the file a.out
cs50code rm a.out
➜  cs50code ls
hello   hello.c*/
/*➜ another way to run it using cs50 library
cs50code clang -o hello hello.c -lcs50
➜  cs50code ./hello
hello, world% */
