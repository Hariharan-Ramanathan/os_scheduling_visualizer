#include<stdio.h>
#include<stdlib.h>
#include "heapSort.c"

void arrayPrint(int*, int);
int lcm(int* ar, int m);

void arrayPrint(int* arr, int n)  {
	for(int i=0; i<n; i++) {
		printf("%d ",arr[i]);
	}
	printf("\n");
}

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
int main(int argc, char **argv)  {
 	int m = 3;
 	int arr[3][4] = {{3,20,7,0},{2,5,4,0},{2,10,9,0}};
 	int* exec = (int*)(malloc(sizeof(int)*m));
 	int* period = (int*)(malloc(sizeof(int)*m));
 	int* deadline = (int*)(malloc(sizeof(int)*m));
 	int* arrival = (int*)(malloc(sizeof(int)*m));
 	int* rdl = (int*)(malloc(sizeof(int)*m)); 	
 	int* offset = (int*)(malloc(sizeof(int)*m));
 	int* rexec = (int*)(malloc(sizeof(int)*m)); 	
 	int* index = (int*)(malloc(sizeof(int)*m));
 	for(int i=0; i<m; i++)	{
 			exec[i] =  arr[i][0];
 			rexec[i] = arr[i][0];
 			period[i] = arr[i][1];
 			deadline[i] = arr[i][2];
 			offset[i] = arr[i][3];
 			arrival[i] = arr[i][3];
 			rdl[i] = arr[i][3] + arr[i][2];
 	}
 	int lcmm = lcm(period,m);
 	int* heapdead = (int*)(malloc(sizeof(int)*lcmm*m));
 	int* heapindex = (int*)(malloc(sizeof(int)*lcmm*m)); 
 	
	int** e = (int**)(malloc(sizeof(int)*m));
	int** plote = (int**)(malloc(sizeof(int)*m));
  for(int i=0; i<m; i++)	{
		e[i] = (int*)(malloc(sizeof(int)*lcmm));
		plote[i] = (int*)(malloc(sizeof(int)*lcmm*100));
	}
 	int value;
 	int indexterm;
 	int heapsize = 0;
 	
 	for(int i=0; i<lcmm; i++)  {	
		for(int j=0; j<m; j++)	{
				e[j][i] = 0;
				for(int k=0; k<100; k++)
					plote[j][i*100+k] = 0;
		
	  		if(arrival[j] == i)	{
					 rdl[j] = deadline[j] + i;

  				 minHeapPush(heapdead, heapindex, &heapsize, rdl[j], j );
  				 arrival[j] += period[j];
					 rexec[j] = exec[j];
				}
		}
			if(heapsize > 0)	{	
				minHeapPop(heapdead,heapindex,&value,&indexterm,&heapsize);
				printf("%d ",indexterm+1);
				e[indexterm][i] = 1;
				for(int k=0; k<100; k++)
					plote[indexterm][i*100+k] = 1;
				if(value>i)  {
					rexec[indexterm]--;
					if(rexec[indexterm]>0)	{
  			  	minHeapPush(heapdead, heapindex, &heapsize, value, indexterm );
					}  	
				}
			}
			else {
	 		printf("0 ");
	 	  }
	}
	printf("\n");
	for(int i=0; i<m; i++){
		arrayPrint(e[i],lcmm); 
	}


   FILE *filePtr;
   filePtr = fopen("polar.dat","w");
      for(int i=0; i<lcmm*100; i++)  {
        //fprintf(filePtr, "%d\t", j);
			  //for(int i=0; i<3; i++)	{	
        	fprintf(filePtr, "%d\t%d\t%d\t%d\n",i, plote[0][i], plote[1][i], plote[2][i]);
          //}
				//fprintf(filePtr, "\n");
        }


/*
	for(int i=0; i<m; i++)	{
		for(int j=0; j<lcmm; j++)	{
			printf("%d\t",plote[i][j]);
		}
		printf("\n");
	}
*/






	return 0;	
} 
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
  /*minHeapBuild(deadline,index,m);
  minHeapPop(deadline,index,&value,&indexterm,&m);
  printf("%d %d\n",value,indexterm);
  minHeapPop(deadline,index,&value,&indexterm,&m);
  printf("%d %d\n",value,indexterm);
  minHeapPop(deadline,index,&value,&indexterm,&m);
  printf("%d %d\n",value,indexterm);
  minHeapPush(deadline, index, &m, 10, 2);
  minHeapPush(deadline, index, &m, 8, 3);
  minHeapPush(deadline, index, &m, 7, 9);
  arrayPrint(deadline,m);
  arrayPrint(index,m);*/

