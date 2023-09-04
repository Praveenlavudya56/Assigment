def fibonacci_with_loop(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = 10  # Change this value to the desired length of the Fibonacci series
result = fibonacci_with_loop(n)
print(result)
