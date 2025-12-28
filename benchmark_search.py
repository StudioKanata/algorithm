import timeit
from recursive_search import find_file_recursive, find_file_loop, file_system

def run_benchmark():
    target = "secret.txt"
    iterations = 100000

    print(f"Benchmarking search for '{target}' with {iterations} iterations...")

    # Recursive
    t1 = timeit.timeit(lambda: find_file_recursive(file_system, target), number=iterations)
    print(f"Recursive: {t1:.5f} seconds")

    # Loop (Iterative)
    t2 = timeit.timeit(lambda: find_file_loop(file_system, target), number=iterations)
    print(f"Loop:      {t2:.5f} seconds")

if __name__ == "__main__":
    run_benchmark()
