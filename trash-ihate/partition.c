#include <stdio.h>

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

// i really don't understand the partition logic behind the quick sort

// { 5, 10, 9, 8, 2, 1 , 3}

int partition(int arr[], int s, int e) {
	
	int pivot = arr[e];
	int p_index = s;

	for( int j = s ; j < e ; j++){
		if(arr[j] <= pivot){
			swap(&arr[p_index] , &arr[j]);
			p_index++;
		}
	}
	swap(&arr[p_index] , &arr[e]);
	return p_index;
}

void quick_sort(int arr[], int s , int e) {
	if(s <= e){
		int p = partition(arr , s, e);
		quick_sort(arr, s , p-1);
		quick_sort(arr, p+1 , e);
	}
}
void main()
{
	int arr[7] = {5, 10, 9, 8,2,1,3};

	int len = 7;

	quick_sort(arr , 0 , len-1);

	for (int i = 0; i < len; i++)
	{
		printf("%d ", arr[i]);
	}
	printf("\n");
}