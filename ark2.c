#include<stdio.h>
int print_Array(int a[],int d){
    for(int i =0;i<d;i++){
        printf("%d ",a[i]);
    }
    printf("\n");
    return 0;
}
int main() {
    int daimen;
    printf("Input the number of elements to store in the array : ");
    scanf("%d",&daimen);
    int arr1[daimen],arr2[daimen], temp;
    for(int i=0;i<daimen;i++){
        printf("element - %d : ",i+1);
        scanf("%d",&temp);
        arr1[i] = temp;
    }
    printf("The vales store into the array : ");
    print_Array(arr1,daimen);
    for(int i=0;i<daimen;i++){
        arr2[i] = arr1[daimen-i-1];
    }
    printf("The vales store into the array in REVERSE: ");
    print_Array(arr2,daimen);
    return 0;
}