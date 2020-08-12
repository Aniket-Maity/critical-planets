#include<stdio.h>
#include<stdio.h>
#include<stdlib.h>
#define gcx getchar_unlocked
#define pcx putchar_unlocked
typedef long int lint;

lint getValue(){
    lint n = 0;
    int c = gcx();
    while(c<'0' ||c>'9') c = gcx();
    while(c>='0' && c<='9'){
        n = n*10 + c-'0';
        c=gcx();
    }
    return n;
}
int main(){
    
}