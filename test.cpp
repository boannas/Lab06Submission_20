#include<stdio.h>
using namespace std;

int a[3][2] = {{1,2},{3,4},{5,6}};

int main() {
    for(int i =0; i< 3 ; i++){
        for(int j =0; j < 2 ; j++){
            printf("Array : %d, index : %d, value : %d \n" , i , j , a[i][j] );
        }
    }
}