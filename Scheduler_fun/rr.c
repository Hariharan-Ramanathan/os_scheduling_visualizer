#include<stdio.h>
#include<stdlib.h>
#include "../data_structures/queue.c"

void rr(int m, int* arrival_t, int* burst_t, int* ans){
	Queue* queue=createQueue(m);
	
	int quantum=3;
	int* arrival=malloc(m*sizeof(int));
	int* burst_time=malloc(m*sizeof(int));
	int* exec=malloc(m*sizeof(int));
	int* rexec=malloc(m*sizeof(int));
	for(int i=0;i<m;i++){
		arrival[i]=arrival_t[i];
		burst_time[i]=burst_t[i];
		if(burst_time[i]<quantum){
			exec[i]=rexec[i]=burst_time[i];
			burst_time[i]=0;
		}
		else{
			exec[i]=rexec[i]=quantum;
			burst_time[i]-=quantum;
		}
	}	
	int total=0;
	for(int i=0;i<m;i++)
		total+=burst_t[i];
	
	int** e=(int**)(calloc(m,sizeof(int**)));
		for(int i=0;i<m;i++)
			e[i]=(int*)(calloc(total,sizeof(int)));
	int value=0,p=0;

	for(int i=0;i<total;i++)
	{
		for(int j=0;j<m;j++){
			if(arrival[j]==i){
				enqueue(queue,j+1);
			}
		}
		value=queue->array[queue->front];
		if(exec[value-1]==0){
				p=dequeue(queue);
				if(burst_time[p-1]!=0){
					enqueue(queue,p);
					if(burst_time[p-1]<quantum){
						exec[p-1]=burst_time[p-1];
						burst_time[p-1]=0;
					}
					else{
						exec[p-1]=quantum;
						burst_time[p-1]-=quantum;
					}
					

				}
			}	
			value=queue->array[queue->front];
			//printf(" %d ",value);
			ans[i] = value;	
			e[value-1][i]=1;
			exec[value-1]--;
	}

}
