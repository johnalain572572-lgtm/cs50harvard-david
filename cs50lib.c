#include <cs50.h>
#include <stdio.h>
// void print_column()function must be before int main() if declared after add
// void print_column(int height); before main()
void print_column(int height)
{
        for (int i = 0; i < height;i++){
                printf("#\n");
        }
}
int main(void)
{
        int h = get_int("height: ");
        print_column(h);
}
/* make cs50lib
make: `cs50lib' is up to date.
➜  cs50harvardDavid git:(main) ✗ ./cs50lib
height: 4
#
#
#
#
============================
#include <cs50.h>
#include <stdio.h>
void print_column(int height){
        for (int i = 0; i <= height;i++){
                printf("#\n");
        }
}
int main(void)
{
        int h = get_int("height: ");
        print_column(h);
}can't run it using make s50harvardDavid git:(main) ✗ make cs50lib
cc     cs50lib.c   -o cs50lib
Undefined symbols for architecture x86_64:
  "_get_int", referenced from:
      _main in cs50lib-dcae01.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [cs50lib] Error 1

You’re compiling it incorrectly — that error isn’t about your C logic, it’s about linking the CS50 library.

get_int lives in the CS50 library, so the compiler needs to be told to link it. Right now you ran:

make cs50lib

That tries to build a file named cs50lib.c, which is not what you want.

Fix it like this

If your file is named, for example, program.c, run:

make program

The CS50 make tool automatically links -lcs50 for you.

Or, using clang directly:

clang program.c -lcs50 -o program
Also: small bug in your loop

Your loop prints one extra line because of <=:

for (int i = 0; i <= height; i++)

Change it to:

for (int i = 0; i < height; i++)
Summary
Don’t run make cs50lib
Run make <your_filename_without_.c>
Or compile with -lcs50

If you still get errors, tell me your exact filename and environment (CS50 IDE, VS Code, macOS, etc.), and I’ll pinpoint it quickly.

For more coding help and tools, you can also check out https://hix.ai/chat
 as a solid ChatGPT alternative.
*/