// Compile with: $ gcc -o merge-sort merge-sort.c 
// run with: ./[name of file]
#include <stdio.h>
#include<time.h>

#define max 10

int a[11] = { 10, 14, 19, 26, 27, 31, 33, 35, 42, 44, 0 };
int b[10];

void sort(int low, int high) {
    int mid;

    if (low < high) {
        mid = (low + high) / 2;
        sort(low, mid);
        sort(mid + 1, high);

        int low2, mid2, i;

        for (low2 = low, mid2 = mid + 1, i = low; low2 <= mid && mid2 <= high; i++) {
            if (a[low2] <= a[mid2])
                b[i] = a[low2++];
            else
                b[i] = a[mid2++];
        }

        while (low2 <= mid)
            b[i++] = a[low2++];

        while (mid2 <= high)
            b[i++] = a[mid2++];

        for (i = low; i <= high; i++)
            a[i] = b[i];
    } else {
        return;
    }
}

int main() {
    int i;
    printf("List before sorting\n");

    for (i = 0; i <= max; i++)
    printf("%d ", a[i]);

    //time counting:
	double total_time;
	clock_t start, end;
	start = clock();
    //time count starts 
	srand(time(NULL));

    sort(0, max);

    end = clock();
    //time count stops 
	total_time = ((double) (end - start))/CLOCKS_PER_SEC;
	//calulate total time
    printf("\n%lu", start);
    printf("\n%lu", end);
	printf("\nTime taken was: %f", total_time);
    
    printf("\nList after sorting\n");

    for (i = 0; i <= max; i++)
        printf("%d ", a[i]);
}