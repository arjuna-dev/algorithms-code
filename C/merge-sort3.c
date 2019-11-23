// Compile with: $ gcc -o merge-sort3 merge-sort.c 
// run with: ./[name of file]
#include <stdlib.h>
#include <stdio.h>
#include<time.h>

#define max 100000



int a[100000];
int b[99999];

void sort(int low, int length) {
    int mid;

    if (low < length) {
        mid = (low + length) / 2;
        sort(low, mid);
        sort(mid + 1, length);

        int low2, mid2, i;

        for (low2 = low, mid2 = mid + 1, i = low; low2 <= mid && mid2 <= length; i++) {
            if (a[low2] <= a[mid2])
                b[i] = a[low2++];
            else
                b[i] = a[mid2++];
        }

        while (low2 <= mid)
            b[i++] = a[low2++];

        while (mid2 <= length)
            b[i++] = a[mid2++];

        for (i = low; i <= length; i++)
            a[i] = b[i];
    } else {
        return;
    }
}

int main() {
    int j;
    for(j = 0; j<100000; j++) {
        a[j] = rand()%100000;
    }

    // printf("List before sorting\n");
    // int i;

    // for (i = 0; i <= 100; i++)
    // printf("%d ", a[i]);

    //time counting:
	double total_time;
	clock_t start, end;
	start = clock();
    //time count starts 
    sort(0, max);
    end = clock();
    //time count stops 
	total_time = ((double) (end - start))/CLOCKS_PER_SEC;
	//calulate total time
	printf("\nTime taken was: %f", total_time);
    
    // printf("\nList after sorting\n");
    // for (i = 0; i <= 100; i++)
    //     printf("%d ", a[i]);
}