#include<stdio.h>
#include<string.h>

int count_vowels(char []);

int main()
{
   char word[100];
   printf("Enter a string\n");
   scanf("%[^n]%*c",word);
   printf("Number of vowels: %d\n", count_vowels(word));
   return 0;
}

int count_vowels(char wd[])
{
    int count = 0, i = 0;
    char ch = wd[i];
    while (ch != '\0'){
        ch = wd[i];
        i++;
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            count ++;
        if (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U')
            count ++;
    }
   return count;
}