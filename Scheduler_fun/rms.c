#include<stdio.h>
#include<stdlib.h>
#include "../data_structures/heapSort.c"


int lcm(int* ar, int m);

int lcm(int* ar, int m)	{
	int res = ar[0];
	int a,b;
	for(int i=1; i<m; i++)  {
		 if(res>ar[i])  {
		   b= res;
		   a= ar[i];
		 }
		 else  {
		   b = ar[i];
		   a = res;
		 }
		 int r=1;
		 while(r>0)  {
		   r = b%a;
		   b = a;
		   a = r;
		 }
		 res = (ar[i]*res)/b;
	}
	return res;
}
 	

void rms(int lcmm, int m, int* exec, int* period, int* arrival, int* ans){
	
 	int* rexec = (int*)(malloc(sizeof(int)*m)); 	
 	int* index = (int*)(malloc(sizeof(int)*m));
 	for(int i=0; i<m; i++)	{
 			rexec[i] = exec[i];
 	
 	}
 	int* heapdead = (int*)(malloc(sizeof(int)*lcmm*m));
 	int* heapindex = (int*)(malloc(sizeof(int)*lcmm*m)); 
 	
	int** e = (int**)(malloc(sizeof(int)*m));
	for(int i=0; i<m; i++)	
		e[i] = (int*)(malloc(sizeof(int)*lcmm));

 	int value;
 	int indexterm;
 	int heapsize = 0;
 	
 	for(int i=0; i<lcmm; i++)  {	
		for(int j=0; j<m; j++)	{
				e[j][i] = 0;
						
	  		if(arrival[j] == i)	{
				arrival[j] += period[j];
			 minHeapPush(heapdead, heapindex, &heapsize,arrival[j], j );
  				 rexec[j] = exec[j];
				}
		}
			if(heapsize > 0)	{	
				minHeapPop(heapdead,heapindex,&value,&indexterm,&heapsize);
//printf("%d ",indexterm+1);
				ans[i]=indexterm+1;
				e[indexterm][i] = 1;
				if(value>i)  {
					rexec[indexterm]--;
					if(rexec[indexterm]>0)	{
  			  	minHeapPush(heapdead, heapindex, &heapsize, value, indexterm );
					}  	
				}
			}
	

}
	
}

