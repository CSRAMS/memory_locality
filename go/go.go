package main

import "fmt"
import "time"

var M = 1024
var N = 1024

func main(){
    sum := 0
      a := make([][]int, M)
      for i := 0; i < M; i ++ {
    	a[i] = make([]int, N)
      	for j := 0; j < N; j++ {
          a[i][j] = 1
    }
  }

start := time.Now()
 for i := 0; i < M; i++{
    for j := 0; j < N; j++{
       sum += a[i][j];
   }
 }

duration := time.Since(start)
fmt.Println(duration.Nanseconds())

 sum2 := 0
  startTime := time.Now()
  for j := 0; j < N; j++{
     for i := 0; i < M; i++{
            sum2 += a[i][j]
   }
 }

durationTime := time.Since(startTime)
fmt.Println(durationTime.Nanoseconds())
}
