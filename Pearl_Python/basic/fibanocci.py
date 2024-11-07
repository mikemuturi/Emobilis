def fibonacci(n):
    # Handle the case for n less than or equal to 0
    if n <= 0:
        return []
    # Handle the case for n equal to 1
    elif n == 1:
        return [0]
    
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to n numbers
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence


print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
print(fibonacci(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
