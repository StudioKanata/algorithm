import timeit
from basic_algorithm import addup, recursive_addup, addup_2

def run_benchmark():
    n = 800
    iterations = 10000

    print(f"Benchmarking with n={n}, {iterations} iterations...")

    # For loop
    t1 = timeit.timeit(lambda: addup(n), number=iterations)
    print(f"Loop (addup):      {t1:.5f} seconds")

    # Recursive
    t2 = timeit.timeit(lambda: recursive_addup(n), number=iterations)
    print(f"Recursive:         {t2:.5f} seconds")

    # Formula
    t3 = timeit.timeit(lambda: addup_2(n), number=iterations)
    print(f"Formula (addup_2): {t3:.5f} seconds")

if __name__ == "__main__":
    run_benchmark()
