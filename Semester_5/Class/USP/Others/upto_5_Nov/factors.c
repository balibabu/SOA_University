#include <stdio.h>
int main(){
	int  num;
	printf("enter a number ");
	scanf("%d",&num);
	for(int i=1;i<=num/2;i++){
		if(num%i==0)
			printf("%d, ",i);
	}
	printf("%d\n",num);
	return 0;
}
