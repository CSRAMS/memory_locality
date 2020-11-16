import java.lang.*;
public class sum{

    public static final int  N = 1024;
    public static final int  M = 1024;
    public static int i,j; public static int sum =0;
    public static int [][] array =  new int [M][N];
	public sum(){

	}
  public static void main (String[] args){
   for(i=0; i<M; i++)
      for(j=0; j<N; j++)
	  array[i][j] = 1;
   sum s = new sum();
     s.firstSum();
     s.secondSum();
 }

  public void firstSum(){
  final long startTime = System.nanoTime();
   for(i=0; i<M; i++)
      for(j=0; j<N; j++)
	sum+= array[i][j];
  final long duration = System.nanoTime()-startTime;
  System.out.println("It takes " + duration + " seconds and the sum is " + sum );
  }

  public void secondSum(){
  sum = 0;
  final long startTime = System.nanoTime();
   for(j=0; j<N; j++)
      for(i=0; i<M; i++)
	sum+= array[j][i];
  final long duration = System.nanoTime()-startTime;
  System.out.println("It takes " + duration + " seconds and the sums is " + sum );
  }
}


