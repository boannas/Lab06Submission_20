#include<stdio.h>
int main() {
    int m,n,i,j,temp,cnt=0;
    printf("Enter number of Rows of matrix: ");
    scanf("%d",&m);
    printf("Enter number of Cols of matrix: ");
    scanf("%d",&n);
    for(i=1;i<m+1;i++){
        for(j=1;j<n+1;j++){
            printf("matrix [%d,%d] : ",i,j);
            scanf("%d",&temp);
            if(temp%2!=0){
                cnt++;
            }
        }
    }
    printf("Frequency of ODD number is %d",cnt);
}