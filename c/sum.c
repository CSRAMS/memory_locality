/*
Given by Dr. Ngo.
This program assesses the memory locality of C
It does so by running a sum program and timing the program
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define N 1024
#define M 1024

int main(int argc, char *argv[]) {
  int i, j, sum = 0;
  int a[M][N];
  clock_t start,end;

  for (i = 0; i < M; i++) {
    for (j = 0; j < N; j++) {
      a[i][j] = 1;
    }
  }

  start = clock();
  for (i = 0; i < M; i++)
    for (j = 0; j < N; j++)
      sum += a[i][j];
  end = clock();
  printf("It takes %f seconds and the sum is %d\n", ((double)(end - start))/ CLOCKS_PER_SEC, sum);

  sum = 0;
  start = clock();
  for (j = 0; j < N; j++)
        for (i = 0; i < M; i++)
            sum += a[i][j];
  end = clock();
  printf("It takes %f seconds and the sum is %d\n", ((double)(end - start))/ CLOCKS_PER_SEC, sum);

  return 0;
}
