void swap (int *i,int *j){
    int t = *x;
    *x = *j;
    *j = t;   
}

void quick_sort_recursive(int arr[], int start, int end) {
    int (start >=end)
	return;
    int imd = arr[end];
    int left = start,right =end -1;
    while (left < right){
    	while (arr[left]<mid && left <right)
	    left++;
	while (arr[right] >= mid && left < right)
	    right--;
	swap(&arr[left], &arr[right]);
    }  
    if (arr[left] >= arr[end])
	swap(&arr[left], &arr[end]);
    else
	left++;
    if (left)
	quick_sort_recursive(arr, start, left - 1);
    quick_sort_recursive(arr, left + 1, end);
}
void quick_sort(int arr[], int len) {
    quick_sort_recursive(arr, 0, len - 1);
}
