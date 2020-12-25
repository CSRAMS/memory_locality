use std::time::Instant;

pub fn main() {
    let N = 1024; let M = 1024;

    let mut arr = vec![vec![1i32; N]; M];

    let mut now = Instant::now();

    let mut sum = 0;

    for i in 0..M {
        for j in 0..N{
            sum += arr[i][j];
        }
    }

    let mut duration = Instant::now() - now;

    println!("{:?}", duration);
    println!("It took {:?} and the sum is {}", duration, sum);

    sum = 0;

    now = Instant::now();

    for i in 0..N {
        for j in 0..M{
            sum += arr[j][i];
        }
    }

    duration = Instant::now() - now;

    println!("It took {:?} and the sum is {}", duration, sum);

}
