#include<stdio.h>
#include<stdlib.h>
#include "../data_structures/heapSort.c"

void sjfnp(int m, int* a_t, int* b_t, int* ans){

	int* arrival=malloc(m*sizeof(int));
	int* burst_time=malloc(m*sizeof(int));
	for(int i=0;i<m;i++){
		arrival[i] = a_t[i];
		burst_time[i] = b_t[i];
	}
	
	int total=0;
	for(int i=0;i<m;i++)
		total+=b_t[i];

	int** e=(int**)(calloc(m,sizeof(int**)));
		for(int i=0;i<m;i++)
			e[i]=(int*)(calloc(total,sizeof(int)));
	int* heaphead=(int*)calloc(m,sizeof(int));
	int* indexvalue=(int*)calloc(m,sizeof(int));

	int index=0;
	int value=0,size=0,job=0;

	for(int i=0;i<total;i++)
	{
		for(int j=0;j<m;j++){
			if(arrival[j]==i){
				minHeapPush(heaphead,indexvalue,&size,burst_time[j],j);	
			}
		}

			if(value==0)
				minHeapPop(heaphead,indexvalue,&value,&index,&size);
			printf(" %d ",index+1);
			ans[i] = index+1;
			e[index][i]=1;
			burst_time[index]--;
			value--;
			

		

	}
}
