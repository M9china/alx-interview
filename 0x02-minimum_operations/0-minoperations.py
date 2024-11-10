def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        # While the divisor divides n, reduce n and count the operations
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
        
    return operations

# Example usage
print(minOperations(9))
